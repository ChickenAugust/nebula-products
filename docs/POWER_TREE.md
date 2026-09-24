# Nebula Power Tree

Preliminary power architecture.

## Inputs

- USB-C external power
- Rechargeable battery

## Functional blocks

USB-C -> input protection -> charging / power-path management -> system battery rail

Battery rail -> PMIC / regulators -> individual system rails

## Rail categories

- Always-on / housekeeping
- Application processor
- Memory
- Storage
- Display
- Camera
- Radio
- Audio
- Sensors
- USB / external I/O

Exact voltages, current limits, sequencing, and regulator part numbers remain TBD until the compute platform is selected.
