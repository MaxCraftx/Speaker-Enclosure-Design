# Custom Lightweight Speaker Enclosures for Curved Zero-Gravity Workstation

**Redesign of Bose DesignMax DM8C donor acoustic components into futuristic, vacuum-formed workstation-integrated stereo housings**

---

<table>
<tr>
<td width="55%" valign="top">

## 1 · Executive Summary

This proposal describes the redesign of a stereo pair of loudspeaker enclosures using donor acoustic components from the **Bose DesignMax DM8C** ceiling loudspeaker. The new enclosures are purpose-built for overhead mounting on the motorised monitor arm of a curved zero-gravity workstation.

**Core objectives:**

- Replace the current provisional white speakers with custom-designed stereo housings that integrate visually and mechanically with the workstation architecture
- Preserve the acoustic performance of the donor Bose system — internal volume, driver orientation, crossover behaviour, and baffle conditions
- Achieve significant weight reduction through vacuum-formed **HIPS** (High Impact Polystyrene) shells with targeted internal reinforcement
- Present eight design variants ranging from smooth biomorphic to structurally-integrated nacelle forms, all sharing a **rounded wedge profile** with a **kidney-shaped plan footprint**

**Key constraints:** ≤ 25 kg total arm payload (including three monitors), donor acoustic volume ≥ 21.8 litres, Formech 300XQ vacuum former forming envelope (430 × 280 mm).

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
| **Mass reduction** | The new housings must be significantly lighter than the 9.6 kg donor enclosure — the arm has ≤ 25 kg total capacity including monitors |
| **Performance retention** | Tonal balance, dispersion, and output capability of the donor transducers and crossover must be preserved |

The Bose DM8C is selected as the donor platform because it provides a professional-grade coaxial point-source driver with wide dispersion from a single chassis — ideal for near-field overhead listening in an unconventional mounting position.

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

### Bose DesignMax DM8C — Full Specifications

#### Transducers

| Parameter | Value |
|-----------|-------|
| **Low-frequency driver** | 1 × 8-inch (203 mm) woofer |
| **High-frequency driver** | 1 × 1-inch (25.4 mm) coaxial centre-firing compression driver |
| **Crossover** | Passive 2-way, 1.5 kHz |
| **Nominal impedance** | 8 Ω (transformer bypass) |

#### Performance

| Parameter | AES test ⁽¹⁾ | Bose extended-lifecycle test ⁽²⁾ |
|-----------|:-:|:-:|
| **Frequency response (−3 dB)** | 60 – 20,000 Hz | 60 – 20,000 Hz |
| **Frequency range (−10 dB)** | 52 – 20,000 Hz | 52 – 20,000 Hz |
| **Sensitivity (1 W / 1 m)** | 91 dB | 91 dB |
| **Power handling, continuous** | 150 W | 125 W |
| **Power handling, peak** | 600 W | 500 W |
| **Max SPL @ 1 m** | 113 dB | 112 dB |
| **Max SPL @ 1 m, peak** | 119 dB | 118 dB |

*⁽¹⁾ AES standard: 2-hour duration, IEC system noise. ⁽²⁾ Bose: pink noise per IEC 268-5, 6 dB crest factor, 500-hour duration.*

#### Coverage

| Parameter | Value |
|-----------|-------|
| **Nominal coverage (1–4 kHz)** | 135° conical |
| **Nominal coverage (1–10 kHz)** | 120° conical |
| **Beamwidth measurement** | Whole-space conditions |

#### Protection and Processing

| Parameter | Value |
|-----------|-------|
| **Recommended high-pass** | 48 Hz, 24 dB/octave |
| **Overload protection** | Resistor-network power reduction with automatic reset |
| **EQ requirement** | Not required; Bose Professional EQ voicing and SmartBass optionally available |
| **Transformer taps (70 V)** | 2.5, 5, 10, 20, 40, 80 W + bypass |
| **Transformer taps (100 V)** | 5, 10, 20, 40, 80 W + bypass |

#### Physical

| Parameter | Value |
|-----------|-------|
| **Grille diameter** | 409 mm (16.1 in) |
| **Backcan diameter × depth** | 340 × 240 mm (13.4 × 9.5 in) |
| **Unit weight (complete)** | 9.6 kg |

