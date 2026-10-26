"""The evaluation catalog must stay usable; this is NOT an LLM behaviour test."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluate_cases", ROOT / "scripts" / "evaluate_cases.py")
assert SPEC is not None and SPEC.loader is not None
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class EvaluationCatalogTests(unittest.TestCase):
    def test_catalog_is_structurally_valid(self):
        self.assertEqual(MOD.validate_cases(), [])

    def test_duplicate_case_id_rejected(self):
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cases.json"
            case = {
                "id": "duplicate", "kind": "safety", "situation": "one", "user_prompt": "two",
                "question_expected": True, "ideal_behavior": "three", "failure_signals": ["four"],
            }
            path.write_text(json.dumps([case, case]), encoding="utf-8")
            errors = MOD.validate_cases(path)
            self.assertTrue(any("duplicate" in err for err in errors), errors)

    def test_explicit_questions_cover_both_directions(self):
        import json
        cases = json.loads(MOD.CASES.read_text(encoding="utf-8"))
        self.assertTrue(any(c["question_expected"] for c in cases))
        self.assertTrue(any(not c["question_expected"] for c in cases))


if __name__ == "__main__":
    unittest.main()
