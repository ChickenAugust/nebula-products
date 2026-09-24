# Nebula Firmware

This layer handles microcontroller-level control, board bring-up, low-level diagnostics, and safety-critical housekeeping that should not depend on the full application operating system.

## Candidate stack

Zephyr is a candidate RTOS for the auxiliary-controller side because its current documentation covers board and SoC porting, device drivers, firmware management, DFU, and MCUboot integration.

Source: https://docs.zephyrproject.org/latest/

## Planned modules

- board initialization
- power controller interface
- battery and charger monitoring
- thermal monitoring
- GPIO / buttons
- sensor polling
- watchdog
- diagnostics
- firmware update hooks

Do not lock the implementation to a specific MCU until the hardware architecture selects the controller.
