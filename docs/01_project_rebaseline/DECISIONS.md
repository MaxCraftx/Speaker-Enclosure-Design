# Architectural Decision Records (ADRs)

## ADR-001: Donor Platform Rebaseline

**Date:** 2026-03-14  
**Status:** Accepted

**Context:** The initial proposal utilized the Bose DM8C. A more appropriate, compact, and available donor unit, the Bose FreeSpace DS 100F, was secured.

**Decision:** The repository is fully rebaselined to target the DS 100F. All prior DM8C specifications are discarded.

**Consequences:** 
- New baseline specifications (5.25" woofer + 2.25" Twiddler, ported, 5.9 kg total).
- Scans of the DS 100F subassemblies become the geometric ground truth.
- Port measurement and extraction is mandatory.

---

## ADR-002: Fusion 360 CAD Workflow

**Date:** 2026-03-14  
**Status:** Accepted

**Context:** The initial conceptual proposal referenced Siemens NX. The active engineering environment is now Fusion 360 with the Design Extension.

**Decision:** Fusion 360 is the authoritative CAD platform for reverse engineering and mechanical design.

**Consequences:**
- Workflows must rely on Mesh Section Sketch tracing rather than generic organic conversion.
- Fusion file naming conventions and parameter schemas are enforced.

---

## ADR-003: Strict Scan-Driven Geometry

**Date:** 2026-03-14  
**Status:** Accepted

**Context:** Prior iterations guessed at internal dimensions. Because we now have sub-millimeter Creality CR-Scan Raptor point clouds, guessing is unacceptable.

**Decision:** No geometric or acoustic dimension (volume, port length, boss location) is allowed into the CAD master model unless it is traceable to either the Bose datasheet or a direct extraction from the scan data.

**Consequences:**
- Any missing value is marked TBD and tracked via a Measurement Task GitHub Issue.
- The `GEOMETRY-REGISTER.md` and `ACOUSTIC-REGISTER.md` track the verification status of all parameters.
