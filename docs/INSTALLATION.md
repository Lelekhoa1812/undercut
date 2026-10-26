# Installation and lifecycle

## Requirements

The skill is plain Markdown and needs no runtime dependencies. For the optional installer, tests and bundle builder use **Python 3.9+** and the standard library.

From the repository root:

```bash
python3 scripts/undercut.py check
python3 scripts/undercut.py install --agent all --scope project --dry-run
python3 scripts/undercut.py install --agent all --scope project
```

The third command installs **five separate copies** in the *current working directory*. For use in only one agent, specify `codex`, `claude`, `cursor`, `copilot`, or `gemini` rather than `all`.

## Host paths

| Host | Project | Personal |
| --- | --- | --- |
| Codex | `.agents/skills/undercut/` | `~/.agents/skills/undercut/` |
| Claude Code | `.claude/skills/undercut/` | `~/.claude/skills/undercut/` |
| Cursor | `.cursor/skills/undercut/` | `~/.cursor/skills/undercut/` |
| GitHub Copilot | `.github/skills/undercut/` | `~/.copilot/skills/undercut/` |
| Gemini CLI | `.gemini/skills/undercut/` | `~/.gemini/skills/undercut/` |

For an alternate project:

```bash
python3 scripts/undercut.py install --agent claude --scope project --project /path/to/project
```

For a personal installation:

```bash
python3 scripts/undercut.py install --agent codex --scope user
```

### Confirm an installation is current

```bash
python3 scripts/undercut.py install --agent codex --scope project --verify
```

This compares the installed package's file contents with the source; it does not modify either location.

The installer doesn't copy the root README/CI/test harness to the target, just `skills/undercut/`.

## Updates / collisions

- By default, a destination that already exists is left untouched and the command exits with an error. **No silent overwrite.**
- `--force` replaces an existing package only if the target has a normal `SKILL.md` declaring `name: undercut`. This may discard personal edits to that installed copy: back them up first.
- The installer stages the new copy and replaces a recognized installation; it does not modify the target application's source files.
- If **any** chosen target already exists without acceptable `--force`, preflight stops before installing to the other agents.
- Symbolic links inside the installed skill path are refused. Use a regular target directory.
- Install individual targets if all-host setup collides with a host's shared discovery path.

**Explicit removal:** delete only the installed `undercut` folder for the selected agent after confirming its contents. There is intentionally no aggressive recursive uninstaller.

## Manual copy

```bash
mkdir -p .agents/skills
cp -R skills/undercut .agents/skills/undercut
```

For another host, substitute its path. Don't nest one `undercut` folder inside another.

## Bundle

```bash
python3 scripts/undercut.py bundle --output dist/undercut-skill.zip
```

The ZIP contains one `undercut/` directory with `SKILL.md`, `references/`, and `assets/`. It is a distributable **skill only**, not the entire Git repository. Use the repository ZIP (`git archive`) if you need docs, examples, tests and release workflows as well.

## Activation and availability

Installation puts files in a recognized location; actual skill discovery, automatic activation, slash commands, cloud sync and precedence are controlled by the host and its version/settings. Try explicitly selecting `undercut` in the host's skill picker. If the host doesn't show it, confirm the folder layout and review the host's official documentation. Some hosts may need a session reload. Do not assume files were synced to remote agents.

## Security

Review skill instructions before installing third-party releases. The installer does not access the network or inject runtime hooks. Installing into an agent's own repository can cause that agent to discover `undercut` as a project skill; use user-level scope only if you want it available across projects.

## Troubleshooting

If a skill does not appear, an install collides with existing files, or a host refuses to activate it, see [Troubleshooting](TROUBLESHOOTING.md). Do not assume discovery or activation succeeded just because files were copied.
