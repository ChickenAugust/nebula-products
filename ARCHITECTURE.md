# Nebula Software Architecture

## Layer 0 — Boot

Responsible for:
- hardware initialization
- trusted boot
- recovery entry
- boot target selection

## Layer 1 — Board support

Responsible for:
- clocks
- regulators
- GPIO
- buses
- storage
- display
- radio interfaces
- sensors

## Layer 2 — Operating system

The application processor should run a Linux-class operating system for the main user-facing environment when the final compute platform supports it.

## Layer 3 — Device services

- power management
- connectivity
- audio
- camera
- display
- input
- sensor fusion
- update service
- diagnostics

## Layer 4 — User experience

- system UI
- settings
- permissions
- notifications
- apps

## Layer 5 — Applications

Nebula applications are isolated from privileged system services and interact through documented APIs.

## Security model

- measured / verified boot where platform support exists
- least-privilege services
- signed software artifacts
- rollback-aware updates
- hardware-backed device identity where available
