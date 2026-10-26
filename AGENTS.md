# Agent instructions for maintaining Undercut

This file applies to contributors **inside this repository**. It does **not** automatically activate the Undercut persona for every task. The installable skill's canonical source is `skills/undercut/SKILL.md`.

- Read `README.md` and the relevant skill reference before editing behavior.
- Preserve the persona: asks material questions, one slice, smallest safe edit, focused truthful verification.
- No invented agent features, routes, network calls, licences, or product requirements.
- Do not move references outside `skills/undercut`: installation copies only that directory.
- If changing installer/validator, add focused unit tests.
- If changing behavior, add/update scenario expectations in `evaluation/cases.json`.
- Run `python3 scripts/undercut.py check` and `python3 -m unittest discover -s tests -v` on changes to the pack.
- Keep all source public-safe; never commit credentials, logs with sensitive data, or private project context.
