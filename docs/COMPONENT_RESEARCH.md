# Nebula Component Research

This is the current public-source research record. It is not a final bill of materials.

## NXP i.MX 8M Plus

NXP describes the i.MX 8M Plus family as an Arm Cortex-A53 / Cortex-M7 applications-processor platform with up to 2.3 TOPS NPU capability, dual ISP/camera inputs, multimedia acceleration, and LPDDR4/DDR4 support. NXP also provides consumer and industrial variants plus reference material and evaluation boards.

Why it is relevant:
- Provides a realistic custom-board compute target.
- Includes application-class processors and real-time control in one package.
- Has documented design resources.

Caution:
- It is not a smartphone SoC with an integrated cellular modem.
- A phone-like Nebula would still need external connectivity, power, display, storage, and RF architecture.

Source:
https://www.nxp.com/products/i.MX8MPLUS

## Zephyr

Zephyr is an open-source RTOS with hardware support, board and SoC porting guides, a device-driver model, and device-management/DFU capabilities. Its current documentation lists Zephyr 4.4.0 as the latest stable release.

Why it is relevant:
- Strong option for the low-level controller / auxiliary MCU side of Nebula.
- Supports board bring-up, device drivers, and secure firmware update workflows.

Sources:
https://docs.zephyrproject.org/latest/
https://docs.zephyrproject.org/latest/hardware/firmware/index.html
https://docs.zephyrproject.org/latest/services/device_mgmt/dfu.html
https://docs.zephyrproject.org/latest/releases/index.html

## Selection rule

Do not select the final compute platform solely from this document. The final choice must be checked against Nebula performance, physical, power, software, supply-chain, and manufacturing requirements.
