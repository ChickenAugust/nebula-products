# 0001 — Platform strategy

Status: Proposed

Nebula software will separate platform-specific code from portable system services.

The application processor platform, boot chain, and operating-system implementation are allowed to change without rewriting higher-level services.

Consequences:
- Board support lives below stable service interfaces.
- Hardware-specific assumptions must be documented.
- Early development can use emulation or development boards before final hardware exists.
