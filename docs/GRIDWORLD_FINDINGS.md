# GridWorld experiment: finite-domain findings

## Comparison universe

The completed dataset describes a deterministic **5×5 GridWorld**, with:

| Dimension | Declared scope |
| --- | --- |
| Initial conditions | 24 known non-goal grid states |
| Action alphabet | `U, R, D, L` |
| Policies evaluated | Every nonempty open-loop cardinal-action string of length at most five |
| Number of action strings | `4 + 16 + 64 + 256 + 1,024 = 1,364` |
| Mechanism hypotheses | Two-step memory lag (**M**); interface shadow (**I-F2**); queued interface shadow (**I-F4**) |
| Hypothesis pairs | M/I-F2; M/I-F4; I-F2/I-F4 |
| Observation contracts | None, wall contact, landmark identity, both |
| Exact comparisons | **24 × 1,364 × 3 × 4 = 392,832** |

Each combination of hypothesis pair and protected-field contract covers **32,736** starting-state/action-string comparisons.

### Outcome definition

A comparison is **unresolved** when the two hypotheses produce the same **delivered observation history** under the registered state, action string, and protected-field contract. This definition concerns the information available to the observer, not whether the simulator's internal trajectories agree.

## Complete comparison table

| Protected fields | M vs I-F2 | M vs I-F4 | I-F2 vs I-F4 |
| --- | ---: | ---: | ---: |
| None | 114 | 32,736 | 114 |
| Wall contact | 114 | 15,900 | 114 |
| Landmark identity | 92 | 23,263 | 114 |
| Wall contact + landmark identity | 92 | 11,444 | 114 |

All counts are unresolved comparisons **out of 32,736 per cell**.

### Finding 1: passive ambiguity

For a registered initial state `[0, 2]`, action sequence `RRLL` generates an identical delivered-position history under M and I-F2 while the oracle histories differ. This is a concrete **existence witness** of observational ambiguity.

It does not establish that M and I-F2 are indistinguishable across all states and possible actions. The complete enumeration makes clear that many other comparisons can separate them.

### Finding 2: active diagnosis

At the specified post-`RRLL` branch, a one-step wall-directed `L` action distinguishes the matched M/I-F2 cases whereas the tested `R` continuation does not.

The conclusion requires a known initial state, deterministic executed actions, the experiment's particular observation contract, no simultaneous execution-path anomaly in the M/I comparison, and the registered time horizon. It is not a general safety guarantee for diagnostic actions.

### Finding 3: partial protected evidence

For M versus I-F4, all 32,736 comparisons are unresolved without protected fields. Protecting both wall contact and landmark identity reduces that count to 11,444, but a large ambiguous region remains.

The experiment therefore illustrates the value **and limits** of independent field-level measurements. Authenticity of a protected field must not be confused with authenticity or freshness of the entire delivered frame.

## Evidence and validation

The original [saved enumeration CSV](../evidence/gridworld/identifiability_enumeration.csv) contains **16,368** policy/pair/contract aggregation rows covering all **392,832** comparisons. Its registered SHA-256 is:

`d7346f6a307e4b711738ac45cc81df517490005edae39595a50d3e4e84eb3f48`

This exact CSV and its [12-cell reaggregation](../evidence/gridworld/table2_reaggregated.csv) are included in the public repository.

The [verification script](../tools/verify_gridworld_enumeration.py) checks the byte hash, row schema, action horizons, comparison coverage, field-contract consistency and count totals. Automated GitHub checks execute the verifier and its regression tests.

**Important:** The published evidence is an **archived experiment output**. Verifying it independently is not the same as independently regenerating every simulator comparison. The canonical GridWorld simulator source and its complete test assets have not yet been released here. An earlier working-copy audit reported 50/50 GridWorld unit tests passing, but those tests are not included in the current public package.

## Limitations

The enumerated finite environment does not establish behavior for unknown initial states, stochastic dynamics, alternative interface mechanisms, unbounded policies, or real-world adversarial settings. No LunarLander population-effect estimate follows from these counts.
