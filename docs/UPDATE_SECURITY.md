# Nebula Update and Security Model

## Goals

- Authenticate software before installation.
- Protect device identity and private keys.
- Prevent accidental downgrade to unsupported images.
- Provide a recovery path after interrupted updates.

## Proposed flow

1. Discover an available signed release.
2. Download into an inactive image slot.
3. Verify signature and compatibility metadata.
4. Mark the new image as pending.
5. Boot the new image.
6. Record successful health confirmation.
7. Automatically recover if the new image fails validation.

The low-level firmware layer may use MCUboot-compatible workflows where the selected MCU and platform support them. Zephyr documents MCUboot integration, signed image handling, and OTA/DFU mechanisms.

Final cryptographic algorithms, key-storage hardware, bootloader, and rollback policy remain platform-dependent.
