# Clarification protocol

Read when ambiguous requirements affect the next edit.

## A good question has three parts

1. **Concrete ambiguity:** state the exact fork, not an open-ended solicitation.
2. **Consequence:** one sentence explaining how each answer changes code or behavior.
3. **Focused options:** a simple A/B choice where useful, and an opening for the user's own answer.

Example: "When the invite expires, should we show a specific 'expired' message (A), or the same 'invalid link' message (B)? This changes the error branch."

## Triage

| Unknown | Action |
| --- | --- |
| Product behavior or acceptance criterion with different possible outputs | Ask before coding that behavior |
| Authorization, billing, privacy, destructive operation, or irreversible migration | Ask/obtain explicit approval, do not assume |
| Existing code answers it definitively | Inspect and cite the actual file/function; do not ask again |
| Cosmetic detail with established project convention | Follow verified convention, disclose only if relevant |
| Choice local, reversible, with no observable impact | Choose simplest established pattern |
| User already clearly answered | Respect answer; do not re-litigate |

## Batch, then stop

Ask **all** material unresolved questions that unblock the next slice; no arbitrary limit. If ten requirements are unclear, identify which ones actually block slice one, ask those together, and park unrelated future questions. A question list is not an excuse to avoid manageable work. If answers are contradictory, quote the conflict concisely and request resolution rather than picking a winner.

Do not replace questions with silent assumptions, unless the decision is trivial, reversible, and genuinely nonmaterial. Mark tentative proposals as proposals: "I propose X because Y; does that match your intent?" is not the same as "X is required."

## When the user is unavailable

Do not make a risky or user-visible decision on their behalf. You can still inspect relevant code, reproduce a known defect, isolate likely affected locations, or draft a minimal change **without applying it**. State the blocker and the exact question. If the request has no material unknowns, implement rather than stall.

## Anti-questions

Avoid: "Can you describe the whole system?", "Shall I implement best practices?", "What do you think?", questions answerable by reading the repository, or multiple-choice forms requiring exhaustive specification. Ask about the actual *next* branch in the logic.
