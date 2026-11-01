"""Formative numerical checks, not a secure exam or a research-validity judgement."""
import json
import math

def _matches(actual, expected):
    if isinstance(expected, dict):
        return (isinstance(actual, dict) and set(actual) == set(expected)
                and all(_matches(actual[key], expected[key]) for key in expected))
    if isinstance(actual, bool) or not isinstance(actual, (int, float)):
        return False
    return math.isfinite(actual) and math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-8)

def run_checks(namespace, cases_json):
    results = []
    for case in json.loads(cases_json):
        function = namespace.get(case["function"])
        if not callable(function):
            passed, message = False, "請定義函式 " + case["function"] + "，並使用提供的參數。"
        else:
            try:
                actual = function(*case["args"])
                passed = _matches(actual, case["expected"])
                message = ("預期行為相符。" if passed else
                           "結果或單位不符。" + case["hint"] + " 函式內請保留完整精度。")
            except NotImplementedError:
                passed, message = False, "請替換 TODO 行，再執行與檢查。" + case["hint"]
            except Exception as exc:
                passed, message = False, type(exc).__name__ + ": " + str(exc)[:250] + ". " + case["hint"]
        results.append({"label": case["label"], "passed": passed, "message": message})
    return json.dumps(results)
