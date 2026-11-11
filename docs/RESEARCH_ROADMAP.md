# Research development roadmap

This is a scientific development plan, **not** a list of completed results.

## Track A — GridWorld independent source reproduction

- [x] Preserve the archived enumeration with its original SHA-256.
- [x] Publish a verifier for all 12 cells and the declared finite-domain comparison total.
- [x] Add automated integrity and regression checks.
- [ ] Publish the **canonical** GridWorld simulation source and required test assets.
- [ ] Provide a one-command source-level enumeration, compare its freshly generated CSV with the registered archive, and record its runtime.
- [ ] Recreate the passive-equivalence and matched active-probe witnesses from source.

## Track B — LunarLander-v3 evaluation

- [ ] Select one authoritative V9.1.1 source/configuration and dependency environment.
- [ ] Validate observation, reward, execution, and termination/truncation semantics.
- [ ] Verify the delivered-history/oracle-history boundary and exact pre-onset causal matching.
- [ ] Define the primary evaluation population, including unreachable and abstained diagnostic opportunities.
- [ ] Compare passive classification against matched-budget diagnostic and passive controls.
- [ ] Report probe cost, intervention risk proxies, independent-run uncertainty, and ablations.
- [ ] Publish code/checkpoints/results with versioned provenance once independently validated.

## Open questions

1. How does causal identifiability change with partial observations or unknown initial state?
2. How can diagnostic actions balance information gain with environmental cost or physical risk?
3. What minimal field-level integrity contract restores useful distinctions?
4. When should an agent abstain rather than infer an unsupported causal explanation?
5. Can trustworthy attribution improve downstream decisions in a held-out stochastic-control evaluation?

Future work should be judged by reproducible evidence and explicit assumptions, rather than broad claims about an AI's access to reality.