---

### Near-Field Relevance Analysis

The DM8C is designed as a ceiling speaker for distributed commercial sound. This project repurposes it as an **overhead near-field monitor at ~0.8–1.5 m listening distance** in an unconventional reclined position. Not all specifications carry equal weight in this context:

| Spec | Near-field relevance | Notes |
|------|:--------------------:|-------|
| **135° conical coverage** | ★★★★★ | **Critical advantage.** The operator is reclined and off-axis; the extreme dispersion means usable response even at large angles. Most studio monitors offer only 60–90°. |
| **Frequency response 52–20 kHz** | ★★★★★ | Full-range capability. The 52 Hz −10 dB point is respectable for an 8-inch driver and eliminates the need for a separate subwoofer in most listening scenarios. |
| **Coaxial point-source** | ★★★★★ | At short listening distance, a coaxial driver provides coherent imaging without the comb-filtering that separate tweeter/woofer arrangements can exhibit off-axis. |
| **91 dB sensitivity** | ★★★☆☆ | At 1 m, 1 W produces 91 dB — far more than needed. Near-field listening at ~80 dB SPL requires < 0.1 W. Sensitivity is essentially irrelevant for this use case. |
| **150 W / 600 W power handling** | ★★☆☆☆ | Massively over-specified for near-field. A 20–50 W amplifier is more than sufficient. The headroom is a safety margin, not a requirement. |
| **113–119 dB max SPL** | ★☆☆☆☆ | Irrelevant. You will never approach these levels at 1 m distance in a workstation. |
| **Transformer taps (70/100 V)** | ☆☆☆☆☆ | Not used. Direct 8 Ω bypass connection to amplifier. The transformer adds weight that could potentially be removed. |
| **48 Hz high-pass recommendation** | ★★★★☆ | Should be implemented in the amplifier/DSP chain to protect the driver from subsonic excursion, especially since the new enclosure geometry differs from the original. |
| **Passive crossover** | ★★★★☆ | Preserves the DM8C's voicing without requiring an active crossover or DSP — simplifies the signal chain. |

> [!TIP]
> **Key insight for this project:** The DM8C's greatest asset for near-field overhead use is its **135° conical dispersion from a coaxial point source**. This is rare — it means the reclined operator will hear consistent frequency response even when significantly off-axis, which is exactly the condition created by overhead mounting.

---

### Donor Internal Volume Calculation

The acoustic core volume is derived from the cylindrical backcan geometry:

```text
V = π × r² × h
V = π × (170 mm)² × 240 mm
V = 21,796,458 mm³
V ≈ 21.8 litres ≈ 0.77 ft³
```

> [!IMPORTANT]
> The new enclosure must preserve a minimum internal acoustic volume of **21.8 litres**. The gross external volume will be larger once shell thickness (≥ 6 mm multi-layer HIPS), internal ribs, bosses, mounting structure, and stiffening features are added. The enclosure must therefore read as a **volumetrically substantial** body — not a compact satellite speaker.

### Components to Transfer from Donor

| Component | Transfer | Notes |
|-----------|:--------:|-------|
| 8" woofer + coaxial compression driver | **Yes** | Core acoustic element — mounted on angled internal baffle |
| Passive crossover PCB | **Yes** | Preserves factory voicing — mount with vibration isolation |
| Wiring harness & terminal cup | **Yes** | Relocate to suit new shell geometry |
| Overload protection circuit | **Yes** | Resistor-network auto-reset — integral to crossover PCB |
| 70/100 V transformer | **Remove** | Not needed for direct 8 Ω amplifier connection — saves ~0.5–1.0 kg |
| Original grille frame | **Evaluate** | May need adaptation or replacement with custom perforated panel |
| Cast aluminium backcan | **Discard** | Replaced by HIPS shell — saves ~5–6 kg |

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

### Design Character

The overall character must be:

| ✓ Should read as | ✗ Must not read as |
|---|---|
| Professional studio monitor | Consumer gaming peripheral |
| Precision aerospace component | Toy or 3D-print experiment |
| Purpose-built workstation hardware | Generic off-the-shelf box |
| Futuristic but credible | Concept-only or impractical |

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

