# Focused verification

**Aim:** enough evidence for the *changed slice*, not ceremony across the whole repository.

## Pick a proof proportional to impact

| Change | Default focused proof |
| --- | --- |
| Pure function bug | One focused unit/regression test for failing input; nearby edge case if directly affected |
| UI copy/layout | Inspect the changed view or run a component-level check; snapshot only if already conventional |
| API response behavior | Targeted handler/contract test, including the specific failure path |
| Config/CLI behavior | One command with relevant input, plus invalid input when failure behavior changes |
| Documentation | Check referenced paths, commands, and examples where feasible |
| Auth/payment/privacy/data-destructive behavior | Mandatory contract, negative-path, and safety checks **as required by risk**; escalate beyond one test if necessary |

1. Identify the changed behavior and its failure mode.
2. Find the most local existing test mechanism. Do not invent a test runner.
3. Reproduce failure **when feasible**. Apply minimal change. Run that proof.
4. Record **exact command / case / observed result**. If blocked, state "not run" and why.
5. Expand only if a failure, touched shared contract, coupling evidence, risk, or explicit instruction requires it.

**Do not** say "all tests pass" when only one test passed. Say "`<command>` passed (1 targeted test); broader suite not run." No tests at all is not a success claim. If no test infrastructure exists, a manual targeted proof may be appropriate for low-risk changes; disclose its limits.

## Expansion triggers

Shared library/API used by multiple modules; schema or migration changes; security boundary changes; race conditions; shared build configuration; concurrency; integration failures; regressions revealed by the focused test; or required CI / repository checks. State the reason before widening scope.

Do not disable or remove tests, mask failed checks, or fake fixtures to obtain a green result.
