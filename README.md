# Reality Attribution in Reinforcement Learning

**Causal identifiability · Active diagnosis · Observation integrity**

An independent research project investigating whether a reinforcement-learning agent can distinguish a change in its environment from a fault or manipulation in the information it receives.

> **Research question:** When different causal mechanisms produce the same agent-visible history, what additional evidence or intervention makes them distinguishable?

**Project status:** Completed bounded GridWorld analysis with an archived, verified enumeration dataset. The larger LunarLander-v3 investigation is ongoing. This is a research project, **not a peer-reviewed publication or a completed stochastic-control study**.

## The problem

An unexpected observation could mean that an action executed differently than intended (**E**), the agent received a delayed observation (**M**), or an observation interface manipulated the delivered information (**I**). Detecting an anomaly is not the same as determining its cause.

The key distinction is between *authentic histories* retained by the experimenter for evaluation and *delivered histories* available to the agent. If two hypotheses produce the same delivered history, passive attribution may be impossible under the specified information contract.

## Experimental approach

| Research track | Role | Evidence status |
| --- | --- | --- |
| **Deterministic GridWorld** | Exact, finite-domain comparisons of memory and interface hypotheses, active diagnostic actions, and protected observation fields | Archived enumeration data verified; source-based simulator reproduction not yet packaged here |
| **LunarLander-v3 extension** | A proposed and partially implemented evaluation framework with learned policies, stochastic dynamics, and probe costs | Ongoing; definitive population-level performance not established |

### GridWorld: exact finite-domain findings

The registered 5 × 5 GridWorld experiment covers **24 known non-goal initial states**, **1,364 open-loop action sequences** of lengths 1–5, **three hypothesis pairs**, and **four protected-field contracts**:

**24 × 1,364 × 3 × 4 = 392,832 exact comparisons.**

Three bounded findings motivate the work:

1. **Passive ambiguity:** Under a registered initial state and action history `RRLL`, a memory-delay mechanism and an interface-shadow mechanism yield the same delivered history while their oracle histories differ.
2. **Active diagnosis:** For that matched branch point, a one-step wall-directed action `L` separates the two mechanisms; the tested ordinary continuation `R` does not.
3. **Partial protected evidence:** Protecting wall-contact and landmark fields reduces—but does not eliminate—unresolved memory/interface comparisons.

| Protected fields | Unresolved M vs I-F4 comparisons |
| --- | ---: |
| None | 32,736 / 32,736 |
| Wall contact | 15,900 / 32,736 |
| Landmark identity | 23,263 / 32,736 |
| Both | 11,444 / 32,736 |

**Interpretation:** These results apply to the declared deterministic model, hypothesis set, known-state assumptions, observation contracts, and finite action horizon. They do not establish universal identifiability or deployment safety.

## Inspect the evidence

The original **16,368-row enumeration CSV** and a 12-cell reaggregation table are included under [`evidence/gridworld/`](evidence/gridworld/README.md).

```bash
# Python 3.11+; no external Python dependencies required
python tools/verify_gridworld_enumeration.py
python -m unittest discover -s tests -p test_gridworld_evidence.py -v
```

The verifier checks the registered **SHA-256**, experiment structure, coverage, and all reported table counts. GitHub Actions runs these checks automatically.

**Important:** This verifies a saved data artifact; it does **not** regenerate the 392,832 comparisons from simulator source. Canonical simulator code is being prepared as a separate reproducibility release.

## Research documentation

- [Research overview](docs/RESEARCH_OVERVIEW.md) — motivation, causal hypotheses, and study design
- [GridWorld findings](docs/GRIDWORLD_FINDINGS.md) — complete finite-domain table and assumptions
- [Claims and evidence](docs/RESEARCH_CLAIMS.md) — what each claim is supported by
- [Reproducibility](docs/REPRODUCIBILITY.md) — data provenance, verification commands, and what is not included
- [Research roadmap](docs/RESEARCH_ROADMAP.md) — active questions and validation work

## Scope and limitations

The project investigates **observer-relative causal identifiability**, not whether an agent can discover a philosophical or metaphysical ground truth. Some source variants and experimental archives remain outside this clean public research package. LunarLander-v3 results should be treated as **ongoing research**, not as established empirical superiority.

**Research interests:** Reinforcement learning · Causal inference · Partial observability · Active experimental design · Reliable AI
