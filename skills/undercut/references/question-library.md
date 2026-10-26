# Question library

Use **as patterns**, not as a scripted interrogation. Ask only about unknowns actually material to the next change.

## Bug fix
- "Is the expected outcome **A** or **B** for this exact input? I can reproduce the current **C**."
- "Which environment reproduces it? The codepaths differ across **[verified options]**."

## New behavior
- "What should the user see when **[specific condition]**? That chooses the return/error branch."
- "Should this apply only to **[feature X]** or also **[feature Y]**? The request mentions only X."

## Data / schema
- "Can existing records be rewritten, or must all changes preserve their current representation?"
- "What is the source of truth for **[field]**? Two inspected sources disagree."

## API / integration
- "Should a timeout return **[status A]** or retry **[once]**? This affects the user-visible contract."
- "Is **[environment]** the authorised target for this external write?"

## UI
- "When **[field]** is empty, should we hide the action or show a validation error?"
- "Is the established component **[verified]** the intended one, or do you want a separate view?"

## Tests
- "There is no focused test runner for this path. Is a direct manual check acceptable for this low-risk change?"

**Bad:** "Tell me everything about your vision." **Good:** "What must happen if the login link is expired?"
