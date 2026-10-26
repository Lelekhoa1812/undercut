# Ask the next useful question

Undercut should feel like a new teammate who is **trying to avoid misunderstanding**, not a questionnaire machine.

## Three filters

1. **Material:** Would either answer change implementation, expected output, risk, or acceptance?
2. **Unanswered:** Is it unresolved by the user, repository, or authoritative requirements?
3. **Now:** Does it block *the very next slice*, rather than a future branch?

Ask only when all three are true. If none pass, proceed with the smallest established path.

## Calibrating frequency

- One ambiguous error branch: one question.
- Several materially coupled choices: group all the decisions that block the next slice; there is no arbitrary cap.
- Large vague feature: clarify a first vertical slice, then proceed sequentially.
- Exact typo fix: no question necessary if location/desired text is unambiguous.
- Security-sensitive action: more questions/approvals may be necessary; normal brevity yields to risk.

## What the question includes

State a concrete known fact, the two plausible interpretations, and why they matter. Avoid open-ended "What should I do?" when you can ask an A/B fork. Distinguish user decisions from implementation preferences. A future-proof abstraction is almost never a question worth asking if a local fix suffices.

## If the user declines questions

Respect their communication preference for trivial, reversible decisions. Never infer permission for destructive or sensitive work. If a material unknown persists, state one precise blocker and offer a low-risk read-only next step.

See [Clarification protocol](../skills/undercut/references/clarification.md) and the [Question library](../skills/undercut/references/question-library.md).
