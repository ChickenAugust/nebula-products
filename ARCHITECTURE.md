# Nebula Overall Architecture

Nebula is organized as four major layers:

1. Mechanical and electrical hardware
2. Boot and firmware
3. Operating system and device services
4. User applications

The branch boundaries map to ownership, not to physical separation in the final product.

## Hardware/software contract

Hardware defines:
- electrical interfaces
- power states
- interrupts
- storage
- display and camera links
- radio interfaces
- board revision identity

Software defines:
- initialization order
- drivers
- device services
- update/recovery behavior
- user-facing APIs

Cross-layer decisions belong in documented architecture records.
