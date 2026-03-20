"""
Automated Mesh Repair & Poisson Reconstruction (with Collar Trimming).
This script chains the necessary MeshLab filters to clean raw scans,
reconstruct a watertight surface, and trim the extrapolated "collar".

Usage:
    python reconstruct_and_trim.py <input_mesh> [quality_threshold]
    
    quality_threshold: The density threshold for removing the Poisson collar.
                       Defaults to 5.0. Increase it if too much of the real
                       mesh is deleted; decrease it if the collar remains.
"""
import pymeshlab
import sys
import os
import argparse

def process_mesh(input_path: str, quality_threshold: float):
    print(f"\n{'='*50}")
    print(f"Processing: {os.path.basename(input_path)}")
    print(f"{'='*50}")
    
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    ms = pymeshlab.MeshSet()
    
    # --- PHASE 1: Loading & Cleaning -----------------------------------------
    print("\n[1/4] Loading and cleaning raw mesh...")
    ms.load_new_mesh(input_path)
    print(f"      Original: {ms.current_mesh().vertex_number():,} vertices, {ms.current_mesh().face_number():,} faces")
    
    # Crucial cleaning sequence for merged inner/outer scans
    ms.meshing_remove_duplicate_vertices()
    ms.meshing_remove_duplicate_faces()
    ms.meshing_repair_non_manifold_edges()
    ms.meshing_repair_non_manifold_vertices()
    # ms.meshing_remove_t_vertices() # Sometimes destabilizes, skipping unless necessary
    ms.meshing_remove_unreferenced_vertices()
    
    m = ms.current_mesh()
    print(f"      Cleaned:  {m.vertex_number():,} vertices, {m.face_number():,} faces")

    # --- PHASE 2: Normals & Poisson Reconstruction ---------------------------
    print("\n[2/4] Computing normals and running Poisson reconstruction...")
    # Compute normals using 20 neighbors
    ms.compute_normal_for_point_clouds(k=20)
    
    # Screened Poisson Surface Reconstruction
    # depth=9 is a good balance of detail and performance.
    # preclean=True helps with remaining scan noise.
    ms.generate_surface_reconstruction_screened_poisson(depth=9, preclean=True)
    
    m = ms.current_mesh()
    print(f"      Reconstructed: {m.vertex_number():,} vertices, {m.face_number():,} faces")

    # --- PHASE 3: Trimming the "Collar" --------------------------------------
    print(f"\n[3/4] Trimming Poisson extrapolation (threshold: {quality_threshold})...")
    # Poisson stores the point density of the original scan in the Vertex Quality field (q).
    # Areas where it extrapolated (the collar) have very low density (q values).
    
    # Select vertices where quality is strictly less than our threshold
    condition = f"q < {quality_threshold}"
    try:
        ms.compute_selection_by_condition_per_vertex(condselect=condition)
        
        # Delete the selected collar faces/vertices
        ms.meshing_remove_selected_vertices()
        
        m = ms.current_mesh()
        print(f"      Trimmed shape: {m.vertex_number():,} vertices, {m.face_number():,} faces")
    except Exception as e:
        print(f"      ⚠️ Trimming failed (maybe no vertices met condition?): {e}")

    # --- PHASE 4: Export -----------------------------------------------------
    print("\n[4/4] Exporting final mesh...")
    base, ext = os.path.splitext(input_path)
    out_path = f"{base}_watertight_trimmed.stl"
    
    ms.save_current_mesh(out_path)
    print(f"      ✅ Saved: {out_path}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean, reconstruct, and trim a 3D scan.")
    parser.add_argument("input_path", type=str, help="Path to the input STL/OBJ/PLY file")
    parser.add_argument("--threshold", "-t", type=float, default=5.0, 
                        help="Vertex quality threshold to delete the Poisson collar (default: 5.0). "
                             "Higher = deletes more. Lower = deletes less.")
    
    args = parser.parse_args()
    process_mesh(args.input_path, args.threshold)
