"""Meaningful checks for the optional Python route; standard library only."""
import json
import math
import runpy
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "python"
SPEC = json.loads((OUT / "exercises.json").read_text(encoding="utf-8"))
CHECK = runpy.run_path(str(OUT / "checker.py"))["run_checks"]


class PythonPracticeTests(unittest.TestCase):
    def check_script(self, exercise, namespace):
        return json.loads(CHECK(namespace, json.dumps(exercise["cases"])))

    def test_references_pass_every_case_and_run_fresh(self):
        for exercise in SPEC:
            namespace = runpy.run_path(str(OUT / "reference" / (exercise["id"] + ".py")), run_name="__practice__")
            self.assertTrue(all(r["passed"] for r in self.check_script(exercise, namespace)), exercise["id"])
            self.assertEqual(self.check_script(exercise, namespace), self.check_script(exercise, namespace))

    def test_only_worked_example_starts_complete(self):
        for exercise in SPEC:
            namespace = runpy.run_path(str(OUT / "scripts" / (exercise["id"] + ".py")), run_name="__practice__")
            passed = all(r["passed"] for r in self.check_script(exercise, namespace))
            self.assertEqual(passed, exercise["id"] == "ch1-change", exercise["id"])

    def test_independent_hand_calculations_and_inflation_invariance(self):
        allocation = runpy.run_path(str(OUT / "reference/ch1-allocation.py"))["portfolio_return"]
        self.assertAlmostEqual(allocation([20, 40, 40], [1, -5, -20]), -9.8)
        self.assertAlmostEqual(allocation([50, 40, 10], [1, -5, -20]), -3.5)
        discount = runpy.run_path(str(OUT / "reference/ch2-discount.py"))["present_value"]
        self.assertAlmostEqual(discount([(1, 50), (2, 1050)], 5), 1000)
        summary = runpy.run_path(str(OUT / "reference/ch2-transfer.py"))["summarise"]
        a, b = summary(1000, 5, 3, 10, 2000), summary(1000, 5, 6, 10, 2000)
        self.assertAlmostEqual(a["real"], 1212.0505797930664)
        self.assertEqual(a["nominal"], b["nominal"])
        self.assertEqual(a["payment_pv"], b["payment_pv"])
        self.assertLess(b["real"], a["real"])

    def test_checker_catches_seeded_misconceptions(self):
        mutants = {
            "ch2-return": {"total_return": lambda start, end, distribution: (end - start) / start * 100},
            "ch2-growth": {"future_value": lambda p, r, y: p * (1 + r / 100 * y), "cagr": lambda s, e, y: (e / s - 1) / y * 100},
            "ch2-discount": {"present_value": lambda payments, r: sum(a for _, a in payments) / (1 + r / 100) ** max(y for y, _ in payments)},
            "ch2-inflation": {"real_return": lambda n, i: n - i, "buying_power": lambda n, i, y: n / (1 + i / 100 * y)},
        }
        for exercise in SPEC:
            if exercise["id"] in mutants:
                self.assertFalse(all(r["passed"] for r in self.check_script(exercise, mutants[exercise["id"]])), exercise["id"])
        case = SPEC[0]["cases"][0]
        for invalid in [True, float("nan"), None, "5"]:
            result = json.loads(CHECK({case["function"]: lambda *args: invalid}, json.dumps([case])))
            self.assertFalse(result[0]["passed"])

    def test_decimal_constant_correlation_is_undefined(self):
        report = runpy.run_path(str(OUT / "reference/ch4-correlation.py"))["paired_report"]
        for rows in [[[str(i), .3, .3] for i in range(12)],
                     [[str(i), .3, i] for i in range(12)],
                     [[str(i), i, .3] for i in range(12)]]:
            self.assertEqual(report(rows), {"defined": 0, "r": 0})
        small = [[str(i), .3 + i * 1e-8, .3 + i * 1e-8] for i in range(3)]
        self.assertEqual(report(small)["defined"], 1)
        self.assertAlmostEqual(report(small)["r"], 1)

    def test_learner_pack_is_self_contained_and_has_no_solutions(self):
        with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(OUT / "learner-pack.zip") as archive:
            self.assertNotIn("reference/", " ".join(archive.namelist()))
            archive.extractall(tmp)
            for exercise in SPEC:
                self.assertEqual((Path(tmp) / (exercise["id"] + ".py")).read_text(), exercise["starter"])
            worked = subprocess.run([sys.executable, "check.py", "ch1-change"], cwd=tmp, capture_output=True, text=True)
            incomplete = subprocess.run([sys.executable, "check.py", "ch1-allocation"], cwd=tmp, capture_output=True, text=True)
            self.assertEqual(worked.returncode, 0, worked.stderr)
            self.assertEqual(incomplete.returncode, 1, incomplete.stderr)
            self.assertIn("REVISIT", incomplete.stdout)


if __name__ == "__main__":
    unittest.main()