Eight variants explore the design space from organic to structural within the shared form vocabulary. All variants share the same acoustic core (≥ 21.8 L), driver orientation, passive crossover, and mounting interface. The variants are grouped into three families:

- **Form-driven** (A, B, C, D) — shape defined primarily by visual character
- **Profile-driven** (E, F) — shape defined by silhouette or manufacturing logic
- **Integration-driven** (G, H) — shape defined by relationship to the arm structure

---

<table>
<tr>
<td width="55%" valign="top">

### Variant A · Smooth Biomorphic Wedge

**Character:** Organic, sculptural, flowing — the most refined and minimal variant.

Surfaces flow continuously like a polished river stone. No visible panel breaks or hard edges. The form is entirely resolved through curvature, with the thermoforming split line placed along the natural equator of the body. The elongated wedge tapers from a deep rear section to a thin leading edge.

**Strengths:**
- Most visually refined and premium appearance
- Simplest tool geometry for vacuum forming — no undercuts
- Minimal trim work required

**Considerations:**
- Large smooth surfaces may require internal ribbing to prevent oil-canning
- Less visual articulation may make the speaker read as smaller than it is

**Best suited for:** workstation builds prioritising calm, gallery-like aesthetics.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_a_biomorphic.png -->
![Variant A — Smooth Biomorphic Wedge](images/variant_a_biomorphic.png)

*Variant A: Flowing organic surfaces, minimal seam lines, sculptural presence*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant B · Technical Faceted Wedge

**Character:** Precision-engineered, architectural — the most technically detailed variant.

The same elongated wedge silhouette as Variant A, but with the surface broken into subtle flat facets separated by crisp-but-soft edges. The faceting creates visual interest and a sense of engineered precision — reminiscent of stealth aircraft or modern architectural panels.

**Strengths:**
- Facets stiffen the shell geometrically, reducing need for internal ribs
- More defined visual scale — faceted panels make the enclosure read as larger and more detailed
- Trim/seam lines can follow facet edges naturally

**Considerations:**
- More complex mould geometry — each facet needs accurate flat-to-flat transitions
- Slightly higher forming pressure required for crisp edges in HIPS
- Sheet thickness variation at facet transitions needs managing

**Best suited for:** workstation builds with a technical, precision-engineering identity.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_b_technical.png -->
![Variant B — Technical Faceted Wedge](images/variant_b_technical.png)

*Variant B: Subtle faceting creates engineered precision and geometric stiffness*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant C · Aggressive Aerodynamic Wedge

**Character:** Dynamic, forward-leaning, performance-oriented — the most dramatic variant.

A pronounced forward-leaning stance angles the front baffle aggressively toward the listening position. Ridge lines flow from the rear mounting face to the leading edge like intake ducts. The form implies motion and purpose — closer to a jet nacelle or racing helmet than a traditional speaker.

**Strengths:**
- Most dramatic visual presence of the form-driven family
- Forward lean naturally angles the driver toward the reclined operator — maximises on-axis benefit of the 135° coverage
- Ridge lines act as structural stiffeners along the shell

**Considerations:**
- Deeper draw ratio at the rear may challenge vacuum forming — may require plug assist
- The aggressive stance may visually dominate the monitor array
- Mounting bracket must account for the shifted centre of gravity

**Best suited for:** workstation builds with a bold, performance-driven character.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_c_aerodynamic.png -->
![Variant C — Aggressive Aerodynamic Wedge](images/variant_c_aerodynamic.png)

*Variant C: Forward-leaning stance, ridge-line stiffeners, dramatic presence*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant D · Arc-Matched Curvature

**Character:** Architecturally integrated, invisible-by-design — the most workstation-native of the form-driven variants.

The outer shell curvature precisely echoes the radius of the monitor array. The speaker looks as if it was born from the same CAD model as the monitor arm structure — sharing radii, visual rhythm, and surface language.

**Strengths:**
- Maximum visual integration — speakers virtually disappear into the workstation form
- Shared curvature language creates a unified product identity
- Top and side surfaces can reference monitor bezel geometry

