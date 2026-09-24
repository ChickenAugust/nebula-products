# Nebula Hardware Specification

## Status

Draft v0.1 — architecture baseline.

## Product intent

Nebula is intended to become a custom computing device with its own board, enclosure, firmware, and software stack.

## Requirements

### Compute
- SoC: TBD
- RAM: TBD
- Storage: TBD

### Display
- Size: TBD
- Resolution: TBD
- Refresh rate: TBD
- Touch: Required

### Connectivity
- Wi-Fi: Required
- Bluetooth: Required
- Cellular: TBD
- GNSS: TBD
- NFC: TBD

### Power
- Battery capacity: TBD
- Charging: USB-C
- Battery protection: Required
- Fuel gauge: Required

### I/O
- USB-C: Required
- Audio: TBD
- Buttons: TBD
- Debug access: Required during development

### Security
- Verified boot: Required
- Device identity / secure key storage: Required

## Non-goals for v0.1

- Designing a smartphone-class processor from scratch
- Committing to a production enclosure before board dimensions are stable
- Choosing final RF bands before the target market is defined

## Change control

Changes to these requirements must be recorded in docs/DECISIONS.md.
