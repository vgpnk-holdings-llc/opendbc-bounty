# hyundai-stock-button-logic — match stock Hyundai button logic

Bounty issue: [commaai/openpilot#30950](https://github.com/commaai/openpilot/issues/30950)

Base: `commaai/opendbc@c9b31d21b`. Source change commit: `edded58` (published here as file contents only — standalone repo because the commaai org blocks forking).

## How to apply

```
git clone https://github.com/commaai/opendbc.git && cd opendbc
git checkout c9b31d21b
# copy every file listed below from this branch into the same relative path
```

## Changed files (8)

- `opendbc/car/hyundai/carstate.py`
- `opendbc/car/hyundai/interface.py`
- `opendbc/car/hyundai/values.py`
- `opendbc/safety/modes/hyundai_common.h`
- `opendbc/safety/tests/common.py`
- `opendbc/safety/tests/hyundai_common.py`
- `opendbc/safety/tests/test_hyundai.py`
- `opendbc/safety/tests/test_hyundai_canfd.py`

## Validation status

Tests green: 447 + 1310 panda safety tests and 249 interface tests. Covers Hyundai CAN and CAN-FD.

No bounty completion is claimed; merge/payout is comma's call.