**Considerations:**
- Arc-matching requires accurate measurement of the actual monitor arm curvature (3D scan recommended)
- Form is specific to this workstation — least transferable to other mounting contexts
- Curved grille panel may be more complex to fabricate

**Best suited for:** builds where the speaker should look like an integral part of the workstation architecture.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_d_arcmatched.png -->
![Variant D — Arc-Matched Curvature](images/variant_d_arcmatched.png)

*Variant D: Curvature mirrors the monitor arc — maximum architectural integration*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant E · Manta Ray

**Character:** Ultra-low-profile, wide-span, biologically inspired — the most visually lightweight variant.

An extremely elongated, flat wedge inspired by the silhouette of a manta ray. The body is dramatically wider than it is tall, with sweeping wing-like side surfaces that taper to thin trailing edges. From the operator's perspective below, the speaker presents minimal visual mass — its bulk is spread laterally rather than protruding downward.

**Strengths:**
- Lowest apparent visual bulk from the operator's viewpoint
- Wide horizontal span reads as architectural, not equipment
- Excellent aerodynamic character — cohesive with futuristic workstation identity
- Lateral spread distributes stiffness naturally

**Considerations:**
- Wide footprint may conflict with adjacent monitors or camera sightlines
- Shallow depth increases forming challenge — may require plug assist for the deep centre section
- Driver cone depth may dictate a minimum local bulge that disrupts the flat profile

**Best suited for:** builds prioritising visual stealth and minimal overhead intrusion.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_e_mantaray.png -->
![Variant E — Manta Ray](images/variant_e_mantaray.png)

*Variant E: Ultra-flat, wide-span profile — minimal visual weight from below*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant F · Split Clamshell

**Character:** Manufacturing-honest, refined industrial — celebrates the vacuum-forming process.

A rounded wedge form that is clearly and deliberately split into two halves along a prominent horizontal equator line. Rather than hiding the thermoforming split, Variant F turns it into a **design feature** — like a high-end automotive body line or the seam on a premium headphone ear cup. A subtle accent strip (dark grey or anodised aluminium) runs along the split.

**Strengths:**
- Most manufacturing-honest design — the split is the design
- Easiest assembly and serviceability — the two halves separate for driver access
- The accent strip provides a natural location for status LEDs, branding, or a grip surface
- Both halves form with consistent draw depth

**Considerations:**
- The visible split must be executed with precision — any waviness or mismatch will read as a defect
- Accent strip adds a secondary material and fastening requirement
- Acoustic sealing at the split is critical — gasket + solvent bond required

**Best suited for:** builds favouring industrial-design honesty and easy serviceability.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_f_clamshell.png -->
![Variant F — Split Clamshell](images/variant_f_clamshell.png)

*Variant F: Prominent equator split becomes a deliberate design feature*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant G · Cantilevered Blade

**Character:** Dramatic, gravity-defying, structural — the most architecturally expressive variant.

The speaker body cantilevers forward from a compact rear mounting hub like a diving board or aircraft wing. The rear section is minimal and structural where it meets the arm bracket, then the body sweeps forward and expands into the full acoustic volume housing the 8-inch driver. A visible structural rib on the underside telegraphs the engineering intent.

**Strengths:**
- Creates a dramatic sense of suspension and weightlessness — aligned with the zero-gravity workstation concept
- The cantilever naturally directs the front baffle downward toward the operator
- Compact rear hub simplifies the mounting bracket
- Structural rib acts as a stiffener and visual feature simultaneously

**Considerations:**
- Cantilevered mass creates a bending moment on the arm bracket — requires careful structural analysis
- The expanding front may challenge forming — deep draw at the leading edge
- Perceived precariousness may be visually unsettling for some users

**Best suited for:** builds where the workstation is a statement piece and the speakers should amplify that drama.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_g_cantilevered.png -->
![Variant G — Cantilevered Blade](images/variant_g_cantilevered.png)

*Variant G: Forward-cantilevered body with structural underside rib*

</td>
</tr>
</table>

---

<table>
<tr>
<td width="55%" valign="top">

### Variant H · Wraparound Nacelle

**Character:** Structurally integrated, engine-pod-like — the speaker becomes part of the arm.

