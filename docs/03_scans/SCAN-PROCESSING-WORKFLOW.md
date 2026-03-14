# Scan Processing Workflow: Capture to CAD

This document defines the 7-stage pipeline for translating a physical DS 100F component into actionable Fusion 360 geometry.

## Stage 1: Raw Capture
**Tool:** Creality Scan 4.7 + CR-Scan Raptor
- Use blue laser mode for 0.02 mm accuracy.
- Apply tracking markers if the part lacks geometric uniqueness.
- Execute multiple passes if necessary to overcome occlusions.
- Run internal point cloud fusion.

## Stage 2: Alignment & Segmentation
**Tool:** CloudCompare 2.14 beta
- Import the raw fused mesh.
- Use cutting planes or manual segmentation to isolate the component of interest (e.g., separating the vent from the backcan).
- Align the part to the global coordinate system (ICP or Point-Pair picking against synthetic reference planes).

## Stage 3: Volume & Datum Extraction
**Tool:** CloudCompare 2.14 beta
- Use the **Volume Computation** tool (2.5D grid-based) on a closed backcan mesh to establish the precise internal acoustic volume.
- Use **Cross-Section & Profile** to extract DXF slices of the bass reflex port.

## Stage 4: Mesh Cleanup & Reduction
**Tool:** Blender 4.1
- **Critical:** Fusion 360 performs poorly with high-poly meshes. 
- Use the Decimate modifier to reduce face count by ≥80% (target < 10,000 faces), preserving edge flow where possible.

## Stage 5: Neutral Export
**Tool:** Blender 4.1
- Export the decimated, aligned mesh as `.stl` or `.obj`.
- Retain the coordinate origin established in Stage 2.

## Stage 6: Fusion 360 Import & Referencing
**Tool:** Fusion 360 Design Extension
- Insert the decimated mesh component.
- **Do NOT** use "Convert Mesh" (prismatic conversion) on the entire body unless it is exceptionally clean.
- Ensure the reference mesh is locked in the timeline.

## Stage 7: Reverse Engineering
**Tool:** Fusion 360 Design Extension
- Create offset planes and use **Create Mesh Section Sketch** to extract true splines and circles.
- Drive parametric solid sweeps, lofts, and extrudes from these extracted sketches, never directly from the mesh faces.
- *Optional:* Use "Organic" T-Spline conversion only for highly localized subsets of geometry (e.g., complex port flares) that cannot be parametrically swept.
