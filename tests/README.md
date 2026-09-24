# Nebula Software Tests

## Test layers

- Unit tests for portable logic
- Integration tests for service boundaries
- Platform tests for board support
- Hardware-in-loop tests for real peripherals
- Release tests for update and recovery

## Test rule

A passing software test must identify what layer it validates. A unit test does not prove that the physical hardware works.
