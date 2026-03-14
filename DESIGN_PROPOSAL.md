# Custom Lightweight Speaker Enclosures for Curved Zero-Gravity Workstation

**Redesign of Bose FreeSpace DS 100F donor acoustic components into futuristic, vacuum-formed workstation-integrated stereo housings**

---

<table>
<tr>
<td width="55%" valign="top">

## 1 · Executive Summary

This proposal describes the redesign of a stereo pair of loudspeaker enclosures using donor acoustic components from the **Bose FreeSpace DS 100F** ceiling loudspeaker. The new enclosures are purpose-built for overhead mounting on the motorised monitor arm of a curved zero-gravity workstation.

**Core objectives:**

- Replace the current provisional white speakers with custom-designed stereo housings that integrate visually and mechanically with the workstation architecture
- Preserve the acoustic performance of the donor Bose system — internal volume, ported architecture, crossover behaviour, and baffle conditions
- Achieve significant weight reduction through vacuum-formed **HIPS** (High Impact Polystyrene) shells with targeted internal reinforcement
- Present eight design variants ranging from smooth biomorphic to structurally-integrated nacelle forms, all sharing a **rounded wedge profile** with a **kidney-shaped plan footprint**

**Key constraints:** ≤ 25 kg total arm payload (including three monitors), donor acoustic volume (TBD pending scan extraction), Formech 300XQ vacuum former forming envelope (430 × 280 mm).

</td>
<td width="45%" valign="top">

<!-- IMAGE: hero_workstation.png -->
![Workstation context — speakers mounted on monitor arm](images/hero_workstation.png)

*Concept rendering: custom speaker enclosures integrated into the curved monitor structure*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

## 2 · Background and Need

The workstation uses a multi-monitor overhead structure with pronounced curvature and limited spare load capacity on its motorised arm system. The currently mounted white speakers are functionally provisional and do not match the visual language, curvature, or packaging logic of the station.

**Four justifications for redesign:**

| Driver | Rationale |
|--------|-----------|
| **Aesthetic integration** | The current loudspeakers visually interrupt an otherwise cohesive, futuristic workstation form |
| **Geometric compatibility** | A custom kidney-shaped wedge can follow the monitor arc and reduce visual bulk |
| **Mass reduction** | The new housings must be lighter than the 5.9 kg donor enclosure — the arm has ≤ 25 kg total capacity including monitors |
| **Performance retention** | Tonal balance, dispersion, and output capability of the donor transducers and crossover must be preserved |

The Bose DS 100F is selected as the donor platform because it provides an exceptionally wide 160° conical coverage from a dual-driver array — ideal for near-field overhead listening in an unconventional mounting position where the operator's head position may shift.

</td>
<td width="45%" valign="top">

<!-- IMAGE: current workstation photo showing provisional speakers -->
![Current workstation with provisional speakers](images/current_workstation.png)

*Reference: current provisional white speakers on the monitor arm (to be replaced)*

</td>
</tr>
</table>

---

## 3 · Donor System Reference

### Bose FreeSpace DS 100F — Core Baseline
*See `docs/02_donor_ds100f` for complete, verified specifications.*

| Parameter | Value | Near-field relevance |
|-----------|-------|----------------------|
| **Low-frequency driver** | 5.25-inch (133 mm) woofer | Deep enough for near-field without a sub |
| **High-frequency driver** | 2.25-inch (57 mm) Twiddler® | Wide frequency band handler |
| **Frequency Response** | 75 Hz – 18 kHz (±3 dB) | Full voice and music coverage |
| **Enclosure Type** | Ported | Must extract port geometry from scans |
| **Nominal coverage** | 160° conical | **Critical advantage:** extreme off-axis tolerance |
| **Unit weight (complete)**| 5.9 kg | Substantially lighter than prior DM8C donor |

> [!TIP]
> **Key insight for this project:** The DS 100F's greatest asset for near-field overhead use is its **160° conical dispersion**. The operator is reclined and off-axis; the extreme dispersion means usable response even at large angles. Normal studio monitors offer only 60–90°, requiring strict mechanical aiming.

### Donor Internal Volume Calculation (TBD)
The exact internal acoustic core volume must be extracted from the 3D scans of the DS 100F backcan using CloudCompare (`ac_vol_target`). The gross external volume of the new enclosure will be larger once shell thickness, ribs, and mounting structure are added.

### Components to Transfer from Donor

| Component | Transfer | Notes |
|-----------|:--------:|-------|
| 5.25" woofer + 2.25" Twiddler | **Yes** | Core acoustic element — mounted on new baffle |
| Passive crossover PCB | **Yes** | Preserves factory voicing — mount with vibration isolation |
| 70/100 V transformer | **Remove** | Not needed for direct 8 Ω connection (weight TBD) |
| Bass reflex port geometry | **Yes** | Replicate exactly via dimension extraction (TBD) |
| Cast/plastic backcan | **Discard** | Replaced by custom HIPS shell |

---

<table>
<tr>
<td width="55%" valign="top">

## 4 · Design Language

### Form Vocabulary

The enclosure form language is driven by integration with the workstation's visual identity:

- **Rounded wedge profile** — deeper at the rear, tapering toward the listener
- **Kidney-shaped footprint** — asymmetric plan view following the monitor arc radius
- **Flowing surfaces** — continuous curvature with no sharp creases, compatible with vacuum forming draft requirements
- **Matte black HIPS** — non-reflective, tactile surface finish consistent with professional equipment
- **Subtle seam lines** — thermoforming split lines treated as deliberate trim details, not hidden joints
- **Integrated mount** — compact engineered bracket that reads as part of the enclosure, not an afterthought

