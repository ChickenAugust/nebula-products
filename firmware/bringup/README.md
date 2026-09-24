# Firmware Bring-Up

Bring-up order:

1. CPU / MCU clock
2. UART debug output
3. GPIO
4. watchdog
5. power / battery telemetry
6. I2C / SPI
7. display or indicator
8. sensors
9. external communications
10. update path

Every step should produce a reproducible test result tied to the hardware revision.
