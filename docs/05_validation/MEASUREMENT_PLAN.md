# Measurement Plan

This plan resolves the items in the "Unknown (TBD)" bucket.

## Phase 1: Scan Extraction (CloudCompare)
**Owner:** CAD / Validation
**Objective:** Non-destructive geometric extraction.
1. `ac_vol_target`: Isolate the backcan scan. Cap the front opening. Run Volume Computation.
2. `ac_port_id` & `ac_port_len`: Section the vent scan. Measure DXF profile.

## Phase 2: Physical Teardown Verification
**Owner:** Engineering
**Objective:** Hard validation of internal components.
1. `pcb_bounding_box`: Remeasure the crossover board with calipers.
2. `transformer_weight`: Weigh the 70V transformer to confirm mass savings.
3. `driver_pitch_dia`: Confirm bolt hole radial position on the actual driver chassis.

## Phase 3: Acoustic Baseline Validation
**Owner:** Acoustic
**Objective:** Define the target curve before enclosure design.
1. Perform a free-air or infinite baffle impedance sweep (REW / DATS) on the raw driver array to find Fs and confirm T/S parameters if simulation (VituixCAD) is desired.
2. Characterize the crossover network transfer function (if possible without destruction).
