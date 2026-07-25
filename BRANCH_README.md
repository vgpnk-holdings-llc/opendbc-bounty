# safety-branch-coverage-clean — enable 100% branch coverage check

Bounty issue: [commaai/opendbc#2557](https://github.com/commaai/opendbc/issues/2557)

Base: `commaai/opendbc@c9b31d21b`. Source change commit: `68030ad22` (published here as file contents only — standalone repo because the commaai org blocks forking).

## How to apply

```
git clone https://github.com/commaai/opendbc.git && cd opendbc
git checkout c9b31d21b
# copy every file listed below from this branch into the same relative path
```

## Changed files (46)

- `opendbc/safety/declarations.h`
- `opendbc/safety/helpers.h`
- `opendbc/safety/modes/body.h`
- `opendbc/safety/modes/chrysler.h`
- `opendbc/safety/modes/chrysler_cusw.h`
- `opendbc/safety/modes/ford.h`
- `opendbc/safety/modes/gm.h`
- `opendbc/safety/modes/honda.h`
- `opendbc/safety/modes/hyundai.h`
- `opendbc/safety/modes/hyundai_canfd.h`
- `opendbc/safety/modes/hyundai_common.h`
- `opendbc/safety/modes/mazda.h`
- `opendbc/safety/modes/nissan.h`
- `opendbc/safety/modes/psa.h`
- `opendbc/safety/modes/rivian.h`
- `opendbc/safety/modes/subaru.h`
- `opendbc/safety/modes/subaru_preglobal.h`
- `opendbc/safety/modes/tesla.h`
- `opendbc/safety/modes/toyota.h`
- `opendbc/safety/modes/volkswagen_common.h`
- `opendbc/safety/modes/volkswagen_meb.h`
- `opendbc/safety/modes/volkswagen_mlb.h`
- `opendbc/safety/modes/volkswagen_mqb.h`
- `opendbc/safety/modes/volkswagen_pq.h`
- `opendbc/safety/safety.h`
- `opendbc/safety/tests/common.py`
- `opendbc/safety/tests/hyundai_common.py`
- `opendbc/safety/tests/test.sh`
- `opendbc/safety/tests/test_body.py`
- `opendbc/safety/tests/test_chrysler.py`
- `opendbc/safety/tests/test_chrysler_cusw.py`
- `opendbc/safety/tests/test_ford.py`
- `opendbc/safety/tests/test_gm.py`
- `opendbc/safety/tests/test_honda.py`
- `opendbc/safety/tests/test_hyundai.py`
- `opendbc/safety/tests/test_hyundai_canfd.py`
- `opendbc/safety/tests/test_mazda.py`
- `opendbc/safety/tests/test_rivian.py`
- `opendbc/safety/tests/test_subaru.py`
- `opendbc/safety/tests/test_subaru_preglobal.py`
- `opendbc/safety/tests/test_tesla.py`
- `opendbc/safety/tests/test_toyota.py`
- `opendbc/safety/tests/test_volkswagen_meb.py`
- `opendbc/safety/tests/test_volkswagen_mlb.py`
- `opendbc/safety/tests/test_volkswagen_mqb.py`
- `opendbc/safety/tests/test_volkswagen_pq.py`

## Validation status

100% branch coverage achieved; safety test suite green (3981 tests OK); reviewer-reproduced on the base commit.

No bounty completion is claimed; merge/payout is comma's call.
