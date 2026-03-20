"""
Headless Mesh Renderer — runs inside Blender's Python.

Produces multi-view renders + cross-section images of STL/OBJ meshes,
giving the AI agent visual understanding of 3D geometry.

Usage (from command line):
    blender --background --python mesh_render.py -- <mesh_path> [--output_dir <dir>] [--sections 3]

Output:
    <output_dir>/view_front.png
    <output_dir>/view_right.png
    <output_dir>/view_top.png
    <output_dir>/view_iso.png
    <output_dir>/view_bottom.png
    <output_dir>/view_rear.png
    <output_dir>/section_z_25pct.png
    <output_dir>/section_z_50pct.png
    <output_dir>/section_z_75pct.png
    <output_dir>/manifest.txt  (list of all outputs)
"""

import bpy
import bmesh
import sys
import os
import math
import mathutils
from pathlib import Path


def parse_args():
    """Parse arguments after the '--' separator."""
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []

    import argparse
    parser = argparse.ArgumentParser(description="Render mesh views for AI analysis")
    parser.add_argument("mesh_path", type=str, help="Path to STL/OBJ/PLY file")
    parser.add_argument("--output_dir", type=str, default=None,
                        help="Output directory (default: next to mesh file)")
    parser.add_argument("--sections", type=int, default=3,
                        help="Number of Z cross-sections (default: 3)")
    parser.add_argument("--resolution", type=int, default=1024,
                        help="Render resolution (default: 1024)")
    return parser.parse_args(argv)


