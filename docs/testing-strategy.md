# Testing strategy: proof proportional to blast radius

One changed branch should usually get one local proof. Undercut does not equate "I changed a file" with "I must run every check in this monorepo." The testing decision begins with the risk of *the specific change*, not the existence of a large suite.

## Evidence levels

1. **Local observation:** direct reproduction, command, or UI confirmation. Suitable for simple low-risk behavior if no test infrastructure exists.
2. **Targeted test:** test for changed function/component/endpoint. Preferred for logic changes.
3. **Adjacent regression check:** nearby case if the same predicate or contract is affected.
4. **Broader integration / suite:** when verified coupling, shared contracts, security, data, or repository policy require it.

Moving to level 4 is not failure; running it unthinkingly for every one-line change is the anti-pattern.

## Mandatory transparency

Every completion says what was run, what passed or failed, and what was not run when relevant. A focused success is evidence for that behavior, not a blanket guarantee.

## Test anti-shortcuts

Never disable or weaken test assertions just to pass; never remove auth checks, hide errors, fake mock behavior, or change unrelated contracts to avoid a test. Unreproducible changes must be labelled as unverified rather than declared finished.

For decision examples, see [Focused verification](../skills/undercut/references/focused-verification.md).
