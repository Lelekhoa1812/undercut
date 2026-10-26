# Contributing

Contributions should make the skill **simpler, more precise, or more honest**.

## Before proposing a change

Describe the unwanted behavior with a short example and show how the proposed wording changes the next agent action. Keep changes to one behavior where possible. Don't expand the skill into a framework for unrelated work.

## Pull request checklist

- [ ] The change solves a described, observable problem.
- [ ] No unsupported claim about a model, host, API, or security guarantee.
- [ ] No new abstraction or dependency without evidence it is needed.
- [ ] On-demand references stay within `skills/undercut`.
- [ ] Relevant scenarios and tests reflect the behavior.
- [ ] `python3 scripts/undercut.py check` passed.
- [ ] `python3 -m unittest discover -s tests -v` passed (or failure honestly disclosed).
- [ ] Docs and changelog updated if public behavior changed.

Please avoid confidential user details or real access tokens in issues, snippets, logs, and fixtures. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
