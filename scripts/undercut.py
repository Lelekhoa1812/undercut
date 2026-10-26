#!/usr/bin/env python3
"""Undercut: validate, install and bundle a self-contained Agent Skill.

Python standard library only. No network access, credential reads, or project edits.
"""
from __future__ import annotations

import argparse
import filecmp
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "undercut"
TARGETS = {
    "codex": (".agents", ".agents"),
    "claude": (".claude", ".claude"),
    "cursor": (".cursor", ".cursor"),
    "copilot": (".github", ".copilot"),
    "gemini": (".gemini", ".gemini"),
}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class PackError(Exception):
    """A user-actionable package or install error."""


def validate_skill(path: Path = SKILL) -> list[str]:
    """Return errors rather than throwing for ordinary content problems."""
    errors: list[str] = []
    entry = path / "SKILL.md"
    if not entry.is_file() or entry.is_symlink():
        return [f"Missing or symlinked SKILL.md: {entry}"]
    try:
        content = entry.read_text(encoding="utf-8")
    except (UnicodeError, OSError) as exc:
        return [f"Cannot read SKILL.md: {exc}"]
    lines = content.splitlines()
    if len(lines) > 500:
        errors.append(f"SKILL.md should stay <=500 lines; found {len(lines)}")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        errors.append("SKILL.md requires YAML frontmatter between --- delimiters")
    else:
        end = lines[1:].index("---") + 1
        fields: dict[str, str] = {}
        for line in lines[1:end]:
            match = re.match(r"^([\w-]+):\s*(.*)$", line)
            if match:
                fields[match[1]] = match[2].strip().strip('"\'')
        name, description = fields.get("name", ""), fields.get("description", "")
        if name != path.name or len(name) > 64 or not NAME_PATTERN.fullmatch(name):
            errors.append(f"frontmatter name must be '{path.name}' (lowercase-hyphen syntax)")
        if not description or len(description) > 1024:
            errors.append("frontmatter description must contain 1..1024 characters")
    for member in sorted(path.rglob("*")):
        if member.is_symlink():
            errors.append(f"symlink in skill: {member.relative_to(path)}")
            continue
        if member.is_dir():
            continue
        if not member.is_file():
            errors.append(f"unsupported special file: {member.relative_to(path)}")
            continue
        if member.stat().st_size > 512_000:
            errors.append(f"oversized file: {member.relative_to(path)}")
        if member.suffix.lower() not in (".md", ".txt", ".json", ".py", ".sh"):
            errors.append(f"unexpected binary or extension: {member.relative_to(path)}")
        try:
            data = member.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"not readable UTF-8: {member.relative_to(path)}")
            continue
        if member.suffix == ".md":
            for raw in MARKDOWN_LINK.findall(data):
                target = raw.split("#", 1)[0].split("?", 1)[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if target.startswith("/"):
                    errors.append(f"absolute link in {member.relative_to(path)}: {raw}")
                    continue
                resolved = (member.parent / target).resolve()
                if not resolved.is_relative_to(path.resolve()):
                    errors.append(f"link escapes skill root in {member.relative_to(path)}: {raw}")
                elif not resolved.is_file():
                    errors.append(f"broken link in {member.relative_to(path)}: {raw}")
    return errors



def validate_repository_links(root: Path = ROOT) -> list[str]:
    """Check internal relative links in all Markdown docs, not just SKILL.md."""
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "dist", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            errors.append(f"Unreadable markdown {path.relative_to(root)}: {exc}")
            continue
        for raw in MARKDOWN_LINK.findall(content):
            dest = unquote(raw.split("#", 1)[0].split("?", 1)[0].strip())
            if not dest or dest.startswith(("http://", "https://", "mailto:")):
                continue
            if dest.startswith("/"):
                errors.append(f"Absolute internal link in {path.relative_to(root)}: {raw}")
                continue
            target = (path.parent / dest).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f"Broken or escaping repository link in {path.relative_to(root)}: {raw}")
    return errors


def location(base: Path, agent: str, scope: str = "project") -> Path:
    project_path, user_path = TARGETS[agent]
    return base / (user_path if scope == "user" else project_path) / "skills" / "undercut"


def reject_symlink_segments(base: Path, target: Path) -> None:
    """Do not write through symlinked skill roots or an existing skill symlink."""
    current = base
    for part in target.relative_to(base).parts:
        current = current / part
        if current.is_symlink():
            raise PackError(f"Refusing symlink in install destination: {current}")


