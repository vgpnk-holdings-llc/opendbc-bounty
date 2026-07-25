# tx-fuzzy-test-clean — add test_panda_safety_tx_fuzzy

Bounty issue: [commaai/opendbc#32425](https://github.com/commaai/opendbc/issues/32425)

Base: `commaai/opendbc@c9b31d21b`. Source change commit: `f86d7b4cb` (published here as file contents only — standalone repo because the commaai org blocks forking).

## How to apply

```
git clone https://github.com/commaai/opendbc.git && cd opendbc
git checkout c9b31d21b
# copy every file listed below from this branch into the same relative path
```

## Changed files (2)

- `opendbc/car/tests/test_models.py`
- `opendbc/testing.py`

## Validation status

Ported to master's `opendbc.testing.fuzzy_test` framework (hypothesis was removed upstream). Verified green: 198 passed / 0 failed across 248 platforms.

No bounty completion is claimed; merge/payout is comma's call.
