# Speaker Enclosure Design

Custom lightweight speaker enclosures for a curved zero-gravity workstation. 

This repository serves as the engineering workspace for redesigning **Bose FreeSpace DS 100F** donor acoustic components into custom, overhead-mounted housings.

## Donor Baseline
The core donor is the **Bose DS 100F**:
- 5.25" woofer + 2.25" Twiddler® driver
- Ported acoustic architecture
- 160° conical coverage (ideal for near-field overhead mounting)

*Note: This project was originally conceptualized around the Bose DesignMax DM8C. All legacy DM8C assumptions (sealed 21.8L volume, 8" coaxial) have been superseded by the DS 100F rebaseline.*

## Current Status
- **Scans completed:** Front panel/base, backcan, connector panel, and bass reflex vent have been captured (Creality Scan 4.7, CR-Scan Raptor).
- **Engineering OS:** Documentation and reverse engineering are actively moving into Fusion 360.
- **Next Steps:** Datum extraction, port geometry measurement, and master assembly creation.

## Repository Structure
- `docs/01_project_rebaseline/`: Reports on the DM8C to DS 100F transition
- `docs/02_donor_ds100f/`: Extracted dimensional and acoustic registers for the new donor
- `docs/03_scans/`: Inventory and processing workflow for 3D scan data
- `docs/04_cad_workflow/`: Fusion 360 conventions and parameter schemas
- `docs/05_validation/`: Measurement and testing plans
- `DESIGN_PROPOSAL.md`: The core design concepts and architecture

## Usage
This repo establishes a strict scan-driven CAD workflow. Please see `docs/04_cad_workflow/FUSION_WORKFLOW.md` before contributing CAD data, and review `PROJECT_BACKLOG.md` for current priorities.
