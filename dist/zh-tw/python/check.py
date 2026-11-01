# -*- coding: utf-8 -*-
"""執行：python3 check.py ch1-allocation；或 python3 check.py all。"""
import argparse
import json
import runpy
from pathlib import Path
from checker import run_checks
here = Path(__file__).resolve().parent
spec = json.loads((here / "exercises.json").read_text(encoding="utf-8"))
parser = argparse.ArgumentParser(description="檢查儲存的學習程式；不會上傳程式碼。")
parser.add_argument("exercise", choices=[item["id"] for item in spec] + ["all"])
args = parser.parse_args()
selected = spec if args.exercise == "all" else [item for item in spec if item["id"] == args.exercise]
failed = False
for exercise in selected:
    try:
        namespace = runpy.run_path(str(here / (exercise["id"] + ".py")), run_name="__practice__")
        results = json.loads(run_checks(namespace, json.dumps(exercise["cases"])))
        print("\n" + exercise["id"] + " " + exercise["title"])
        for result in results:
            print(("通過" if result["passed"] else "重新檢查"), result["label"], "-", result["message"])
        passed = sum(result["passed"] for result in results)
        print(str(passed) + "/" + str(len(results)) + " 項數值檢查通過。請另外解釋結果與限制。")
        failed = failed or passed != len(results)
    except (SyntaxError, NameError, TypeError, ValueError) as exc:
        print(type(exc).__name__ + ": " + str(exc))
        print("檢查縮排、名稱與尚未替換的 None，再修改重試。")
        failed = True
raise SystemExit(1 if failed else 0)
