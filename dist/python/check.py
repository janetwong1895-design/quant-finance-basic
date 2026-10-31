"""Run: python3 check.py ch1-allocation (or use py on Windows)."""
import argparse
import json
import runpy
from pathlib import Path
from checker import run_checks

here = Path(__file__).resolve().parent
spec = json.loads((here / "exercises.json").read_text(encoding="utf-8"))
parser = argparse.ArgumentParser(description="Check one saved learner script.")
parser.add_argument("exercise", choices=[item["id"] for item in spec])
args = parser.parse_args()
exercise = next(item for item in spec if item["id"] == args.exercise)
try:
    namespace = runpy.run_path(str(here / (exercise["id"] + ".py")), run_name="__practice__")
    results = json.loads(run_checks(namespace, json.dumps(exercise["cases"])))
    for result in results:
        print(("PASS" if result["passed"] else "REVISIT"), result["label"], "-", result["message"])
    passed = sum(result["passed"] for result in results)
    print(str(passed) + "/" + str(len(results)) + " numerical checks passed. Explain and critique your result too.")
    raise SystemExit(0 if passed == len(results) else 1)
except (SyntaxError, NameError, TypeError) as exc:
    print(type(exc).__name__ + ": " + str(exc))
    print("Check indentation, names and remaining None placeholders; then revise and retry.")
    raise SystemExit(1)