The enclosure wraps partially around the monitor arm tube like an engine nacelle on a wing pylon. The arm tube passes through or alongside the speaker body, making the speaker look **structurally integral with the arm** rather than hung from it. The 8-inch driver fires downward-forward from the underside of the nacelle form.

**Strengths:**
- Maximum structural integration — the speaker IS the arm in that zone
- No visible bracket — the arm is the bracket
- Distributes load along the arm tube rather than concentrating at a single clamp point
- Most mechanically robust mounting approach

**Considerations:**
- Requires the arm tube to pass through the enclosure — may need the arm to be partially disassembled for installation
- Shell geometry is arm-diameter-specific — no transferability
- Complex multi-part shell strategy needed to wrap around the tube
- Acoustic volume may be compromised by the tube pass-through

**Best suited for:** builds where the speaker should read as an organic extension of the arm structure itself.

</td>
<td width="45%" valign="top">

<!-- IMAGE: variant_h_wraparound.png -->
![Variant H — Wraparound Nacelle](images/variant_h_wraparound.png)

*Variant H: Enclosure wraps the arm tube — speaker becomes structural arm element*

</td>
</tr>
</table>

---

### Variant Comparison Matrix

| Attribute | A | B | C | D | E | F | G | H |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| | *Biomorphic* | *Technical* | *Aerodynamic* | *Arc-Matched* | *Manta Ray* | *Clamshell* | *Cantilever* | *Nacelle* |
| Visual integration | ★★★☆ | ★★★☆ | ★★☆☆ | ★★★★ | ★★★☆ | ★★★☆ | ★★☆☆ | ★★★★ |
| Mouldability | ★★★★ | ★★★☆ | ★★☆☆ | ★★★☆ | ★★☆☆ | ★★★★ | ★★☆☆ | ★☆☆☆ |
| Shell stiffness (geometric) | ★★☆☆ | ★★★★ | ★★★☆ | ★★★☆ | ★★★☆ | ★★★☆ | ★★★★ | ★★★☆ |
| Visual presence / drama | ★★☆☆ | ★★★☆ | ★★★★ | ★★☆☆ | ★★★☆ | ★★★☆ | ★★★★ | ★★★☆ |
| Driver aim at operator | ★★★☆ | ★★★☆ | ★★★★ | ★★★☆ | ★★★☆ | ★★★☆ | ★★★★ | ★★★★ |
| Transferability | ★★★★ | ★★★★ | ★★★☆ | ★★☆☆ | ★★★☆ | ★★★★ | ★★★☆ | ★☆☆☆ |
| Near-field advantage | ★★★☆ | ★★★☆ | ★★★★ | ★★★☆ | ★★★★ | ★★★☆ | ★★★★ | ★★★★ |
| Serviceability | ★★★☆ | ★★★☆ | ★★☆☆ | ★★★☆ | ★★☆☆ | ★★★★ | ★★☆☆ | ★☆☆☆ |
| Mould complexity | Low | Med | High | Med | High | Low | High | Very High |

> [!TIP]
> **Shortlist recommendation:** Variants **B** (faceted self-stiffening, good mouldability), **C** (best driver aim for reclined operator), and **F** (easiest to build and service) represent the strongest candidates for first prototyping. Variant **H** is the most architecturally compelling but the most complex to manufacture.

---

<table>
<tr>
<td width="55%" valign="top">

## 6 · Acoustic Strategy for Near-Field Overhead Use

The goal is not to improve the Bose DM8C acoustics — it is to **preserve** the donor's voicing while **optimising the enclosure for overhead near-field listening** at approximately 0.8–1.5 m distance to a reclined operator.

### Volume Preservation

| Parameter | Donor (Original) | New Enclosure Target |
|-----------|:-:|:-:|
| Internal acoustic volume | 21.8 L (0.77 ft³) | ≥ 21.8 L |
| Gross external volume | ~24 L (estimated) | ~28–32 L (thicker shell + ribs) |

The new enclosure's external body will be **significantly larger** than 21.8 litres to account for:
- ≥ 6 mm multi-layer HIPS shell wall thickness (substantially more volume displacement than thin-wall construction)
- Internal bracing ribs (~5% volume displacement)
- Mounting bosses and inserts
- Crossover board clearance
- Port / vent geometry (see Acoustic Path below)