</td>
<td width="45%" valign="top">

<!-- IMAGE: design language mood board or form studies -->
![Design language reference](images/design_language.png)

*Form vocabulary: rounded wedge × kidney footprint × monitor arc curvature*

</td>
</tr>
</table>

---

## 5 · Design Variants

Eight variants explore the design space from organic to structural within the shared form vocabulary. All variants share the same acoustic core, ported loading, passive crossover, and mounting interface.

### Overview of Concept Directions
1. **Variant A: Smooth Biomorphic Wedge** - Continuous curvature, minimal seam lines.
2. **Variant B: Technical Faceted Wedge** - Facets stiffen the shell geometrically.
3. **Variant C: Aggressive Aerodynamic Wedge** - Forward-leaning stance with ridge lines.
4. **Variant D: Arc-Matched Curvature** - Maximum architectural integration.
5. **Variant E: Manta Ray** - Ultra-flat, wide-span profile to minimize visual height.
6. **Variant F: Split Clamshell** - Prominent equator split becomes a deliberate design feature.
7. **Variant G: Cantilevered Blade** - Speaker thrusts forward from a structural rib.
8. **Variant H: Wraparound Nacelle** - Enclosure wraps the arm tube structurally.

> [!TIP]
> **Shortlist recommendation:** Variants **B** (faceted self-stiffening), **C** (best driver aim), and **F** (easiest to build and service) represent the strongest candidates for first CAD prototyping.

---

<table>
<tr>
<td width="55%" valign="top">

## 6 · Acoustic Strategy for Near-Field Overhead Use

The goal is to **preserve** the DS 100F's voicing while optimising the enclosure for overhead near-field listening at ≈0.8–1.5 m distance.

### Acoustic Path & Volume Preservation
The DS 100F is explicitly a **ported** enclosure. To ensure the best fidelity, the new enclosure must:
1. Hit the target internal volume (`ac_vol_target`) extracted from scans.
2. Meticulously replicate the original port geometry (inner diameter flare and length — TBD).
3. Ensure all shell joints are sealed (gaskets at split lines) to prevent air leaks that would detune the port.

### Driver Orientation — Near-Field Aim
The dual-driver array will be mounted on an angled internal baffle aimed downward-forward toward the operator's head position. Target aim angle: **15–25° below horizontal**, confirmed by CAD study. Thanks to the 160° coverage, precise aiming is less critical than with conventional monitors.

### Baffle Diffraction
The original circular grille provides consistent edge diffraction. The new kidney-shaped front aperture creates asymmetric diffraction. Mitigation includes rounded baffle edges (minimum 10 mm radius) and felt diffraction rings if required following acoustic testing.

</td>
<td width="45%" valign="top">

<!-- IMAGE: cross_section.png -->
![Internal cross-section](images/cross_section.png)

*Cross-section: driver array on angled baffle, matched port, crossover relocation*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

## 7 · Mounting and Integration

### Arm Load Budget

| Component | Est. Weight |
|-----------|:-:|
| Three monitors | ~15–18 kg |
| Monitor brackets & cabling | ~2 kg |
| **Budget remaining for speakers** | **~5–8 kg** |
| Target per speaker | **≤ 4.5 kg** |

The DS 100F complete donor weighs 5.9 kg. Removing the heavy backcan housing and the 70V transformer will drop this core weight significantly (exact savings TBD via teardown). The multi-layer HIPS shell and bracket will add 0.8–1.5 kg. The ≥ 4.5 kg target is comfortably achievable with this donor.

</td>
<td width="45%" valign="top">

<!-- IMAGE: mounting_detail.png -->
![Mounting bracket detail](images/mounting_detail.png)

*Mounting concept: clamp bracket with vibration isolation and adjustment*

</td>
</tr>
</table>

---

## 8 · Materials and Manufacturing

### Primary Material: HIPS (High Impact Polystyrene)
Target > 6 mm thickness (multi-layer laminate) to ensure acoustic rigidity. Internal bonded ribs will supplement shell stiffness to prevent oil-canning.

### Formech 300XQ Constraints
Max forming area: 430 × 280 mm. The shell must be produced as a **multi-part assembly** because the kidney footprint will exceed these limits.
- Upper shell (top + sides)
- Lower shell / baffle panel
- Internal structural baffle (CNC-cut MDF or PU)
- M5 threaded mounting inserts

### Assembly Sequence
1. Vacuum-form shells.
2. CNC-trim outline and apertures.
3. Bond stiffening ribs and mounting inserts.
4. Install baffle with driver array and ported tube.
5. Apply acoustic damping and join shells.

---

## 9 · Verification and Backlog
Please refer to `PROJECT_BACKLOG.md` for macro project phases and ownership.
Validation testing is defined in `docs/05_validation/VALIDATION_PLAN.md`.
All unknown physical dimensions required to commence CAD modeling are tracked in `docs/05_validation/ASSUMPTIONS_AND_TBD.md`.

---

*Document: PQ-SPEAKER-ENC-PROPOSAL-v3.0*
*Project: Phantom Quantum — Zero-Gravity Workstation Speaker Integration*
*Donor Baseline: Bose FreeSpace DS 100F*
