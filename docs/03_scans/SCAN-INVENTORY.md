# Scan Inventory

This document tracks the status of all 3D scan data captured for the DS 100F rebaseline. 

| Component | Status | Capture Tool | Alignment | Ref File | Notes |
|-----------|--------|--------------|-----------|----------|-------|
| Front Panel / Base | Completed | CR-Scan Raptor | TBD | `base_with_components` (.stl/.obj/.ply) | Includes driver array. BBox: 300×150×300mm |
| Backcan | Completed | CR-Scan Raptor | TBD | `metal backcan.obj` (57MB) | Non-watertight mesh, 1.05M faces. Convex hull vol: 8.0L |
| Connector Panel | Completed | CR-Scan Raptor | TBD | `connector box` (.obj/.stl) | BBox: 156×56×139mm |
| Bass Reflex Vent | Completed | CR-Scan Raptor | TBD | `bassreflex vent pipe` (.obj/.stl) | Flared port: entry Ø40→bore Ø27→exit Ø20mm, length ~120mm |
| Workstation Arm | **Missing** | TBD | TBD | TBD | Must capture mounting zone clearance |

## Scan Analysis Results (2026-03-15)

Automated analysis performed by `trimesh` Python library. Results stored in `scan_analysis_results.json`.

### Key Findings
- **None of the meshes are watertight** — typical for raw CR-Scan Raptor captures
- The backcan mesh has significant holes, making internal volume extraction unreliable. Mesh repair recommended before CAD import.
- The vent tube shows a clear **flared bass-reflex port profile** — this is consistent with professional port design for reducing turbulent noise (chuffing)
- Simplified base assembly mesh (15MB) is available for faster loading

*All completed scans were captured in Creality Scan 4.7 using the CR-Scan Raptor in blue laser mode. Meshes were fused from point clouds internally within the Creality application.*
