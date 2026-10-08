import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("evaluation_validator", ROOT / "evaluations/tools/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.rows, self.digest = validator.validate_pack(ROOT / "evaluations/prompts.jsonl")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def write_rows(self, rows, name="cases.jsonl"):
        path = self.directory / name
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        return path

    def test_pack_coverage(self):
        self.assertEqual(len(self.rows), 24)
        self.assertEqual(len(self.digest), 64)
        self.assertEqual({r['expected_or_rubric']['type'] for r in self.rows}, {'exact_text', 'json', 'checklist'})

    def test_missing_case_rejected(self):
        with self.assertRaises(ValueError):
            validator.validate_pack(self.write_rows(self.rows[:-1]))

    def test_duplicate_case_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[1]['id'] = rows[0]['id']
        with self.assertRaises(ValueError):
            validator.validate_pack(self.write_rows(rows))

    def test_invented_grading_mode_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['expected_or_rubric']['type'] = 'invented'
        with self.assertRaises(ValueError):
            validator.validate_pack(self.write_rows(rows))

    def test_duplicate_json_key_rejected(self):
        path = self.directory / 'invalid.jsonl'
        path.write_text('{"id": "one", "id": "two"}\n')
        with self.assertRaises(ValueError):
            validator.read_jsonl(path)

    def test_nonstandard_json_constant_rejected(self):
        path = self.directory / 'invalid.jsonl'
        path.write_text('{"value": NaN}\n')
        with self.assertRaises(ValueError):
            validator.read_jsonl(path)

    def test_blank_run_not_mistaken_for_results(self):
        _, responses = validator.init_run(self.directory / 'run', self.rows, self.digest)
        counts = validator.check_responses(responses, self.rows)
        self.assertEqual(dict(counts), {'not_run': 24})
        rows, _ = validator.read_jsonl(responses)
        self.assertTrue(all(r['raw_output'] is None and r['grading'] is None for r in rows))

    def test_run_refuses_overwrite(self):
        target = self.directory / 'run'
        validator.init_run(target, self.rows, self.digest)
        before = (target / 'responses.jsonl').read_bytes()
        with self.assertRaises(ValueError):
            validator.init_run(target, self.rows, self.digest)
        self.assertEqual((target / 'responses.jsonl').read_bytes(), before)

    def test_completed_null_rejected(self):
        _, responses = validator.init_run(self.directory / 'run', self.rows, self.digest)
        rows, _ = validator.read_jsonl(responses)
        rows[0]['status'] = 'completed'
        with self.assertRaises(ValueError):
            validator.check_responses(self.write_rows(rows, 'responses.jsonl'), self.rows)

    def test_inconsistent_pass_rejected(self):
        _, responses = validator.init_run(self.directory / 'run', self.rows, self.digest)
        rows, _ = validator.read_jsonl(responses)
        rows[0].update(status='completed', raw_output='Synthetic test fixture', grading={
            'outcome': 'pass', 'reviewer': 'test fixture',
            'checks': {'comparison': 'fail'}, 'notes': 'Contradiction for validator test only.'})
        with self.assertRaises(ValueError):
            validator.check_responses(self.write_rows(rows, 'responses.jsonl'), self.rows)

    def test_empty_completed_answer_is_actual_attempt(self):
        _, responses = validator.init_run(self.directory / 'run', self.rows, self.digest)
        rows, _ = validator.read_jsonl(responses)
        rows[0]['status'] = 'completed'
        rows[0]['raw_output'] = ''
        counts = validator.check_responses(self.write_rows(rows, 'responses.jsonl'), self.rows)
        self.assertEqual(counts['completed'], 1)


if __name__ == '__main__':
    unittest.main()
