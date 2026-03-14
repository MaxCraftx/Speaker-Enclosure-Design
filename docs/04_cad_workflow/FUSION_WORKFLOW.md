# Fusion 360 Scan-to-CAD Workflow

This repository enforces a strict, robust workflow for reverse-engineering the DS 100F scans into a manufacturable enclosure in Fusion 360 (January 2026 or later, with Design Extension).

## 1. Top-Down Master Assembly
The main design file (`10-ENC-ASSY`) contains the master coordinate system and drives all sub-components.
- Do **not** build parts in separate files and assemble them later.
- Build sub-components in place within the master assembly.

## 2. Mesh Handling (The "Reference, Don't Convert" Rule)
Fusion's prismatic mesh-to-solid conversion (even with 2026 improvements) remains unreliable on complex, noisy 3D scan data. 
- **Rule:** Keep the imported `.stl` or `.obj` meshes as **Reference Components**.
- **Do not** attempt to convert the entire backcan or front baffle into a Solid B-Rep body.
- Hide the mesh component when not actively referencing it.

## 3. Reverse Engineering Technique
Extract parametric truth from the noisy mesh:
1. Create a Construction Plane intersecting the mesh at a critical feature (e.g., across the port center).
2. Create a Sketch on that plane.
3. Use **Create > Mesh Section Sketch** to project the mesh intersection into the sketch.
4. Use standard sketch tools (Line, Circle, Spline) to trace the section. Constrain these lines to the Master Datums or User Parameters.
5. Extrude/Revolve/Loft these bounded sketches to build the parametric solid.

*Exception:* You may use the "Organic" (T-Spline) conversion tool from the Design Extension **only** for highly localized, mathematically complex surfaces (e.g., the specific curvature of the aerodynamic port flare) if they cannot be reasonably replicated via lofts. This must be done on a pre-segmented subset of the mesh, never the whole file.

## 4. Master Datums
Before sketching, establish the key coordinate systems in the assembly root:
- **Global Origin:** Centered on the geometric center of the workstation mounting arm clamp.
- **Listening Axis:** A construction axis aiming ≈15–20° downward from horizontal.
- **Baffle Plane:** The angled mounting face for the DS 100F driver array.
- **Port Axis:** The centerline of the bass reflex tube.

## 5. Acoustic Volume Verification
The internal volume must be precisely tracked as wall thicknesses and stiffening ribs are manipulated.
1. Create a solid body representing the **Internal Cavity** (the negative space of the enclosure).
2. Measure its Volume via the `Properties` dialog.
3. Compare this to the scan-extracted baseline target.
4. The final shell is created via a Boolean Subtract/Combine: (Outer Shell Body) - (Internal Cavity Body) - (Port Solid Body).
