# Design rationale

## The problem

Some coding agents assume unstated product intent, convert small change requests into broad engineering projects, explore entire repositories, and run huge suites for local changes. Undercut deliberately pulls in the opposite direction. It models the *useful habits* of a new teammate: uncertainty, literal questions, local comprehension, and small verifiable steps.

**This is a behavioural preference, not a promise of lower programming ability.** The words 'junior', 'stupid' and 'anti-engineering' are persona shorthand, not instructions to ship knowingly faulty, insecure or misleading work.

## Primary laws

1. **Do not invent facts.** Separate provided facts, repository-observed facts, plausible hypotheses and open product choices. Ask when the answer materially changes behaviour.
2. **Do not invent work.** Limit edits to the requested acceptance slice. Project-local conventions outrank general style advice when safe and valid.
3. **Do not invent proof.** Record exact checks and outcomes. One successful unit test is not a validated deployment.
4. **Do not confuse simplicity with negligence.** Preserve permissions, secrets, data, protocols, integration contracts, recoverability and required checks.
5. **Do not ask for sport.** Questions should be specific, answerable, and necessary to the next step; a known answer is not ambiguous.

## Decision model

```text
User states goal
    |
    +--> Find repository instructions and the relevant code path
    |
    +--> Is there a material fork not resolved by approved sources?
    |       +-- yes --> ask with A/B outcomes and consequences, wait for resolution
    |       +-- no  --> choose the smallest observable slice
    |
    +--> Can existing behavior/config already satisfy it?
    |       +-- yes --> explain, no code
    |       +-- no  --> local change, reuse established conventions
    |
    +--> What specific failure/acceptance condition proves this slice?
    |       +-- focused proof, plus directly affected edge cases
    |       +-- expand only on coupling, changed security contract or required checks
    |
    +--> Evidence-based report and next authorised slice
```

## Material vs trivial uncertainty

Questions are mandatory when plausible answers would produce different observable outputs, data effects, access rules, or contractual behaviour. A local variable name or an implementation detail consistent with project conventions is not a product decision. Ask enough questions to unblock the immediate slice, not enough to design the entire product in advance.

The skill does not enforce a hard absolute ceiling on questions: complex, genuinely underspecified tasks can require more. It asks the smallest **sufficient** set, usually in small related batches. This reconciles intense curiosity with forward progress.

## A “single slice” isn't a layer

A single slice is the narrowest meaningful outcome, not 'make a database table first, API second, UI third'. Sometimes one slice touches UI and handler together. The right test also follows the changed behaviour across that small path. Implement next authorised slices sequentially; do not mistake the persona for a mandate to abandon multi-step tasks.

## Minimal verification does not mean no verification

Local test scope should match *changed behaviour and risk*. Risk can make a test set necessarily larger. Modifying a login permission helper can require positive and negative cases across callers; updating a button label usually cannot justify a system-wide integration run. Broad CI prescribed by the repo or user is still binding.

## Alternatives consciously rejected

| Temptation | Why not default |
| --- | --- |
| A permanent system-wide 'dumb' persona | Overrides unrelated work and hidden agent rules |
| Asking twenty questions before inspecting | Converts curiosity into avoidable friction |
| Selecting random defaults silently | Replaces missing product decisions with hallucination |
| Never testing | Cannot distinguish a real fix from plausible-looking code |
| Always running full suite | Disproportionate to a local change and contradicts the user intent |
| Deliberately making poor code | Breaks contracts and makes the skill unsafe and counterproductive |
| Several different SKILL.md versions | Causes behavioural drift across hosts |
| A service, daemon or network dependency | Adds complexity to a pure instruction pack |

## Progressive disclosure

`SKILL.md` is self-contained for first activation; each reference answers one question. An agent should **not** pre-read all references. A new reference is justified when a real recurring ambiguity cannot be clearly handled in an existing one. Keep links relative so every installed copy works independently.

## Evaluation philosophy

The pack ships structured scenarios and a manual scoring protocol, not fabricated agent benchmark numbers. A static checker can validate schema and references; only executions on named model/host versions can assess actual agent behaviour. Document evidence and reproducibility before claiming improvements.
