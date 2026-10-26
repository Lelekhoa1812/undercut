# Maintainer playbook

## Authority and source layout

`skills/undercut/SKILL.md` is the single behavioural entry point. Its sibling `references/` and `assets/` are deliberately small and optional at runtime. Root docs explain the pack, `examples/` teach humans the expected conversations, and `evaluation/cases.json` is the structured behavioural prompt catalog.

Do not modify copies installed into `.claude/`, `.cursor/`, or `.agents/` and treat them as source. Change `skills/undercut/` and reinstall.

## The smallest useful release process

1. Read the diff and ensure every newly asserted behaviour can be traced to `SKILL.md` or a referenced document.
2. Update cases and examples only where the rule changes; don't game a benchmark to fit instructions.
3. Run `make check`, `make test`, and `make evaluate` or their equivalent Python commands.
4. Build the skill ZIP and inspect its member paths; it must have one top-level `undercut/` folder.
5. Check installation in a temporary project for each supported agent, including no-overwrite and dry-run behavior.
6. Check the changelog and tag an actual release only if publishing rights exist; CI on a tag can attach the skill ZIP as a build artifact.
7. Publish a release note identifying what changed, the exact checks, and any untested host behaviour.

## Versioning

Use semantic tags (`vMAJOR.MINOR.PATCH`) for public releases, where major changes alter the behavioural contract; minor releases add meaningful guides or features; patch releases fix inaccuracies and packaging defects. `CHANGELOG.md` starts at *Unreleased* until the first publication.

## No manufactured badges

Do not put '100% tested', 'enterprise certified', model success percentages, downloads or GitHub stars on the README without independently reproducible evidence.

## Future candidates, not promises

Possibilities worth evaluating include a user-selectable question intensity preset, a recorded behavioural evaluation harness, a dedicated IDE marketplace listing, and localization of the question examples. Require evidence that each improves outcomes; the existing format remains the default.

## Accuracy checklist

Before a release, manually compare the README's command-line examples to `python3 scripts/undercut.py --help` and `python3 scripts/undercut.py install --help`. Update host paths only against current upstream guidance and never claim real-world model compliance from offline schema tests.
