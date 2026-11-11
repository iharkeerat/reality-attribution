# Claim-to-evidence register

This table identifies what can be defended from the files currently available to a reader. A **saved-data check** is not a fresh simulator reproduction; a **research plan** is not an empirical outcome.

| ID | Claim | Supporting artifact | Current verification level |
| --- | --- | --- | --- |
| G1 | The registered GridWorld comparison universe contains **392,832** comparisons | 24 known states × 1,364 action strings × 3 pairs × 4 contracts; [original enumeration](../evidence/gridworld/identifiability_enumeration.csv) | Arithmetic and archived-data verification |
| G2 | The GridWorld unresolved-count table has the reported 12 cells | [Original enumeration CSV](../evidence/gridworld/identifiability_enumeration.csv), [reaggregated table](../evidence/gridworld/table2_reaggregated.csv), [verifier](../tools/verify_gridworld_enumeration.py) | Registered SHA-256, schema checks, exact reaggregation; automatic tests |
| G3 | One registered M/I-F2 pair has equal delivered `RRLL` histories and is separated by a wall-directed `L` probe | Original research manuscript and separate canonical GridWorld source archive | Documented controlled witness; fresh public-source reproduction still pending |
| G4 | A previous standalone GridWorld source test suite passed 50 tests after support assets were restored | November 2026 working-copy audit, separate from this public release | Earlier test execution; **not** equivalent to the CI tests in this repository |
| L1 | A LunarLander-v3 research framework was developed | Separate, unpublished V9/V9.1.1 research source archives | Ongoing implementation; not a completed population study |
| L2 | Active probing improves stochastic LunarLander attribution or control outcomes | Proposed evaluation protocol | **Not established** |
| L3 | Protected observation fields improve LunarLander diagnosis | Proposed evaluation protocol | **Not established** |

## What the automated check establishes

The public repository's [GridWorld verifier](../tools/verify_gridworld_enumeration.py) checks that the **archived data bytes** match the research-record SHA-256, the declared finite-domain design is consistent, and the unresolved counts agree with the research table.

The automatic regression tests also check that an altered artifact is rejected. Neither check recomputes original agent trajectories or evaluates LunarLander.

## Methodological commitments

- Report ambiguity **relative to** a specified observer, information contract, intervention, initial-state assumption, and horizon.
- Distinguish correct attribution among **all scheduled events** from conditional accuracy among completed diagnostic probes.
- Keep oracle scoring variables outside deployable agent features.
- Distinguish field integrity from observation freshness and from whole-frame authentication.
- Report independent-run uncertainty before claiming stochastic-environment performance.

These are methodological requirements and open validation tasks, not proof that every required LunarLander test has already been passed.