### Driver Orientation — Near-Field Aim

The coaxial driver will be mounted on an **angled internal baffle** aimed downward-forward toward the operator's head position. At ~1 m distance, the 135° conical coverage means the −6 dB point is at ±67.5° off-axis — so even with imperfect aiming, the operator will be well within the usable coverage zone.

Target aim angle: **15–25° below horizontal**, confirmed by 3D-scan geometry study of the operator head position relative to the arm mounting zone.

> [!NOTE]
> Because the DM8C coverage is 135° conical (vs. 60–90° for typical studio monitors), precise aim is **less critical** than with conventional near-field speakers. This is a significant practical advantage for an overhead mounting where the operator's head position varies with recline angle.

### Near-Field Power and SPL

At ~1 m listening distance:

| Listening level | Power required | Notes |
|:---:|:---:|-------|
| 75 dB SPL (relaxed) | ~0.03 W | Background / ambient listening |
| 85 dB SPL (moderate) | ~0.3 W | Normal music / media |
| 95 dB SPL (loud) | ~3 W | Peak transients, film |
| 105 dB SPL (very loud) | ~30 W | Sustained loud listening (rare) |

A **20–50 W amplifier** provides ample headroom. The DM8C's 150 W continuous rating means the driver will operate at a tiny fraction of its thermal capacity, ensuring negligible power compression and long driver life.

### Acoustic Path

The original DM8C backcan includes a **port** — the enclosure is **not sealed**. The exact acoustic loading type (bass-reflex, transmission line, or tuned vent) must be confirmed during the 3D-scan disassembly phase by measuring the port dimensions, position, and any internal ducting.

**Selected Strategy: Replicate the original port**

To ensure the best fidelity to the donor's voicing and preserve the critical 52–60 Hz low-frequency extension, the new enclosure will meticulously replicate the original port geometry. During the 3D-scan and disassembly phase, the port's exact diameter, length, and spatial relationship to the driver will be measured and transferred identically into the new CAD model.

Additional acoustic path requirements:
- All shell joints must be **well-sealed** — gaskets at split lines, sealed threaded inserts — to prevent air leaks that would detune the port
- The port opening must be kept clear of obstructions and positioned to avoid boundary interference from the arm structure
- Recommended **48 Hz high-pass filter** (24 dB/octave) should be applied in the amplifier or DSP chain to protect against subsonic excursion

### Baffle Diffraction

The original circular grille (409 mm Ø) on the DM8C provides consistent edge diffraction from a symmetrical boundary. The new kidney-shaped front aperture will create **asymmetric diffraction** — different path-length differences from the driver cone to each edge of the baffle. At near-field distances this effect is reduced but not eliminated.

Mitigation options:
- Felt or foam diffraction ring around the driver cone
- Rounded baffle edges (minimum 10 mm radius)
- Computational baffle-step simulation in the CAD phase
- *Near-field advantage:* at 0.8–1.5 m, the direct-to-reflected ratio is high, reducing the audibility of diffraction artifacts compared to far-field commercial installations

### Damping

Internal acoustic damping material (polyester fill or open-cell foam) will line the inner walls, replicating the donor enclosure's damping behaviour.

### Transformer Removal Note

The DM8C includes 70 V / 100 V transformer taps for distributed commercial audio systems. For direct 8 Ω amplifier connection, the transformer is bypassed and can be **physically removed** to save approximately 0.5–1.0 kg. The passive crossover and overload protection circuit must be retained.

</td>
<td width="45%" valign="top">

<!-- IMAGE: cross_section.png -->
![Internal cross-section](images/cross_section.png)

*Cross-section: driver on angled baffle, crossover on rear wall, bracing ribs, acoustic damping*

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
| Target per speaker (enclosure + driver + bracket) | **≤ 4.0 kg** |

The donor driver assembly, crossover, and grille weigh approximately **3.0–3.5 kg** (the remaining ~6 kg of the original 9.6 kg DM8C is the cast aluminium backcan and transformer). The multi-layer HIPS shell (≥ 6 mm) and bracket will be heavier than a thin-wall single-layer shell — estimated **0.8–1.5 kg** — bringing total per-speaker weight to approximately **3.8–5.0 kg**. This is still well within the arm's remaining payload budget.