def is_existing_undercut(target: Path) -> bool:
    manifest = target / "SKILL.md"
    if not manifest.is_file() or manifest.is_symlink():
        return False
    try:
        return re.search(r"(?m)^name:\s*undercut\s*$", manifest.read_text("utf-8")) is not None
    except (UnicodeError, OSError):
        return False


def installation_matches(source: Path, target: Path) -> bool:
    if not target.is_dir() or target.is_symlink():
        return False
    source_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    target_files = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
    if source_files != target_files:
        return False
    return all(filecmp.cmp(source / file, target / file, shallow=False) for file in source_files)


def install_one(target: Path, force: bool) -> None:
    """Stage copy before changing destination; restore old package on swap error."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staged = Path(tempfile.mkdtemp(prefix=".undercut-stage-", dir=target.parent))
    backup: Path | None = None
    try:
        shutil.rmtree(staged)
        shutil.copytree(SKILL, staged)
        if target.exists():
            if not force or not is_existing_undercut(target):
                raise PackError(f"Target exists, not replaced: {target}")
            backup = Path(tempfile.mkdtemp(prefix=".undercut-backup-", dir=target.parent))
            backup.rmdir()
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup is not None and not target.exists():
                backup.rename(target)
                backup = None
            raise
        if backup is not None:
            shutil.rmtree(backup)
    finally:
        if staged.exists():
            shutil.rmtree(staged)


def run_install(args: argparse.Namespace) -> None:
    errors = validate_skill()
    if errors:
        raise PackError("Invalid source package:\n" + "\n".join(errors))
    if args.scope == "user" and args.project is not None:
        raise PackError("--project is only valid with --scope project")
    base = (Path.home() if args.scope == "user" else Path(args.project or Path.cwd())).resolve()
    if not base.is_dir():
        raise PackError(f"Project/user directory does not exist: {base}")
    agents = list(TARGETS) if args.agent == "all" else [args.agent]
    destinations = [location(base, agent, args.scope) for agent in agents]
    if args.verify and args.dry_run:
        raise PackError("--verify cannot be combined with --dry-run")
    # Preflight *every* target to avoid a partial install on predictable failure.
    for target in destinations:
        reject_symlink_segments(base, target)
        if not args.verify and target.exists() and (not args.force or not is_existing_undercut(target)):
            raise PackError(f"Target exists (use --force only for an Undercut install): {target}")
    for target in destinations:
        if args.verify:
            if not installation_matches(SKILL, target):
                raise PackError(f"Installed skill is missing or differs: {target}")
            print(f"verified install -> {target}")
        elif args.dry_run:
            print(f"would install -> {target}")
        else:
            install_one(target, args.force)
            print(f"installed -> {target}")


def run_bundle(args: argparse.Namespace) -> None:
    errors = validate_skill()
    if errors:
        raise PackError("Invalid skill package:\n" + "\n".join(errors))
    output = Path(args.output).resolve()
    if output.is_dir():
        raise PackError(f"Output must be a zip file, not directory: {output}")
    if output.suffix.lower() != ".zip":
        raise PackError("Bundle output must have a .zip extension")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                info = zipfile.ZipInfo("undercut/" + path.relative_to(SKILL).as_posix())
                info.date_time = (2026, 1, 1, 0, 0, 0)
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes())
    print(f"bundle -> {output}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install or validate the Undercut Agent Skill")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate SKILL metadata and internal resource links")
    install = commands.add_parser("install", help="copy the skill to a host discovery path")
    install.add_argument("--agent", required=True, choices=[*TARGETS, "all"])
    install.add_argument("--scope", choices=["project", "user"], default="project")
    install.add_argument("--project", help="target project directory; defaults to current directory")
    install.add_argument("--dry-run", action="store_true", help="preview without creating directories")
    install.add_argument("--force", action="store_true", help="replace a verified existing Undercut install")
    install.add_argument("--verify", action="store_true", help="check that installed bytes match this package without writing")
    bundle = commands.add_parser("bundle", help="produce a portable skill-folder ZIP")
    bundle.add_argument("--output", default="dist/undercut-skill.zip")
    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            errors = validate_skill() + validate_repository_links()
            if errors:
                raise PackError("\n".join(errors))
            print("PASS: skill manifest, UTF-8 resources and repository-relative links")
        elif args.command == "install":
            run_install(args)
        else:
            run_bundle(args)
    except (PackError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
