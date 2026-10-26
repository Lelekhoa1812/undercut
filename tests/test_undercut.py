"""Focused tests of the repository's package tooling; no external packages."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "undercut.py"
SPEC = importlib.util.spec_from_file_location("undercut_cli", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ValidationTests(unittest.TestCase):
    def test_real_skill_passes(self):
        self.assertEqual(MOD.validate_skill(), [])

    def test_missing_skill_detected(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertTrue(any("Missing" in err for err in MOD.validate_skill(Path(td))))

    def test_broken_link_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "undercut"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: undercut\ndescription: test\n---\n[Missing](references/nope.md)\n", encoding="utf-8"
            )
            errors = MOD.validate_skill(root)
            self.assertTrue(any("broken link" in err for err in errors), errors)

    def test_escape_link_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "undercut"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: undercut\ndescription: test\n---\n[Bad](../secret.txt)\n", encoding="utf-8"
            )
            errors = MOD.validate_skill(root)
            self.assertTrue(any("escapes skill root" in err for err in errors), errors)

    def test_name_mismatch_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "undercut"
            root.mkdir()
            (root / "SKILL.md").write_text("---\nname: other\ndescription: test\n---\n", encoding="utf-8")
            self.assertTrue(any("name must" in e for e in MOD.validate_skill(root)))


class CommandTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], cwd=ROOT, text=True, capture_output=True)

    def test_user_copilot_target_is_not_project_github_path(self):
        self.assertEqual(MOD.location(Path("/tmp/root"), "copilot", "user"), Path("/tmp/root/.copilot/skills/undercut"))
        self.assertEqual(MOD.location(Path("/tmp/root"), "copilot", "project"), Path("/tmp/root/.github/skills/undercut"))

    def test_check_command(self):
        result = self.run_cli("check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_install_codex(self):
        with tempfile.TemporaryDirectory() as td:
            result = self.run_cli("install", "--agent", "codex", "--project", td)
            self.assertEqual(result.returncode, 0, result.stderr)
            target = Path(td) / ".agents" / "skills" / "undercut"
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertTrue((target / "references" / "clarification.md").is_file())
            self.assertEqual(MOD.validate_skill(target), [])

    def test_install_all(self):
        with tempfile.TemporaryDirectory() as td:
            result = self.run_cli("install", "--agent", "all", "--project", td)
            self.assertEqual(result.returncode, 0, result.stderr)
            for parent in (".agents", ".claude", ".cursor", ".github", ".gemini"):
                self.assertTrue((Path(td) / parent / "skills" / "undercut" / "SKILL.md").is_file())

    def test_verify_detects_content_drift(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(self.run_cli("install", "--agent", "gemini", "--project", td).returncode, 0)
            self.assertEqual(self.run_cli("install", "--agent", "gemini", "--project", td, "--verify").returncode, 0)
            target = Path(td) / ".gemini" / "skills" / "undercut" / "SKILL.md"
            target.write_text("altered", encoding="utf-8")
            result = self.run_cli("install", "--agent", "gemini", "--project", td, "--verify")
            self.assertNotEqual(result.returncode, 0)

    def test_existing_not_overwritten(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(self.run_cli("install", "--agent", "claude", "--project", td).returncode, 0)
            target = Path(td) / ".claude" / "skills" / "undercut"
            (target / "my-notes.txt").write_text("retain this", encoding="utf-8")
            result = self.run_cli("install", "--agent", "claude", "--project", td)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((target / "my-notes.txt").read_text(), "retain this")

    def test_force_replaces_recognized_undercut(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(self.run_cli("install", "--agent", "cursor", "--project", td).returncode, 0)
            target = Path(td) / ".cursor" / "skills" / "undercut"
            (target / "obsolete.txt").write_text("old", encoding="utf-8")
            result = self.run_cli("install", "--agent", "cursor", "--project", td, "--force")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((target / "obsolete.txt").exists())

    def test_force_does_not_replace_nonundercut(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / ".agents" / "skills" / "undercut"
            target.mkdir(parents=True)
            (target / "SKILL.md").write_text("---\nname: other\ndescription: x\n---\n", encoding="utf-8")
            result = self.run_cli("install", "--agent", "codex", "--project", td, "--force")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("name: other", (target / "SKILL.md").read_text())

    def test_all_preflight_no_partial_install(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / ".cursor" / "skills" / "undercut"
            target.mkdir(parents=True)
            (target / "KEEP.txt").write_text("do not touch", encoding="utf-8")
            result = self.run_cli("install", "--agent", "all", "--project", td)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((Path(td) / ".agents").exists())
            self.assertFalse((Path(td) / ".claude").exists())

    def test_dry_run_no_changes(self):
        with tempfile.TemporaryDirectory() as td:
            result = self.run_cli("install", "--agent", "all", "--project", td, "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("would install", result.stdout)
            self.assertEqual(list(Path(td).iterdir()), [])

    def test_reject_symlink_in_destination(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            (Path(td) / ".agents").symlink_to(outside, target_is_directory=True)
            result = self.run_cli("install", "--agent", "codex", "--project", td)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("symlink", result.stderr)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_zip_contains_only_skill_under_one_root(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "pack.zip"
            result = self.run_cli("bundle", "--output", path)
            self.assertEqual(result.returncode, 0, result.stderr)
            with zipfile.ZipFile(path) as archive:
                files = archive.namelist()
                self.assertIn("undercut/SKILL.md", files)
                self.assertIn("undercut/references/risk-boundaries.md", files)
                self.assertNotIn("README.md", files)
                self.assertTrue(all(s.startswith("undercut/") for s in files))


if __name__ == "__main__":
    unittest.main()