### Mounting Concept

The mounting bracket is an integral part of the enclosure design, not a separate accessory:

- **Material:** Anodised aluminium or glass-filled nylon (3D printed prototype, CNC final)
- **Interface:** Clamp-on to the existing arm tube or rail, with M5/M6 threaded fixings
- **Adjustment:** ±10° tilt and ±15° yaw for fine-aiming at the operator
- **Isolation:** Rubber or silicone grommets between bracket and shell to decouple vibration
- **Safety:** Positive mechanical retention — no friction-only clamps — plus a secondary safety lanyard

### Cable Management

Speaker cables will route through the arm tube or along the arm surface in adhesive cable channels, entering the speaker shell through a gasketed rear port with strain relief.

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

| Property | Value |
|----------|-------|
| Density | 1.04 g/cm³ |
| Tensile strength | 20–40 MPa |
| Impact resistance | Good (rubber-modified) |
| Thermoforming suitability | Excellent |
| Sheet thickness (target) | ≥ 6 mm (multi-layer laminated shell) |
| Finish | Matte black (pigmented in-mass or spray-finished) |
| Acoustic damping | Moderate — requires internal treatment |
| Cost | Low |

> [!NOTE]
> A single 3–4 mm HIPS pull will be too flexible for an enclosure of this size. The target is a **multi-layer laminated shell** — either vacuum-forming two 3 mm sheets and bonding them into a 6 mm+ composite, or forming a single 6 mm sheet on the Formech 300XQ (which can handle up to 6 mm stock). Internal bracing ribs supplement shell stiffness regardless of wall thickness.

### Formech 300XQ Constraints

| Parameter | Limit |
|-----------|-------|
| Max sheet size | 450 × 300 mm |
| Max forming area | 430 × 280 mm |
| Reduced forming area (optional plate) | 254 × 228 mm |
| Max sheet thickness | 6 mm |
| Material compatibility | Thermoplastic sheet only |

### Shell Strategy

Given that the enclosure's kidney footprint will exceed the 430 × 280 mm forming envelope in at least one axis, the shell will be produced as a **multi-part assembly**:

| Part | Forming | Notes |
|------|---------|-------|
| Upper shell (top + sides) | Vacuum formed, single pull | Primary visual surface |
| Lower shell / baffle panel | Vacuum formed or flat-formed + CNC trimmed | Driver aperture cut post-forming |
| Internal baffle | CNC-cut MDF or cast rigid polyurethane | Structural + acoustic — bonds to shell halves |
| Stiffening ribs | Bonded-in HIPS or polyurethane strips | Prevent oil-canning on large flat areas |
| Mounting boss plates | Aluminium or nylon inserts | Threaded M5 inserts bonded into shell |

### Split Line Strategy

The split between upper and lower shells should be placed at the **widest perimeter** of the enclosure (the "equator") where:
- It naturally reads as a designed trim line
- It provides full mould release with ≥ 3° draft angle on all surfaces
- It allows access for driver installation and wiring

### Shell Stiffening

To prevent resonance and flex without adding excessive mass:
- **Geometric stiffening** — facets (Variant B) or ridge lines (Variant C) add stiffness at zero weight cost
- **Bonded ribs** — 10–15 mm deep HIPS or PU strips bonded to the inner surface at 80–100 mm spacing
- **Internal baffle** — the driver mounting baffle acts as a structural diaphragm tying the shells together
- **Perimeter flange** — the split-line flange provides edge stiffness and bonding area

### Assembly Sequence

1. Vacuum-form upper and lower shells
2. CNC-trim to final outline and cut apertures
3. Bond stiffening ribs to inner surfaces
4. Install threaded inserts and mounting bosses
5. Mount internal baffle with driver and crossover
6. Apply acoustic damping material
7. Join upper and lower shells — solvent-bond + mechanical fasteners
8. Install grille panel and cable entry
9. Attach mounting bracket

---

## 9 · Design Risks and Mitigations

