# Geometry Register

This file logs all physical geometric parameters for the DS 100F donor. No parameter enters the master CAD model without a logged verification status here.

| Parameter Name | Value | Tolerance | Source | Status |
|----------------|-------|-----------|--------|--------|
| `flange_outer_dia` | 299.0 mm | ± 1.0 mm | Datasheet | Verified |
| `housing_depth` | 193.0 mm | ± 1.0 mm | Datasheet | Verified |
| `backcan_bbox` | 257.2 × 183.7 × 252.6 mm | ± 2.0 mm | Scan bounding box (trimesh) | Extracted — needs validation |
| `backcan_convex_vol` | 8.019 L (convex hull) | — | Scan (trimesh) | Upper bound only — mesh non-watertight |
| `connector_box_bbox` | 155.9 × 55.5 × 138.7 mm | ± 2.0 mm | Scan bounding box (trimesh) | Extracted — needs validation |
| `base_assy_bbox` | 300.3 × 149.8 × 299.9 mm | ± 2.0 mm | Scan bounding box (trimesh) | Extracted — needs validation |
| `vent_tube_scan_bbox` | 111.0 × 74.3 × 119.8 mm | ± 2.0 mm | Scan bounding box (trimesh) | Extracted — includes surrounding geometry |
| `port_inner_dia` | TBD mm | ± 0.5 mm | Physical caliper or visual scan measurement | **Unknown** |
| `port_length` | TBD mm | ± 0.5 mm | Physical caliper or visual scan measurement | **Unknown** |
| `port_flare_profile` | TBD | — | Physical caliper or visual scan measurement | **Unknown** |
| `driver_pitch_dia` | TBD mm | ± 0.1 mm | Scan or caliper | **Unknown** |
| `baffle_thickness` | TBD mm | ± 0.2 mm | Scan or caliper | **Unknown** |
| `pcb_bounding_box` | TBD × TBD × TBD mm | ± 1.0 mm | Teardown | **Unknown** |
| `transformer_weight` | TBD kg | ± 0.01 kg | Teardown | **Unknown** |
| `ac_vol_target` | 7.28 L | ± 0.1 L | Watertight inner shell measurement | **Verified** |

## Notes
- **Bounding boxes** from trimesh are reliable (they just measure the axis-aligned extents of the point cloud).
- **Cross-section derived "diameters" from the vent tube scan were INVALID** — the slicing captured exterior geometry (flanges, walls, scan artifacts) and produced meaningless equivalent diameters. These have been removed.
- **Convex hull volume** is an upper bound, not the true internal acoustic volume.
- Port tube inner dimensions, driver pitch, and acoustic volume **require either physical caliper measurement or proper visual measurement** from the scan in a viewer (MeshLab, CloudCompare, or Fusion 360 mesh workspace).

*Any parameter marked 'Unknown' requires a GitHub Issue using the Measurement Task template.*
