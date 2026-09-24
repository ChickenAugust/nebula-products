# Nebula Hardware Architecture

Nebula is a modular custom-board platform. The first hardware revision is intentionally built from commercially available ICs rather than custom silicon.

## Top-level domains

- Compute
- Memory and storage
- Power / battery / charging
- Display and touch
- Connectivity / RF
- Cameras
- Audio
- Sensors
- Security
- USB-C / external I/O
- Thermal / mechanical

## Architecture rules

1. Requirements are defined before final schematic capture.
2. Power sequencing and voltage domains are documented before layout.
3. High-speed interfaces use controlled-impedance routing where required.
4. RF paths are isolated from noisy digital and switching-power regions.
5. Every board revision has a unique hardware revision identifier.
6. Every production candidate has a manufacturing BOM and validation record.

## Candidate compute direction

The current research baseline includes NXP i.MX 8M Plus as a development candidate. NXP documents quad Cortex-A53 variants, Cortex-M7 real-time control, LPDDR4/DDR4 interfaces, dual ISP/camera inputs, multimedia acceleration, and extensive design resources. This is a development-class candidate, not a final product decision.

See docs/COMPONENT_RESEARCH.md for the research record.

## Validation stages

- EVT — electrical bring-up and first working board
- DVT — system, thermal, RF, mechanical, and reliability validation
- PVT — manufacturing validation and production readiness