| Risk | Severity | Mitigation |
|------|:--------:|------------|
| Enclosure too large for single-pull vacuum forming | High | Multi-part shell strategy already planned |
| HIPS shell resonance (oil-canning) | Medium | Internal ribs + faceted geometry + bonded baffle |
| Acoustic volume shortfall from ribs/structure | Medium | Target 10% volume margin over 21.8 L minimum |
| Driver aim misaligned to operator | Medium | Adjustable bracket + 3D-scan driver aim study |
| Split-line air leaks | Medium | Solvent bond + gasket at split + test with smoke |
| Arm overweight | High | Strict weight budget ≤ 4.5 kg/speaker — weigh-check at every prototype stage |
| Baffle diffraction artifacts | Low | Rounded baffle edges + felt diffraction ring |
| HIPS UV yellowing (unlikely indoors) | Low | Pigmented-in-mass black + optional clear coat |

---

## 10 · Verification and Qualification Plan

### 3D Scanning Phase

Before CAD modelling:
1. **3D-scan the donor DM8C backcan** — establish precise internal volume and driver mounting geometry
2. **3D-scan the monitor arm mounting zone** — capture arm tube diameter, available clearance, and curvature radius

### CAD Phase

- Model enclosure in **Siemens NX** or equivalent
- Verify internal volume ≥ 21.8 L using CAD volume analysis
- Check forming draft angles ≥ 3° on all surfaces
- Confirm shell fits within 430 × 280 mm forming envelope (per part)

### FEA Phase

- **Structural FEA** — modal analysis of shell to identify resonant frequencies and ensure they fall outside the 60 Hz–20 kHz passband, or are adequately damped
- **Acoustic FEA** *(optional)* — baffle diffraction simulation to validate front-face geometry

### Prototype Phase

1. MDF or foam plug mould for first vacuum-form trial
2. Fit-check with donor driver assembly
3. Weigh-check against 4.5 kg target
4. Listening test — A/B comparison with original DM8C enclosure
5. Vibration test — check for shell buzz or rattle under full-power bass signal

---

## 11 · Collaboration Inputs Sought

The following areas would benefit from external review or specialist input during the CAD and tooling phases:

| Topic | Input Needed |
|-------|-------------|
| **Vacuum forming feasibility** | Review of geometry for draft, draw ratio, and release |
| **Split line / trim line definition** | Optimal parting plane for multi-part shells |
| **Plug vs. cavity mould** | Selection of mould type for the Formech 300XQ |
| **Sheet draw & thickness variation** | Allowances for thinning at deep draws and corners |
| **Stiffening strategy** | Internal rib pattern vs. geometric stiffening trade-offs |
| **Threaded insert method** | Best practice for bonding metal inserts into HIPS |
| **Tooling material** | MDF plug vs. CNC tooling board vs. 3D-printed tool |
| **Repeatable L/R production** | Strategy for consistent left-hand and right-hand shells |

---

## 12 · Next Steps

| Phase | Description | Dependencies |
|-------|-------------|:------------:|
| **1 · Variant selection** | Review concept renders, select preferred variant or hybrid | This document |
| **2 · 3D scanning** | Scan donor DM8C backcan and monitor arm mounting zone | Donor unit access |
| **3 · CAD modelling** | Develop enclosure in Siemens NX with internal fitment | Scan data |
| **4 · FEA validation** | Structural modal + optional acoustic diffraction analysis | CAD model |
| **5 · Mould design** | Plug mould geometry for Formech 300XQ | Forming feasibility review |
| **6 · Prototype** | First vacuum-form pull, fit-check, weight-check | Mould |
| **7 · Acoustic test** | A/B listening comparison vs. original DM8C | Prototype + donor drivers |
| **8 · Production pair** | Final shells, finishing, assembly, installation | Validated prototype |

---

> [!NOTE]
> This is a **Phase 1 design proposal**. All concept images are directional renderings — final geometry will be developed in CAD following 3D scanning of the donor components and mounting zone.

---

*Document: PQ-SPEAKER-ENC-PROPOSAL-v2.0*
*Date: 2026-03-12*
*Project: Phantom Quantum — Zero-Gravity Workstation Speaker Integration*
