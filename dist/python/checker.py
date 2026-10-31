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
            passed, message = False, "Define the function " + case["function"] + " with the supplied arguments."
        else:
            try:
                actual = function(*case["args"])
                passed = _matches(actual, case["expected"])
                message = ("Expected behaviour matched." if passed else
                           "Result or units differ. " + case["hint"] + " Keep full precision inside functions.")
            except NotImplementedError:
                passed, message = False, "Replace the TODO line, then run and check again. " + case["hint"]
            except Exception as exc:
                passed, message = False, type(exc).__name__ + ": " + str(exc)[:250] + ". " + case["hint"]
        results.append({"label": case["label"], "passed": passed, "message": message})
    return json.dumps(results)