def clear_scene():
    """Remove all objects from the scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    # Clear orphan data
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)


def import_mesh(filepath: str):
    """Import a mesh file, auto-detecting format."""
    ext = Path(filepath).suffix.lower()
    if ext == ".stl":
        bpy.ops.wm.stl_import(filepath=filepath)
    elif ext == ".obj":
        bpy.ops.wm.obj_import(filepath=filepath)
    elif ext == ".ply":
        bpy.ops.wm.ply_import(filepath=filepath)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=filepath)
    else:
        raise ValueError(f"Unsupported format: {ext}")

    obj = bpy.context.selected_objects[0]
    return obj


def get_mesh_info(obj):
    """Extract key dimensional info from the mesh."""
    # Apply transforms
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    xs = [v.x for v in bbox]
    ys = [v.y for v in bbox]
    zs = [v.z for v in bbox]

    info = {
        "min": (min(xs), min(ys), min(zs)),
        "max": (max(xs), max(ys), max(zs)),
        "size": (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)),
        "center": ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, (min(zs) + max(zs)) / 2),
        "vertices": len(obj.data.vertices),
        "faces": len(obj.data.polygons),
    }
    return info


def setup_scene(resolution: int = 1024):
    """Set up camera, lighting, and render settings for clean technical renders."""
    scene = bpy.context.scene

    # Render settings — Cycles (EEVEE fails headless, confirmed by Blender devs)
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'GPU'
    scene.cycles.samples = 64  # low sample count for speed; enough for technical renders
    scene.render.resolution_x = resolution
    scene.render.resolution_y = resolution
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'

    # Create camera
    cam_data = bpy.data.cameras.new("RenderCam")
    cam_data.type = 'ORTHO'
    cam_obj = bpy.data.objects.new("RenderCam", cam_data)
    scene.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    # Create key light
    light_data = bpy.data.lights.new("KeyLight", type='SUN')
    light_data.energy = 3.0
    light_obj = bpy.data.objects.new("KeyLight", light_data)
    light_obj.rotation_euler = (math.radians(45), math.radians(15), math.radians(45))
    scene.collection.objects.link(light_obj)

    # Create fill light
    fill_data = bpy.data.lights.new("FillLight", type='SUN')
    fill_data.energy = 1.5
    fill_obj = bpy.data.objects.new("FillLight", fill_data)
    fill_obj.rotation_euler = (math.radians(60), math.radians(-30), math.radians(-45))
    scene.collection.objects.link(fill_obj)

    # Set world background to dark grey for contrast
    world = bpy.data.worlds.new("TechWorld")
    scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get("Background")
    if bg_node:
        bg_node.inputs[0].default_value = (0.15, 0.15, 0.17, 1.0)

    return cam_obj


def apply_material(obj):
    """Apply a clean technical material (light grey, slight metallic)."""
    mat = bpy.data.materials.new("TechMat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (0.6, 0.65, 0.7, 1.0)
        bsdf.inputs["Metallic"].default_value = 0.3
        bsdf.inputs["Roughness"].default_value = 0.4
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def position_camera(cam_obj, mesh_info, view_name: str, padding: float = 1.3):
    """Position orthographic camera for the given view."""
    cx, cy, cz = mesh_info["center"]
    sx, sy, sz = mesh_info["size"]
    max_dim = max(sx, sy, sz) * padding

    cam_obj.data.ortho_scale = max_dim

    views = {
        "front":  ((cx, cy - max_dim, cz), (math.radians(90), 0, 0)),
        "rear":   ((cx, cy + max_dim, cz), (math.radians(90), 0, math.radians(180))),
        "right":  ((cx + max_dim, cy, cz), (math.radians(90), 0, math.radians(90))),
        "left":   ((cx - max_dim, cy, cz), (math.radians(90), 0, math.radians(-90))),
        "top":    ((cx, cy, cz + max_dim), (0, 0, 0)),
        "bottom": ((cx, cy, cz - max_dim), (math.radians(180), 0, 0)),
        "iso":    ((cx + max_dim * 0.7, cy - max_dim * 0.7, cz + max_dim * 0.5),
                   (math.radians(55), 0, math.radians(45))),
    }

    loc, rot = views[view_name]
    cam_obj.location = loc
    cam_obj.rotation_euler = rot


def render_view(cam_obj, mesh_info, view_name: str, output_path: str):
    """Render a single view."""
    position_camera(cam_obj, mesh_info, view_name)
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    print(f"  ✅ Rendered: {view_name} → {output_path}")


def create_cross_section(obj, mesh_info, z_fraction: float):
    """
    Create a cross-section by bisecting the mesh at a Z height.
    Returns the bisected object (upper half removed).
    """
    z_min, z_max = mesh_info["min"][2], mesh_info["max"][2]
    z_cut = z_min + (z_max - z_min) * z_fraction

    # Duplicate the object for sectioning
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.duplicate()
    section_obj = bpy.context.active_object
    section_obj.name = f"Section_{int(z_fraction * 100)}pct"

    # Enter edit mode and bisect
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')

    # Bisect: cut at z_cut, clear the upper half
    bpy.ops.mesh.bisect(
        plane_co=(0, 0, z_cut),
        plane_no=(0, 0, 1),
        clear_outer=True,
        clear_inner=False,
        use_fill=True,
    )

    bpy.ops.object.mode_set(mode='OBJECT')
    return section_obj, z_cut


def render_sections(obj, cam_obj, mesh_info, output_dir: str, n_sections: int = 3):
    """Render cross-section views at evenly spaced Z heights."""
    rendered = []
    # Use original mesh XY extent for camera framing
    orig_sx, orig_sy, _ = mesh_info["size"]
    frame_dim = max(orig_sx, orig_sy) * 1.4

    for i in range(1, n_sections + 1):
        fraction = i / (n_sections + 1)
        pct = int(fraction * 100)

        # Hide the original, show section
        obj.hide_render = True
        section_obj, z_cut = create_cross_section(obj, mesh_info, fraction)

        # Apply section material (orange for visibility)
        mat = bpy.data.materials.new(f"SectionMat_{pct}")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = (0.9, 0.4, 0.1, 1.0)
            bsdf.inputs["Metallic"].default_value = 0.1
            bsdf.inputs["Roughness"].default_value = 0.6
        section_obj.data.materials.clear()
        section_obj.data.materials.append(mat)

        # Get actual section bounds for camera targeting
        sec_bbox = [section_obj.matrix_world @ mathutils.Vector(c) for c in section_obj.bound_box]
        sec_xs = [v.x for v in sec_bbox]
        sec_ys = [v.y for v in sec_bbox]
        sec_zs = [v.z for v in sec_bbox]
        sec_cx = (min(sec_xs) + max(sec_xs)) / 2
        sec_cy = (min(sec_ys) + max(sec_ys)) / 2
        sec_cz = (min(sec_zs) + max(sec_zs)) / 2

        # Render from iso angle, centered on section, using original scale
        cam_obj.data.ortho_scale = frame_dim
        cam_obj.location = (
            sec_cx + frame_dim * 0.7,
            sec_cy - frame_dim * 0.7,
            sec_cz + frame_dim * 0.5
        )
        cam_obj.rotation_euler = (math.radians(55), 0, math.radians(45))

        output_path = os.path.join(output_dir, f"section_z_{pct}pct.png")
        bpy.context.scene.render.filepath = output_path
        bpy.ops.render.render(write_still=True)
        print(f"  ✅ Section at Z={z_cut:.1f}mm ({pct}%) → {output_path}")
        rendered.append(output_path)

        # Clean up section
        bpy.ops.object.select_all(action='DESELECT')
        section_obj.select_set(True)
        bpy.ops.object.delete()

        obj.hide_render = False

    return rendered


def write_manifest(output_dir: str, mesh_path: str, mesh_info: dict, files: list):
    """Write a manifest file listing all outputs and mesh stats."""
    manifest_path = os.path.join(output_dir, "manifest.txt")
    with open(manifest_path, "w") as f:
        f.write(f"Mesh Render Manifest\n")
        f.write(f"{'=' * 50}\n")
        f.write(f"Source: {mesh_path}\n")
        f.write(f"Vertices: {mesh_info['vertices']:,}\n")
        f.write(f"Faces: {mesh_info['faces']:,}\n")
        f.write(f"Bounding Box (mm): {mesh_info['size'][0]:.1f} × {mesh_info['size'][1]:.1f} × {mesh_info['size'][2]:.1f}\n")
        f.write(f"Center: ({mesh_info['center'][0]:.1f}, {mesh_info['center'][1]:.1f}, {mesh_info['center'][2]:.1f})\n")
        f.write(f"{'=' * 50}\n")
        f.write(f"\nRendered files:\n")
        for fp in files:
            f.write(f"  {os.path.basename(fp)}\n")
    print(f"  📋 Manifest: {manifest_path}")
    return manifest_path


def main():
    args = parse_args()
    mesh_path = os.path.abspath(args.mesh_path)

    if not os.path.exists(mesh_path):
        print(f"❌ File not found: {mesh_path}")
        sys.exit(1)

    # Output directory
    if args.output_dir:
        output_dir = os.path.abspath(args.output_dir)
    else:
        mesh_name = Path(mesh_path).stem
        output_dir = os.path.join(os.path.dirname(mesh_path), f"{mesh_name}_renders")

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n{'=' * 50}")
    print(f"  Mesh Renderer — {Path(mesh_path).name}")
    print(f"  Output: {output_dir}")
    print(f"{'=' * 50}\n")

    # Setup
    clear_scene()
    obj = import_mesh(mesh_path)
    mesh_info = get_mesh_info(obj)

    print(f"  📐 Bbox: {mesh_info['size'][0]:.1f} × {mesh_info['size'][1]:.1f} × {mesh_info['size'][2]:.1f} mm")
    print(f"  📊 {mesh_info['vertices']:,} verts, {mesh_info['faces']:,} faces\n")

    cam_obj = setup_scene(args.resolution)
    apply_material(obj)

    # Render views
    rendered_files = []
    for view in ["front", "right", "top", "iso", "bottom", "rear"]:
        fp = os.path.join(output_dir, f"view_{view}.png")
        render_view(cam_obj, mesh_info, view, fp)
        rendered_files.append(fp)

    # Render cross-sections
    if args.sections > 0:
        section_files = render_sections(
            obj, cam_obj, mesh_info, output_dir, args.sections
        )
        rendered_files.extend(section_files)

    # Write manifest
    manifest = write_manifest(output_dir, mesh_path, mesh_info, rendered_files)
    rendered_files.append(manifest)

    print(f"\n✅ Done! {len(rendered_files) - 1} renders + manifest")


if __name__ == "__main__":
    main()
