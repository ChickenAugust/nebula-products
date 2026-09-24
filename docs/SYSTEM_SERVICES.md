# Nebula System Services

## Core services

### Power
Owns battery state, charging state, thermal limits, sleep, wake, and shutdown policy.

### Connectivity
Owns network interfaces and connection state without exposing raw hardware details to applications.

### Audio
Owns routing, volume, microphone access, speaker output, and policy.

### Display
Owns display discovery, modes, backlight, touch input, and display power.

### Sensors
Normalizes sensor data and timestamps.

### Camera
Owns camera discovery, capture configuration, privacy state, and pipeline control.

### Update
Manages signed software artifacts, installation, recovery, and rollback.

### Diagnostics
Collects structured logs, crash information, health data, and hardware revision metadata.

## Service rules

- Services expose stable interfaces.
- Privileged services validate inputs from less-trusted clients.
- Device-specific details stay below the service boundary.
