# Change Impact Report: DM8C to DS 100F Rebaseline

## 1. Donor Change Summary

The project was originally structured around repurposing the Bose DesignMax DM8C. It has been formally rebaselined to use the **Bose FreeSpace DS 100F**. 
All documentation, CAD intent, and validation plans must reflect this change.

## 2. Acoustic Architecture Impact
- **Prior intent (DM8C):** 8-inch coaxial point source, treated as sealed internal volume (or unknown).
- **New intent (DS 100F):** 5.25-inch woofer and 2.25-inch Twiddler® driver array. Explicitly **ported** architecture.
- **Consequence:** The internal volume target and bass reflex vent dimensions must now be extracted from the scans of the DS 100F backcan and preserved in the new enclosure.

## 3. Geometry Impact
- **Prior intent (DM8C):** 21.8 L internal volume, large 409 mm grille diameter, ~340 mm backcan.
- **New intent (DS 100F):** The DS 100F is significantly more compact (299 mm outer flange, 193 mm depth).
- **Consequence:** The required internal acoustic volume is substantially smaller (exact value TBD pending scan extraction). The physical size of the final custom enclosure will be reduced, improving workstation packaging and sightlines.

## 4. Mass Budget Impact
- **Prior intent (DM8C):** Donor total weight 9.6 kg.
- **New intent (DS 100F):** Donor total weight 5.9 kg.
- **Consequence:** The project enjoys a much more forgiving mass budget. The target weight of ≤ 4.5 kg per enclosure remains, but it is much easier to achieve given the lighter donor.

## 5. Design Language Implications
- The 160° conical coverage of the DS 100F is even wider than the DM8C's 135°. This further reduces the criticality of precise angular alignment toward the operator.
- The dual-driver arrangement (woofer + Twiddler) introduces a new baffle face constraint compared to the single coaxial driver.

## 6. Manufacturing Implications
- Lighter donor components mean internal mounting bosses and baffle structures do not need to be as robust as previously envisioned. Vacuum-formed HIPS remains the primary shell strategy.

## 7. Validation Implications
- The acoustic validation baseline shifts to 75 Hz – 18 kHz (±3 dB).
- Port tuning frequency must be explicitly verified against the donor behavior.

## 8. Explicit List of Legacy Assumptions to Delete
The following assumptions from the concept phase are **superseded and invalid**:
1. "The enclosure requires 21.8 litres of internal volume."
2. "The donor is an 8-inch coaxial driver."
3. "The acoustic loading type is unknown/sealed."
4. "The donor weighs 9.6 kg."
5. "Siemens NX is the primary CAD software." (Now Fusion 360).
