# Roadmap and deliberate non-goals

## Current scope

A clear reusable skill, on-demand references, local installation, structural validation, illustrative transcripts, and human-evaluation cases.

## Possible future work (not committed)

- Confirm host-specific skill discovery changes against future official docs.
- Collect anonymised before/after conversations to assess how well questions target real decision forks.
- Add an optional model-evaluation adapter **only if** users provide a concrete need and evaluation budget.
- Add package-manager convenience wrappers **only if** copying a directory becomes a proven problem.

## Explicit non-goals

- A runtime application, dashboard, server, bot framework, or central service.
- Tool-permission bypasses, forced model behavior, auto-execution, production deployments.
- A global always-on rule installed without consent.
- A general code quality framework, test orchestrator, or monorepo audit engine.
- Adding layers of abstractions to a skill that argues against unnecessary layers.

**Guiding review question:** If this new feature disappeared, would an actual user lose a necessary part of the Undercut behavior? If not, it may not belong.
