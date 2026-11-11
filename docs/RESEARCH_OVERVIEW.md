# Research overview

## Motivation

An unexpected observation is compatible with more than one explanation. A reinforcement-learning agent may receive a stale measurement, observe the effect of an altered action, or see a value substituted by the interface that delivers observations. Detecting a mismatch is not equivalent to identifying its cause.

**Reality attribution** asks what an agent can infer about the causal source of such a mismatch from *its own available evidence*, and whether a limited diagnostic action or an independently protected measurement can resolve ambiguity.

## Question and hypotheses

> When two anomaly mechanisms generate the same delivered history, under what information and intervention contracts can an observer distinguish them?

The project separates three modelled anomaly locations:

| Symbol | Mechanism | Illustrative difference |
| --- | --- | --- |
| **E** | Execution-path anomaly | The environment receives an action different from the one the agent intended |
| **M** | Observation-memory lag | The delivered observation refers to an earlier environment state |
| **I** | Observation-interface manipulation | The delivered values are altered after the authentic environment event |

These are **experimental hypotheses**, not an exhaustive account of possible real-world faults.

A central distinction is between the **oracle history**, recorded by the simulator for ground-truth scoring, and the **delivered history**, available to the agent. A deployable diagnosis cannot be based on privileged oracle information.

## Study design

### Deterministic GridWorld

A finite 5×5 GridWorld supports exact comparison of delivered transcripts across specified states, open-loop action strings, mechanism pairs, and protected-field contracts.

It investigates three claims of limited scope:

1. Two different mechanisms can generate identical agent-visible histories under a particular controlled action sequence.
2. A chosen action may distinguish a matched pair even when an ordinary continuation cannot.
3. Protecting a subset of observation fields can reduce ambiguity without making the whole frame trustworthy.

See [GridWorld findings](GRIDWORLD_FINDINGS.md) for the precise assumptions, complete table and evidence interpretation.

### LunarLander-v3 research extension

The broader research program considers how these questions would be tested with learned value-based agents and a stochastic continuous-observation, discrete-action environment. Proposed evaluation dimensions include passive classifiers, diagnostic probes, attack parameters, held-out runs, end-to-end attribution, and probe costs.

**Current evidence boundary:** The public repository does not contain the canonical V9.1.1 LunarLander source, trained-model evidence, or definitive population-level results. That extension remains ongoing; no performance improvement is claimed.

## Interpretation

The work studies **observer-relative identifiability**: two situations can differ in simulator truth while remaining indistinguishable to an agent that sees the same delivered information.

A diagnostic intervention changes the information available to that observer, but its benefit depends on the specific hypothesis set, initial-state knowledge, action and observation contracts, and time horizon. Field-level integrity is likewise not equivalent to complete observation authenticity.

This is an engineering and causal-inference investigation, not a claim that an agent can establish metaphysical reality or that the demonstrated probe is safe for physical deployment.
