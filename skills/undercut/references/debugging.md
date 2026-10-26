# Junior debugging loop

1. **Ask for the observable failure** if not given: exact error, expected output, actual output, and how to reproduce. Ask only what is missing and material.
2. **Reproduce locally** with the smallest input / call / test available. If reproduction is impossible, label the diagnosis unconfirmed.
3. **Trace narrowly:** inspect the failing branch and closest callers; identify one root cause hypothesis grounded in the trace.
4. **Patch that cause**, not every nearby imperfect thing.
5. **Prove exactly this failure is resolved** with the reproduction/test; include one directly affected edge case when useful.
6. **Report evidence and limits**; do not claim broad correctness.

If the first hypothesis is contradicted, re-evaluate from observed evidence. Do not stack unverified patches or enter an endless retry loop. For conflicting signals, pause and present the exact contradiction and question.

**No danger shortcuts:** do not remove authorization checks, catch-and-ignore errors, hardcode secrets, swallow exceptions, use unsafe eval, or hide failed tests to make a symptom disappear.
