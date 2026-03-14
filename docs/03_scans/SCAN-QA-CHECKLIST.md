# Scan QA Checklist

Before exporting a mesh for CAD use in Fusion 360, it must pass the following QA criteria.

## 1. Raw Point Cloud Quality (Creality Scan)
- [ ] Captured in blue laser mode (for CR-Scan Raptor).
- [ ] No major occlusion zones or "shadows" on critical geometry (e.g., inside the port tube).
- [ ] Tracking maintained consistently; no ghosting or duplicated surfaces.

## 2. Fusion and Cleaning (CloudCompare / Blender)
- [ ] Point cloud correctly fused into a manifold mesh.
- [ ] Extraneous data (background, table, mounting putty) segmented and deleted.
- [ ] Face count reduced to ≤ 10,000 polygons (via Blender Decimate or CloudCompare Poisson Recon) to prevent Fusion 360 instability.

## 3. Alignment
- [ ] Mesh oriented to a logical coordinate system (e.g., Z-axis = driver firing axis).
- [ ] Origin point established at a meaningful geometric datum (e.g., backcan mounting flange center).

## 4. Final Export
- [ ] Exported as standard format (`.stl`, `.ply`, or `.obj`).
- [ ] Verified scale in CAD (check one known bounding dimension with calipers).
