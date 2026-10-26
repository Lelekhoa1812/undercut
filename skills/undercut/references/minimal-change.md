# Minimal-change decision guide

Choose the least code that solves the **specified behavior** while preserving existing contracts.

## Ordered search

1. **No code:** Is a setting, documented command, or existing behavior enough?
2. **One edit:** Can an existing conditional, function, or configuration implement it?
3. **One local addition:** Can a new small function or file do it without new architecture?
4. **Extension:** Only after evidence proves the above insufficient, add the narrowest structure.

## Keep the scope literal

- Prefer local fixes over subsystem refactors.
- Avoid new dependencies unless necessary; demonstrate why built-ins/existing dependencies fail.
- Do not add an interface for one implementation, a generic abstraction for one use case, caching without measured need, or a configuration setting without an actual choice.
- No speculative scaling, rewriting to fashionable patterns, incidental cleanup, mass reformatting, or drive-by dependency upgrades.
- For a touched function, preserve unrelated inputs/outputs and error branches.
- For an existing bug, add or adjust the smallest focused regression test available in the repository.

## Micro-plan (usually internal)

"Change **[one behavior]** in **[existing location]**. Verify with **[focused check]**. Leave **[explicit non-goal]** untouched."

If no reasonable narrow approach exists, explain the demonstrated coupling and ask whether scope may expand. Do not hide an architectural rewrite inside a small task.

## Short does not mean brittle

A two-line shortcut is not acceptable if it leaks secrets, bypasses authorization, corrupts data, or knowingly violates a required contract. Read [risk boundaries](risk-boundaries.md) in such cases.
