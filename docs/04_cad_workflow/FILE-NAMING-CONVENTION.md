# File and Component Naming Convention

Adhere to the following nomenclature within Fusion 360 and GitHub LFS.

## 1. Fusion 360 Documents (Projects / Assemblies)
Format: `[ID]-[TYPE]-[NAMESPACE]-[Subname]`
- `10-ENC-ASSY` (Master Speaker Enclosure Assembly)
- `20-MNT-ASSY` (Workstation Monitor Arm Bracket Assembly)
- `30-MLD-ASSY` (Vacuum Forming Mould Tooling Assembly)

## 2. Component Naming (Inside the Assembly)
Format: `[Category]_[Description]`
- Categories:
  - `REF`: Reference meshes / scan data (e.g., `REF_DS100F_Backcan`)
  - `ENV`: Environment/Obstacles (e.g., `ENV_Monitor_Arm`)
  - `SHL`: Shell Plastics (e.g., `SHL_Top_Cover`)
  - `BFL`: Baffle & Internal Structure (e.g., `BFL_Main`)
  - `PRT`: Acoustic Port geometry (e.g., `PRT_Reflex_Tube`)
  - `HRD`: Hardware/Fasteners (e.g., `HRD_M5_Insert`)

## 3. Body Naming
Rename bodies immediately upon creation to prevent `Body1`, `Body2`.
- `Target_Cavity`
- `Shell_Blank`
- `Rib_Pattern`
- `Port_Cutout_Tool`

## 4. Export Nomenclature (STL, STEP, IGES)
Format: `[Revision]-[Component]-[Date/Desc].[ext]`
Example: `v04-SHL_Top_Cover-For_Print.stl`

*Note: Milestone `.f3z` archives committed to Git LFS should use semantic version tags matching the repository release.*
