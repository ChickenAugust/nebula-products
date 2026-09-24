# Nebula Component Research

This is the current public-source research record. It is not a final bill of materials.

## Candidate A — NXP i.MX 8M Plus

NXP documents quad Cortex-A53 variants, a Cortex-M7, LPDDR4/DDR4 interfaces, dual ISP/camera inputs, multimedia acceleration, and NPU capability. It is a realistic custom-board development target, but cellular connectivity would be external.

Source: https://www.nxp.com/products/i.MX8MPLUS

## Candidate B — NXP i.MX 95

NXP positions i.MX 95 as a higher-performance applications processor family for edge platforms, with advanced security features and a hardware secure enclave. It is a more ambitious board target and would need a careful power, thermal, software, and cost review.

Source: https://www.nxp.com/products/i.MX95

## Candidate C — Raspberry Pi Compute Module 5

Raspberry Pi documents Compute Module 5 as a 55 mm × 40 mm system-on-module with a 64-bit quad-core Arm Cortex-A76 SoC, configurable RAM/storage, optional Wi-Fi/Bluetooth, PCIe, USB, MIPI DSI/CSI, and extensive electrical/mechanical design documentation. It can be useful for a first prototype because Nebula can make a custom carrier board while keeping the compute module itself unchanged.

Source: https://www.raspberrypi.com/products/compute-module-5/

## Candidate D — Qualcomm Robotics RB5 / QRB5165

Qualcomm documents the RB5 platform around the QRB5165, with heterogeneous compute, AI acceleration, advanced imaging, Wi-Fi, and cellular support through companion modules. It is aimed at robotics rather than phones, so licensing, availability, thermal design, and software access need to be evaluated before any selection.

Sources:
https://www.qualcomm.com/news/press-kits/robotics-rb5-platform
https://www.qualcomm.com/internet-of-things/products/flight-rb5-platform

## Development strategy

The project should separate:

- **Prototype path:** fastest route to a working custom carrier board.
- **Production compute path:** highest control over the final motherboard.
- **Software bring-up path:** platform with the clearest documentation and development ecosystem.

No candidate is selected yet. The decision should use the product requirements, power budget, mechanical envelope, software needs, supply chain, and required radio functionality.

## Current assessment

The Raspberry Pi Compute Module 5 is useful as a low-risk custom-carrier prototype because Raspberry Pi publishes electrical and mechanical design information. NXP i.MX platforms are stronger candidates when deeper board-level control is required. Qualcomm RB5 is interesting for a high-compute, camera, and connectivity-heavy design but needs a deeper access/licensing review.

This document is research input, not a ranking.
