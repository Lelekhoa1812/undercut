# Compatibility notes

Undercut uses the portable [Agent Skills](https://agentskills.io/) format: a folder named `undercut` containing `SKILL.md` with YAML frontmatter and relative reference files. It is written for coding assistants that expose local skills.

## Intended platforms

| Agent | Conventional location | Invocation examples | Notes |
| --- | --- | --- | --- |
| Codex | `.agents/skills/undercut/` | skill selector, `$undercut` when supported | Host determines when to load and activate |
| Claude Code | `.claude/skills/undercut/` | `/undercut` when supported | May require reloading if skill not visible |
| Cursor | `.cursor/skills/undercut/` | `/undercut` or `@` skill picker when supported | Also recognises compatible skill paths; avoid accidental duplicate copies |
| GitHub Copilot | `.github/skills/undercut/` | host skills picker | VS Code / cloud variants control activation and permissions |
| Gemini CLI | `.gemini/skills/undercut/` | `/skills list` and activation prompt | Workspace trust and activation consent may apply |
| Other Agent Skills hosts | host's documented skills folder | host-specific | Manual installation required unless an equivalent target is supported |

These are intended integration paths based on public host documentation, **not certification of tested behavior for every current release**. Host UI, loading and naming rules may change. Confirm your installed agent's docs when activation differs.

**Duplication caveat:** Cursor can discover `.agents/skills/` and other host skill locations as well as `.cursor/skills/`; installing with `--agent all` in the same project may therefore expose duplicate `undercut` entries. Prefer installing to the one location most appropriate for your primary agent, or use compatible shared `.agents/skills/` when available.

## Behavior is probabilistic

An instruction file cannot force an agent to comply with policies, run particular commands, or forgo broad exploration. Host/developer/system instructions may override this skill. The agent may not have a repository, execution access, or question interface. Undercut tells it to state those limits, not to fabricate evidence.

## Sources for maintainers

- Agent Skills specification: https://agentskills.io/specification
- Codex skill guidance: https://learn.chatgpt.com/docs/build-skills
- Claude skills guidance: https://docs.anthropic.com/en/docs/claude-code/skills
- Cursor skills documentation: https://cursor.com/help/customization/skills
- GitHub Copilot skills documentation: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Gemini CLI skills documentation: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md

Review these upstream sources before changing supported paths or frontmatter syntax. No vendor endorsement is implied.
