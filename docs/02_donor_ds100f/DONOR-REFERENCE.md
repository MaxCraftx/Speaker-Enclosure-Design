# Bose FreeSpace DS 100F: Donor Reference

This document serves as the master specification for the donor components. 

## Source Verification Protocol
Every property must be traced to one of the following sources:
- **Datasheet Verified**: Explicitly stated in Bose technical documentation.
- **Scan Verified**: Extracted explicitly from a Creality CR-Scan Raptor point cloud in CloudCompare or Fusion 360.
- **Measured by Teardown**: Physical measurement with calipers, scales, or REW acoustic sweep.
- **Engineering Estimate**: Pending formal verification. MUST be upgraded before final CAD freeze.

---

## 1. Transducer Specifications

| Parameter | Value | Verification Status | Notes |
|-----------|-------|--------------------|-------|
| Low-Frequency Driver | 5.25" (133 mm) woofer | Datasheet Verified | |
| High-Frequency Driver | 2.25" (57 mm) Twiddler® | Datasheet Verified | Centrally mounted |
| Nominal Impedance | 8 Ω | Datasheet Verified | Transformer bypassed |

## 2. Acoustic Performance

| Parameter | Value | Verification Status | Notes |
|-----------|-------|--------------------|-------|
| Frequency Response (±3 dB) | 75 Hz – 18 kHz | Datasheet Verified | |
| Frequency Range (−10 dB) | 60 Hz – 20 kHz | Datasheet Verified | |
| Nominal Dispersion | 160° conical | Datasheet Verified | Ideal for near-field off-axis |
| Sensitivity (1 W / 1 m) | 85 dB SPL | Datasheet Verified | |
| Max SPL (Continuous) | 105 dB | Datasheet Verified | |
| Power Handling (Continuous) | 100 W | Datasheet Verified | |
| Recommended High-Pass | 55 Hz (estimated) | Engineering Estimate | Datasheet is silent on exact HPF required; must verify via Bose DSP presets or REW testing |

## 3. Physical Specifications 

| Parameter | Value | Verification Status | Notes |
|-----------|-------|--------------------|-------|
| Enclosure Type | Ported | Datasheet Verified | Explicitly listed as ported |
| Total Unit Weight | 5.9 kg (13 lbs) | Datasheet Verified | Includes transformer/backcan |
| Outer Flange Diameter | 299 mm (11.8") | Datasheet Verified | |
| Depth | 193 mm (7.6") | Datasheet Verified | |
| Mounting Hole Cutout | 267 mm (10.5") | Datasheet Verified | |

## 4. Unknowns Requiring Extraction from Scans

The following properties are **unknown** from the datasheet and must be measured:
1. **Internal Acoustic Volume**: The precise cubic volume enclosing the rear of the drivers.
2. **Bass Reflex Port Inner Diameter**: The flare and throat diameter of the port tube.
3. **Bass Reflex Port Length**: The acoustic centerline length of the port tube.
4. **Driver Mounting Pitch Circle**: The hole pattern securing the driver assembly to the baffle.
5. **Crossover Board Envelope**: The 3D bounding box for the bare PCB (with transformer removed).
6. **Transformer Mass Saving**: Exact weight of the 70V/100V transformer yielding net assembly weight.
