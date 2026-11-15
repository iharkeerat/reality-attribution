# Reviewer guide — Reality Attribution

**Status:** student-led research programme; bounded deterministic GridWorld analysis archived and data-verified; stochastic LunarLander-v3 extension ongoing. **Not a peer-reviewed paper or a completed V9/V10 evaluation.**

## 1. Research question (30 seconds)

Can an embedded reinforcement-learning agent distinguish environment/action anomalies, delayed observations and interface manipulation **using only its delivered history**? When two mechanisms give the same history, which controlled intervention or protected measurement would make them distinguishable?

See [research overview](RESEARCH_OVERVIEW.md) for the formal hypotheses E (execution), M (memory lag) and I (interface alteration).

## 2. Exact results currently supported

The archived 5×5 deterministic GridWorld comparison comprises 24 non-goal initial states × 1,364 action sequences × 3 mechanism pairs × 4 observation contracts = **392,832 comparisons**. The claim is limited to this model, declared action horizons and observation definitions.

- [GridWorld findings](GRIDWORLD_FINDINGS.md) contains the 12-cell comparisons, one passive ambiguity witness and a tested active-diagnosis continuation.
- [Claims register](RESEARCH_CLAIMS.md) separates individual propositions from their supporting artifacts.
- [Original saved evidence](../evidence/gridworld/README.md) explains the archived CSV, summary table and byte identity.

## 3. Verify the included evidence (Python 3.11+)

From the repository root, with no third-party Python packages:

    python tools/verify_gridworld_enumeration.py
    python -m unittest discover -s tests -p test_gridworld_evidence.py -v

The verifier checks the registered CSV hash, row structure and reported aggregate counts. GitHub Actions also runs these checks on repository changes.

**Critical boundary:** verifying an archived enumeration table is **not** regenerating simulator trajectories. The canonical deterministic simulator/generator and full V9.1.1 LunarLander pipeline are not in this public checkout.

## 4. What a reviewer should *not* infer

- No general theorem that all environmental changes, sensor delays and tampering are distinguishable.
- No independently reproduced state-of-the-art LunarLander improvement, generalised real-world safety result or population-level confidence interval.
- No source-based end-to-end regeneration of the original GridWorld comparison from the public files alone.
- The private/historical research code and public evidence snapshot are different release scopes.

For precise omissions, consult [reproducibility](REPRODUCIBILITY.md).

## 5. Next scientific steps

Recover and license-check canonical simulation sources and assets, add deterministic regeneration with protocol/version locking, independently inspect the matched ambiguity witness, evaluate controlled baselines and uncertainty on held-out stochastic settings, and publish negative as well as positive results.

**Suggested review path:** [overview](RESEARCH_OVERVIEW.md) → [findings](GRIDWORLD_FINDINGS.md) → [claims](RESEARCH_CLAIMS.md) → [reproducibility](REPRODUCIBILITY.md) → [verification script](../tools/verify_gridworld_enumeration.py).
