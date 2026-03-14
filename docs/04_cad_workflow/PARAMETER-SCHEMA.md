# Fusion 360 User Parameter Schema

To maintain parametric stability across the master assembly, avoid "magic numbers" in sketches. All critical dimensions must be driven by User Parameters.

## Naming Convention
- Use `snake_case` for all parameter names.
- Group parameters logically by prefix.

## Required Parameters

### Acoustic Variables
| Parameter | Description | Initial Value | Notes |
|-----------|-------------|---------------|-------|
| `ac_vol_target` | Target internal acoustic volume | TBD mm³ | Sourced from CloudCompare extraction |
| `ac_vol_actual` | Measured volume of the cavity body | (Driven) | Check against target |
| `ac_port_id` | Inner diameter of reflex vent | TBD mm | |
| `ac_port_len` | Length of reflex vent centerline | TBD mm | |

### Structural / Shell Variables
| Parameter | Description | Initial Value | Notes |
|-----------|-------------|---------------|-------|
| `sh_wall_thk` | Nominal shell wall thickness | 6.0 mm | Sourced from HIPS forming constraint |
| `sh_rib_thk` | Thickness of internal stiffening ribs | 4.0 mm | |
| `sh_rib_spacing` | Nominal pitch between ribs | 100.0 mm | |
| `sh_draft_ang` | Minimum draft angle for vacuum forming | 3 deg | Critical for mould release |

### Mounting Variables
| Parameter | Description | Initial Value | Notes |
|-----------|-------------|---------------|-------|
| `mt_arm_dia` | Workstation monitor arm OD | TBD mm | Scan extraction required |
| `mt_bolt_dia` | Fastener clearance diameter | 5.5 mm | M5 clearance |
| `mt_boss_dia` | Boss outer diameter | 12.0 mm | |
