# Troubleshooting

Use these checks in order. The installer only copies a static skill; an agent host controls discovery and activation.

| Symptom | Check | Smallest next step |
| --- | --- | --- |
| `undercut` does not appear in your agent | Host-supported skill directory and project root | Compare [host paths](INSTALLATION.md#host-paths) and reload the session if that host requires it |
| A duplicate skill appears | Shared `.agents/skills` and host-specific `.cursor/skills`, `.claude/skills`, etc. | Keep one canonical install for that host/project |
| `Target exists` | A prior install or custom folder at the destination | Inspect the folder; use `--verify` or back it up before `--force` |
| `--force` is refused | Existing folder does not identify itself as `name: undercut` or is a symlink | Do not force over unrelated content; choose the correct path |
| `--verify` fails | Local customization or outdated package | Diff against `skills/undercut/` and explicitly preserve wanted customizations |
| Symlink rejection | Destination's parent or target is a symlink | Install into a regular folder and avoid writing through unknown targets |
| Installer check fails | Missing `SKILL.md`, malformed manifest, or broken internal link | Run `python3 scripts/undercut.py check` and inspect the exact reported path |
| Agent ignores questions-first style | Skill not activated, tool doesn't support this format, or higher-priority instructions override it | Explicitly invoke `undercut`, check activation, and try a [behavioral evaluation](../evaluation/README.md) |
| Agent asks redundant questions | Repository facts or explicit answers already settle the branch | Ask it to cite the *material fork* and read the existing relevant contract before asking |
| Agent runs no tests | No verified command or agent lacks execution access | Request one focused reproduction/check; do not accept a fabricated "tested" claim |

## Safe diagnosis

```bash
python3 scripts/undercut.py check
python3 scripts/undercut.py install --agent codex --scope project --project /path/to/repo --dry-run
python3 scripts/undercut.py install --agent codex --scope project --project /path/to/repo --verify
python3 scripts/undercut.py install --help
```

Replace `codex` and `/path/to/repo` with the actual target. A successful installer command proves **file placement only**; it does not prove the agent used the skill.

## Reporting an issue

Include the host product and version, actual project directory, command and exit status, relevant error text, and whether the destination pre-existed. Strip personal paths and all credentials. For behavioral failures, attach a minimal redacted request/response and the expected question or boundary. See [Issue templates](../.github/ISSUE_TEMPLATE/bug_report.yml).
