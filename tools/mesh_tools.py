"""
Mesh Tools for Speaker Enclosure Design.
Wraps PyMeshLab and trimesh for scan processing.

Usage:
    from tools.mesh_tools import repair_mesh, measure_mesh, open_in_cloudcompare
"""

import pymeshlab
import trimesh
import numpy as np
import os
import subprocess

CLOUDCOMPARE_PATH = r"C:\Program Files\CloudCompare\CloudCompare.exe"


def repair_mesh(input_path: str, output_path: str = None, max_hole_size: int = 1000) -> dict:
    """
    Repair a mesh: remove duplicates, fix non-manifold, close holes.
    
    Args:
        input_path: Path to the input mesh file (.stl, .obj, .ply)
        output_path: Path to save the repaired mesh (default: adds _repaired suffix)
        max_hole_size: Maximum hole size to close (in edges)
    
    Returns:
        dict with repair statistics
    """
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_repaired.stl"
    
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(input_path)
    
    m = ms.current_mesh()
    orig_v, orig_f = m.vertex_number(), m.face_number()
    
    ms.meshing_remove_duplicate_vertices()
    ms.meshing_remove_duplicate_faces()
    ms.meshing_repair_non_manifold_edges()
    ms.meshing_repair_non_manifold_vertices()
    ms.meshing_remove_null_faces()
    ms.meshing_close_holes(maxholesize=max_hole_size)
    
    m = ms.current_mesh()
    ms.save_current_mesh(output_path)
    
    geom = ms.get_geometric_measures()
    
    return {
        "original_vertices": orig_v,
        "original_faces": orig_f,
        "repaired_vertices": m.vertex_number(),
        "repaired_faces": m.face_number(),
        "bbox_mm": [round(m.bounding_box().dim_x(), 1),
                     round(m.bounding_box().dim_y(), 1),
                     round(m.bounding_box().dim_z(), 1)],
        "volume_mm3": round(abs(geom.get('mesh_volume', 0)), 1),
        "volume_litres": round(abs(geom.get('mesh_volume', 0)) / 1e6, 4),
        "surface_area_mm2": round(geom.get('surface_area', 0), 1),
        "output_path": output_path,
    }


def measure_mesh(path: str) -> dict:
    """
    Measure a mesh file and return key dimensions.
    
    Returns:
        dict with vertices, faces, bbox, volume, surface area
    """
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(path)
    m = ms.current_mesh()
    
    bb = m.bounding_box()
    geom = ms.get_geometric_measures()
    
    vol = abs(geom.get('mesh_volume', 0))
    
    return {
        "vertices": m.vertex_number(),
        "faces": m.face_number(),
        "bbox_mm": [round(bb.dim_x(), 1), round(bb.dim_y(), 1), round(bb.dim_z(), 1)],
        "center_mm": [round((bb.min()[0] + bb.max()[0]) / 2, 1),
                       round((bb.min()[1] + bb.max()[1]) / 2, 1),
                       round((bb.min()[2] + bb.max()[2]) / 2, 1)],
        "volume_mm3": round(vol, 1),
        "volume_litres": round(vol / 1e6, 4),
        "surface_area_mm2": round(geom.get('surface_area', 0), 1),
    }


def decimate_mesh(input_path: str, output_path: str = None, target_faces: int = 50000) -> str:
    """
    Decimate a mesh to a target face count for faster CAD reference loading.
    
    Returns:
        Path to decimated mesh
    """
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_decimated.stl"
    
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(input_path)
    
    m = ms.current_mesh()
    if m.face_number() > target_faces:
        ms.meshing_decimation_quadric_edge_collapse(targetfacenum=target_faces)
    
    ms.save_current_mesh(output_path)
    return output_path


def open_in_cloudcompare(*paths: str):
    """Open one or more mesh files in CloudCompare GUI."""
    cmd = [CLOUDCOMPARE_PATH]
    for p in paths:
        cmd.extend(["-O", p])
    subprocess.Popen(cmd)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"Measuring: {path}")
        result = measure_mesh(path)
        for k, v in result.items():
            print(f"  {k}: {v}")
    else:
        print("Usage: python mesh_tools.py <path_to_mesh>")
