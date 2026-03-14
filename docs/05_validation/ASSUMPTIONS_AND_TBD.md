# Assumptions and TBD Register

Discipline in tracking knowledge state is critical for this rebaseline. Every engineering parameter exists in one of three buckets:

## 1. Verified (Ground Truth)
Parameters validated by OEM datasheet or direct measurement.
- **Donor:** Bose FreeSpace DS 100F
- **Architecture:** Ported
- **LF/HF Drivers:** 5.25" / 2.25"
- **Nominal Impedance:** 8 Ω
- **Dispersion:** 160° conical

## 2. Assumed (Working Theory - Must Verify)
Parameters assumed for planning but pending hard verification.
- The 430 × 280 mm Formech 300XQ envelope is sufficient for a single-pull upper shell.
- The 5.9 kg donor weight includes a ~1.0 kg transformer that can be discarded.
- The recommended high-pass filter is ≈55 Hz.

## 3. Unknown (TBD - Blocked)
Parameters totally unknown, requiring active measurement before CAD can proceed.
- Internal acoustic volume.
- Port tube inner diameter, length, and flare profile.
- Driver mounting pitch circle and baffle cutouts.
- Crossover PCB bounding box.
- Monitor arm mounting tube diameter and clearance.
