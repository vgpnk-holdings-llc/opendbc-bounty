# opendbc-bounty

This repo is a standalone snapshot of comma bounty work against [commaai/opendbc](https://github.com/commaai/opendbc) at base commit `c9b31d21b` ("Volkswagen: add Skoda Superb Mk3 firmware fingerprint (#3576)"). It exists as a standalone repo because the commaai GitHub org blocks forking, so the normal fork + pull-request workflow is unavailable; each bounty branch is published here instead. Every branch contains ONLY the files changed relative to the base commit (full new contents), plus a `BRANCH_README.md` with the exact file list and instructions to apply the change onto a real clone of `commaai/opendbc@c9b31d2`.

## Branches

| Branch | Bounty issue | Change | Files |
|---|---|---|---|
| `safety-branch-coverage-clean` | [commaai/opendbc#2557](https://github.com/commaai/opendbc/issues/2557) | Enable 100% branch coverage check and fix all violations | 46 |
| `tx-fuzzy-test-clean` | [commaai/opendbc#32425](https://github.com/commaai/opendbc/issues/32425) | Add `test_panda_safety_tx_fuzzy` (fuzz TX path on `opendbc.testing.fuzzy_test`) | 2 |
| `hyundai-stock-button-logic` | [commaai/openpilot#30950](https://github.com/commaai/openpilot/issues/30950) | Match stock Hyundai button logic (CAN + CAN-FD) | 8 |

No bounty completion is claimed by this repo; merge and payout decisions are entirely comma's call.
