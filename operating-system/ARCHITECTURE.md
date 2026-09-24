# Nebula OS Architecture

## Boot

Firmware / bootloader -> trusted kernel / OS image -> system services -> user session.

## Kernel boundary

Only low-level platform and driver responsibilities should sit in the kernel.

## Userspace

System services provide hardware-neutral APIs to applications.

## Recovery

A dedicated recovery environment must remain available even when the normal userspace is broken.

## Logging

Logs use structured records with:
- timestamp
- component
- severity
- hardware revision
- software version
- event identifier
