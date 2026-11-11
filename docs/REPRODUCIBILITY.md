# Reproducibility and provenance

## What this repository contains

| Item | Present? | Role |
| --- | --- | --- |
| Original GridWorld aggregation CSV | **Yes** | 16,368-row saved finite-domain enumeration |
| Original 12-cell summary | **Yes** | Reaggregated comparison counts |
| SHA-256 and structure verifier | **Yes** | Rechecks saved-data integrity and consistency |
| Regression tests | **Yes** | Tests reference data and tampering rejection |
| GitHub Actions verification workflow | **Yes** | Runs the verifier on relevant changes |
| Canonical GridWorld simulator generator | **No** | Required for independent fresh trajectory enumeration |
| Complete V9.1.1 LunarLander experiment source | **No** | Retained separately; not part of this public release |
| Definitive LunarLander trained models/results | **No** | No confirmed population-level claim |

## Reproduce saved-data verification

Requires **Python 3.11 or later**. No third-party dependencies are required for the archived-data verifier.

From the repository root:

~~~bash
python tools/verify_gridworld_enumeration.py
python -m unittest discover -s tests -p test_gridworld_evidence.py -v
~~~

The verifier checks the SHA-256 of [`identifiability_enumeration.csv`](../evidence/gridworld/identifiability_enumeration.csv) against:

`d7346f6a307e4b711738ac45cc81df517490005edae39595a50d3e4e84eb3f48`

The file is tracked with **CRLF** line endings. The repository's [`.gitattributes`](../.gitattributes) marks the file as non-text for Git normalization purposes so the registered bytes are preserved across checkout platforms.

Expected verified totals:

- **16,368** CSV data rows.
- **1,364** action strings for each hypothesis/field-contract cell.
- **12** cells, each with **32,736** state–string comparisons.
- **392,832** exact comparisons across the declared universe.

All 12 unresolved counts appear in [GridWorld findings](GRIDWORLD_FINDINGS.md).

## What this does not reproduce

This workflow does **not**:

- Rerun the deterministic GridWorld simulator for all state/action combinations.
- Regenerate the causal ambiguity and active-probe witness from canonical source.
- Train Double-DQN agents in LunarLander-v3.
- Establish a population-level effect, confidence interval, or publication acceptance.

A future fully reproducible source release requires the canonical simulation implementation, compatible tests and non-code assets, deterministic enumeration entry point, and verified provenance manifest.

## Scientific reproducibility versus artifact integrity

A stored CSV may be byte-authentic and internally coherent without independently establishing that the simulator which generated it was correctly implemented. This is why the current release labels its results as **archived-evidence verified**, with source-level reproduction still pending.

The data is suitable for inspection and the bounded comparisons are clearly specified. It should not be cited as if this public checkout were the full V9/V10 experimental system.
