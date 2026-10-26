# Behaviour evaluation

**Purpose:** judge whether an agent using Undercut behaves as intended, not whether it can solve every programming task.

The [`cases.json`](cases.json) catalog supplies situations, user requests, whether a materially blocking question is expected, ideal behavior and failure signals. They are hypothetical evaluation scenarios, **not executions that happened**.

## Manual protocol

1. Record agent product, exact version/model if available, operating mode, installed skill commit/tag, scope and whether invocation was explicit.
2. Give the agent a fresh, minimal toy repository that implements the case's stated facts. A plain-text role-play alone is a *discussion test*, not an execution test.
3. Submit the case's `user_prompt`, adding only the case's `situation` as the repository facts/mock issue. Do not leak the ideal answer or failure signals into the agent's instructions.
4. Observe questions, inspected files, diff, commands, output and claims. Do not rescue the agent with extra hints except where the case intentionally requires a user answer.
5. Score using [the rubric](RUBRIC.md); save both positive and negative evidence with exact command/output where available.
6. Compare with the *same* agent/model and repository **without** the skill as a baseline, repeating enough samples to expose variance. Avoid cross-model superiority claims.

## Static checks

```bash
python3 scripts/evaluate_cases.py --check
```

This command checks case shape, IDs and required fields. It does **not** invoke a model, prove persona compliance, or assign accuracy scores.

## Interpreting a failure

Determine whether failure came from the skill wording, missing host activation, untrusted repository context, unavailable tools, unclear case setup, or nondeterministic behavior. Fix the narrowest demonstrated cause and add a regression case; do not automatically lengthen `SKILL.md`.
