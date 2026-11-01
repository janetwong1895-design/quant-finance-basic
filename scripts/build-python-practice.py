"""Build the standard-library-only optional Python practice assets."""
import json
import textwrap
import zipfile
import html
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "python"


def code(text):
    return textwrap.dedent(text).strip() + "\n"


def case(label, function, args, expected, hint):
    return dict(label=label, function=function, args=args, expected=expected, hint=hint)


EXERCISES = [
    dict(id="ch1-change", chapter=1, kind="Worked example", minutes=10,
         title="Turn a percentage into Python", concept="Chapter 1 · readiness and percentage changes",
         objective="Read variables, arithmetic and a function; explain a percentage relative to its starting value.",
         prediction="Predict the percentage change from £200 to £210 before running. Why is the denominator 200?",
         instructions="This first script is complete. Run it, inspect the named inputs and printed result, then change ending_value to 190 and predict the result. Restore the original example before checking.",
         syntax="= stores a value; # starts a comment; / divides; * multiplies. def names a reusable function. Four spaces indent its body. return sends a result back. print displays it. You call a function with values in parentheses.",
         hints=["The change is ending value minus starting value.", "Divide by the starting value, then multiply by 100. A lower ending value gives a negative change."],
         reflection="Explain the denominator and the effect of changing 210 to 190. Passing these checks only confirms the supplied function, not that you have written independent code.",
         starter=code('''
            # Hypothetical amounts; no deposits, withdrawals, fees or tax.
            def percentage_change(start, end):
                return (end - start) / start * 100

            if __name__ == "__main__":
                starting_value = 200
                ending_value = 210  # Try 190, predict, then run again.
                result = percentage_change(starting_value, ending_value)
                print("Percentage change:", result, "%")
         '''),
         solution=None,
         example=None,
         cases=[case("The supplied example", "percentage_change", [200, 210], 5, "Use change divided by starting value."),
                case("A falling value", "percentage_change", [200, 190], -5, "Keep the negative sign."),
                case("A new base", "percentage_change", [80, 100], 25, "Use 80, not 100, as the denominator.")]),
    dict(id="ch1-allocation", chapter=1, kind="Guided practice", minutes=15,
         title="Build a weighted portfolio return", concept="Chapter 1 · allocation lab",
         objective="Implement a weighted return and compare the fixed 20/40/40 baseline with another allocation.",
         prediction="Which returns do you expect for the 20/40/40 baseline and a 50/40/10 allocation in the stress scenario?",
         instructions="Replace the single TODO expression inside the loop. weights contains cash, bond and share percentages; returns_pct contains their one-year returns in the same order. Complete the expression, run, then check on several allocations.",
         syntax="A list groups values in square brackets. zip pairs items in order. for repeats the indented calculation for each pair. total += contribution adds to a running total. None is a placeholder here, not zero.",
         hints=["A 20% weight is 20 / 100, or 0.20.", "Each contribution is weight / 100 multiplied by that asset's return in percentage units."],
         reflection="Compare both allocations in steady and stress conditions using the earlier browser table. Explain a trade-off and one limitation of the invented data.",
         starter=code('''
            import math

            def portfolio_return(weights, returns_pct):
                if len(weights) != 3 or len(returns_pct) != 3:
                    raise ValueError("Supply three matching assets.")
                if any(w < 0 or w > 100 for w in weights):
                    raise ValueError("Each weight must be between 0 and 100.")
                if not math.isclose(sum(weights), 100):
                    raise ValueError("Weights must add to 100%.")
                total = 0
                for weight, asset_return in zip(weights, returns_pct):
                    contribution = None  # TODO: replace None with the weighted return.
                    total += contribution
                return total

            if __name__ == "__main__":
                stress = [1, -5, -20]  # Cash, bonds, shares: synthetic annual returns (%).
                print("Baseline stress return (%):", portfolio_return([20, 40, 40], stress))
                print("Alternative stress return (%):", portfolio_return([50, 40, 10], stress))
         '''),
         solution="contribution = weight / 100 * asset_return",
         replace="contribution = None  # TODO: replace None with the weighted return.",
         example=code('''
            # Worked calculation: the fixed baseline in the steady scenario.
            weights = [20, 40, 40]
            returns_pct = [2, 3, 8]
            total = 0
            for weight, asset_return in zip(weights, returns_pct):
                total += weight / 100 * asset_return
            print("Baseline steady return (%):", total)  # 4.8
         '''),
         cases=[case("Steady baseline", "portfolio_return", [[20, 40, 40], [2, 3, 8]], 4.8, "Use decimal weights but percentage-unit asset returns."),
                case("Stress baseline", "portfolio_return", [[20, 40, 40], [1, -5, -20]], -9.8, "Keep negative asset returns."),
                case("Alternative allocation", "portfolio_return", [[50, 40, 10], [1, -5, -20]], -3.5, "Use the function's inputs, not fixed weights."),
                case("All cash transfer", "portfolio_return", [[100, 0, 0], [1, -5, -20]], 1, "The two zero-weight holdings contribute zero.")]),
    dict(id="ch1-comparison", chapter=1, kind="Transfer challenge", minutes=15,
         title="Repair an omitted-cost comparison", concept="Chapter 1 · fair benchmarks, optional cost extension",
         objective="Calculate ending wealth after a flat fee and use the same convention for a comparison.",
         prediction="The browser's first lab assumes zero costs. What happens to a £1,000 balance earning 4.8% when a £5 fee is deducted at year end?",
         instructions="Write the ending_value function using its three inputs. This extension introduces a flat pound fee charged at the end of the year, after growth. Compare both portfolios using that same convention. It is not a full trading-cost or tax model.",
         syntax="Use parentheses to group 1 + return_pct / 100. Subtract a pound fee from a pound balance. Do not subtract a pound amount directly from a percentage.",
         hints=["First calculate the ending value before the fee.", "Multiply start by (1 + return_pct / 100), then subtract fee_gbp."],
         reflection="Explain why £5 is 0.5 percentage points of a £1,000 starting balance. State when the fee was charged and why both comparisons need the same timing.",
         starter=code('''
            def ending_value(start, return_pct, fee_gbp):
                # TODO: replace the next line with a calculation and return its result.
                raise NotImplementedError("Calculate growth, then deduct the end-year pound fee.")

            if __name__ == "__main__":
                print("Baseline after fee (£):", ending_value(1000, 4.8, 5))
                print("Alternative after fee (£):", ending_value(1000, 3.0, 5))
         '''),
         solution="return start * (1 + return_pct / 100) - fee_gbp",
         replace='raise NotImplementedError("Calculate growth, then deduct the end-year pound fee.")',
         example=code('''
            starting_pounds = 500
            return_pct = 2
            end_year_fee_pounds = 3
            gross_end = starting_pounds * (1 + return_pct / 100)
            print("Net ending pounds:", gross_end - end_year_fee_pounds)  # 507
         '''),
         cases=[case("Baseline with fee", "ending_value", [1000, 4.8, 5], 1043, "The fee is £5, not 5%."),
                case("Alternative with same fee", "ending_value", [1000, 3, 5], 1025, "Apply the same fee timing."),
                case("Stress loss plus fee", "ending_value", [1000, -9.8, 5], 897, "A fee increases a loss."),
                case("New starting amount", "ending_value", [500, 2, 3], 507, "Use all function arguments, not the example constants.")]),
    dict(id="ch2-return", chapter=2, kind="Guided practice", minutes=10,
         title="Include the distribution once", concept="Chapter 2 · measure a return",
         objective="Implement a total-return function and distinguish price gain from a cash distribution.",
         prediction="What total return comes from buying at £80, ending at £76 and receiving £2 in cash?",
         instructions="Replace the TODO line. The distribution is held as cash to the end, with no reinvestment return; there are no external deposits, fees or taxes. Return a percentage number such as 7, not a decimal 0.07.",
         syntax="Function arguments make the same formula reusable on new data. Keep full precision inside the function; rounding is only for printed presentation.",
         hints=["Net gain equals end minus start plus the distribution.", "Divide that net gain by start and multiply by 100."],
         reflection="Explain why the loss case remains negative. What would change if a supplied total-return series had already included distributions?",
         starter=code('''
            def total_return(start, end, distribution):
                # TODO: return the total return in percentage units.
                raise NotImplementedError("Include both the price change and the cash distribution.")

            if __name__ == "__main__":
                print("Total return (%):", total_return(80, 76, 2))
         '''),
         solution="return (end - start + distribution) / start * 100",
         replace='raise NotImplementedError("Include both the price change and the cash distribution.")',
         example=code('''
            start, end, distribution = 50, 52, 1
            gain = end - start + distribution
            print("Total return (%):", gain / start * 100)  # 6
         '''),
         cases=[case("Price plus distribution", "total_return", [100, 104, 3], 7, "Add the cash receipt once."),
                case("Loss partly offset", "total_return", [80, 76, 2], -2.5, "Use the starting £80 denominator."),
                case("New independent values", "total_return", [200, 210, 6], 8, "Do not hard-code the worked example.")]),
    dict(id="ch2-growth", chapter=2, kind="Guided practice", minutes=15,
         title="Compound and annualise", concept="Chapter 2 · compound over time",
         objective="Implement future value and CAGR, and diagnose adding successive returns.",
         prediction="Predict £500 growing at 8% for two years. Then predict the CAGR connecting £1,000 to £1,331 over three years.",
         instructions="Complete both functions. Rates use percentage units and years are whole positive annual periods. No external deposits or withdrawals. Change the worked script's return list from [20, -20] to [25, -20] and explain the difference.",
         syntax="Python uses ** for powers, not ^. For a square root use ** (1 / 2). Convert a percentage to a decimal with / 100, and a decimal return to a percentage with * 100.",
         hints=["Future value multiplies principal by the annual growth factor raised to years.", "CAGR is ((end / start) ** (1 / years) - 1) * 100."],
         reflection="Explain why multiplying yearly growth factors differs from adding returns. What information about the investment path does CAGR leave out?",
         starter=code('''
            def future_value(principal, rate_pct, years):
                raise NotImplementedError("TODO: compound the annual growth factor.")

            def cagr(start, end, years):
                raise NotImplementedError("TODO: find the equivalent annual percentage rate.")

            if __name__ == "__main__":
                print("Future value (£):", future_value(500, 8, 2))
                print("CAGR (%):", cagr(1000, 1331, 3))
         '''),
         replacements={'raise NotImplementedError("TODO: compound the annual growth factor.")': 'return principal * (1 + rate_pct / 100) ** years',
                       'raise NotImplementedError("TODO: find the equivalent annual percentage rate.")': 'return ((end / start) ** (1 / years) - 1) * 100'},
         example=code('''
            balance = 100
            returns_pct = [20, -20]
            for rate in returns_pct:
                balance *= 1 + rate / 100
            print("Ending balance (£):", balance)  # 96
            print("Cumulative return (%):", (balance / 100 - 1) * 100)  # -4
         '''),
         cases=[case("Two-year compounding", "future_value", [500, 8, 2], 583.2, "Use ** for powers; do not multiply rate by years."),
                case("Three-year transfer", "future_value", [800, 4, 3], 899.8912, "Keep full precision until printing."),
                case("Annualising growth", "cagr", [1000, 1331, 3], 10, "Take the cube root of the ending-to-starting ratio."),
                case("Annualising a loss", "cagr", [100, 81, 2], -10, "A loss can have a negative CAGR.")]),
    dict(id="ch2-discount", chapter=2, kind="Guided practice", minutes=15,
         title="Discount each dated payment", concept="Chapter 2 · present value and bonds",
         objective="Translate a dated cash-flow schedule into a reproducible present-value calculation.",
         prediction="What is the time-0 value of a £20 payment in year 1 plus £1,020 in year 2, discounted at 5%?",
         instructions="payments is a list of (year, pounds) pairs. Complete one expression inside the loop. The final bond payment already includes principal. Use one supplied annual effective discount rate, with no default, fees or tax.",
         syntax="for year, amount in payments unpacks each pair into names. Each payment has its own power. Add the discounted values, not the undated cash amounts.",
         hints=["Convert rate_pct to a decimal before forming the denominator.", "The term is amount / (1 + rate_pct / 100) ** year."],
         reflection="Explain why one exponent cannot discount the entire bond schedule correctly. Why must you avoid adding principal twice?",
         starter=code('''
            def present_value(payments, rate_pct):
                total = 0
                for year, amount in payments:
                    discounted = None  # TODO: discount this payment using its year.
                    total += discounted
                return total

            if __name__ == "__main__":
                bond = [(1, 20), (2, 1020)]
                print("Present value (£):", round(present_value(bond, 5), 2))
         '''),
         solution="discounted = amount / (1 + rate_pct / 100) ** year",
         replace="discounted = None  # TODO: discount this payment using its year.",
         example=code('''
            future_payment = 1210
            discount_rate = 10 / 100
            years = 2
            print("Present value (£):", future_payment / (1 + discount_rate) ** years)  # 1000
         '''),
         cases=[case("Two bond payments", "present_value", [[(1, 20), (2, 1020)], 5], 944.2176870748299, "Discount each dated payment before summing."),
                case("A single payment", "present_value", [[(3, 926.1)], 5], 800, "Use the supplied payment year."),
                case("Different coupon and rate", "present_value", [[(1, 30), (2, 1030)], 4], 981.1390532544378, "The final amount already includes principal."),
                case("Zero-rate comparison", "present_value", [[(1, 50), (2, 1050)], 0], 1100, "At zero discount rate, sum the cash payments.")]),
    dict(id="ch2-inflation", chapter=2, kind="Guided practice", minutes=10,
         title="Calculate exact real returns", concept="Chapter 2 · purchasing power",
         objective="Use ratios for real returns and compound inflation to deflate a nominal balance.",
         prediction="Can a 3% nominal gain produce a loss of buying power when inflation is 5%? Predict the sign before running.",
         instructions="Complete both TODO lines. Both rates cover the same period. buying_power deflates an already computed nominal balance over whole years. It is not investment-rate discounting.",
         syntax="Group both growth factors with parentheses. Return a real percentage from real_return and a pound amount from buying_power. Names carry units, which helps prevent mixing them.",
         hints=["Real return is a ratio of one plus nominal return to one plus inflation, minus one.", "Deflate the nominal balance by (1 + inflation_pct / 100) ** years."],
         reflection="Distinguish nominal pounds, starting-year buying power and the PV of a future payment. Explain why subtracting rates is only an approximation.",
         starter=code('''
            def real_return(nominal_pct, inflation_pct):
                raise NotImplementedError("TODO: return the exact real percentage.")

            def buying_power(nominal_balance, inflation_pct, years):
                raise NotImplementedError("TODO: return starting-year purchasing power in pounds.")

            if __name__ == "__main__":
                print("Real return (%):", real_return(3, 5))
                print("Buying power (£):", round(buying_power(1030, 5, 1), 2))
         '''),
         replacements={'raise NotImplementedError("TODO: return the exact real percentage.")': 'return ((1 + nominal_pct / 100) / (1 + inflation_pct / 100) - 1) * 100',
                       'raise NotImplementedError("TODO: return starting-year purchasing power in pounds.")': 'return nominal_balance / (1 + inflation_pct / 100) ** years'},
         example=code('''
            nominal_pct, inflation_pct = 6, 4
            real_pct = ((1 + nominal_pct / 100) / (1 + inflation_pct / 100) - 1) * 100
            print("Exact real return (%):", round(real_pct, 2))  # 1.92, not exactly 2
         '''),
         cases=[case("Exact ratio", "real_return", [6, 4], 1.9230769230769162, "Subtraction is only an approximation."),
                case("Negative real return", "real_return", [3, 5], -1.904761904761909, "Keep the negative sign."),
                case("One-year buying power", "buying_power", [1030, 5, 1], 980.952380952381, "The result is pounds, not a percentage."),
                case("Multi-year transfer", "buying_power", [1210, 10, 2], 1000, "Compound the inflation factor over both years.")]),
    dict(id="ch2-transfer", chapter=2, kind="Transfer challenge", minutes=15,
         title="Reproduce and critique the growth lab", concept="Chapter 2 · calculation card and reproducibility",
         objective="Build a small report that keeps nominal growth, real value and discounting distinct.",
         prediction="If only inflation rises from 3% to 6%, which outputs change? Predict nominal end, buying power and the PV of the separate payment.",
         instructions="Complete three formulas in summarise. Return a dictionary with the specified keys. Use the inputs, not constants from the example. The separate future payment is discounted at growth_pct as an illustrative opportunity rate; it is not the portfolio balance.",
         syntax="A dictionary pairs text keys with values: {\"nominal\": nominal}. It gives units and meanings a stable label. Keep calculations unrounded; round only when printing the report.",
         hints=["Compute nominal = principal * (1 + growth_pct / 100) ** years.", "Deflate nominal using inflation; discount the separate payment using growth_pct. These are different operations."],
         reflection="Report a hand check and an inflation-only comparison. State one model limitation and one specific revision to your initial prediction. Explain why tests are evidence of code behaviour, not proof of an investment claim.",
         starter=code('''
            def summarise(principal, growth_pct, inflation_pct, years, future_payment):
                nominal = None  # TODO: compound the principal.
                real = None  # TODO: express nominal balance in starting-year pounds.
                payment_pv = None  # TODO: discount the separate future payment.
                return {"nominal": nominal, "real": real, "payment_pv": payment_pv}

            if __name__ == "__main__":
                for inflation in [3, 6]:
                    result = summarise(1000, 5, inflation, 10, 2000)
                    print("Inflation scenario (%):", inflation)
                    for label, amount in result.items():
                        print(label, "(pounds):", round(amount, 2))
         '''),
         replacements={'nominal = None  # TODO: compound the principal.': 'nominal = principal * (1 + growth_pct / 100) ** years',
                       'real = None  # TODO: express nominal balance in starting-year pounds.': 'real = nominal / (1 + inflation_pct / 100) ** years',
                       'payment_pv = None  # TODO: discount the separate future payment.': 'payment_pv = future_payment / (1 + growth_pct / 100) ** years'},
         example=code('''
            # Dictionary syntax before building your report.
            report = {"nominal": 1100, "real": 1000}
            for label, amount in report.items():
                print(label, "(pounds):", amount)
         '''),
         cases=[case("Default lab", "summarise", [1000, 5, 3, 10, 2000], {"nominal": 1628.894626777442, "real": 1212.0505797930664, "payment_pv": 1227.8265070815182}, "Use different rates for deflating and discounting."),
                case("Change only inflation", "summarise", [1000, 5, 6, 10, 2000], {"nominal": 1628.894626777442, "real": 909.566251737624, "payment_pv": 1227.8265070815182}, "Only the real balance should change."),
                case("New principal, rate and horizon", "summarise", [500, 10, 0, 2, 1210], {"nominal": 605, "real": 605, "payment_pv": 1000}, "Use each function argument rather than the default values.")])
]


CHECKER = code('''
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
''')

LOCAL_CHECK = code('''
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
''')


def build():
    # Chapter-specific source definitions keep authoring and review independent.
    all_exercises = list(EXERCISES)
    for chapter in range(3, 11):
        module = ROOT / "scripts" / ("python_chapter_%02d.py" % chapter)
        if module.exists():
            all_exercises.extend(runpy.run_path(str(module))["EXERCISES"])
    for folder in [OUT / "scripts", OUT / "reference", ROOT / "instructor" / "python"]:
        folder.mkdir(parents=True, exist_ok=True)
    public = []
    for source in all_exercises:
        item = dict(source)
        solution = item["starter"]
        substitutions = item.pop("replacements", {})
        if item.pop("solution", None):
            substitutions[item["replace"]] = source["solution"]
        item.pop("replace", None)
        for old, new in substitutions.items():
            solution = solution.replace(old, new)
        if item["example"] is None:
            item["example"] = item["starter"]
        public.append(item)
        (OUT / "scripts" / (item["id"] + ".py")).write_text(item["starter"], encoding="utf-8")
        (OUT / "reference" / (item["id"] + ".py")).write_text(solution, encoding="utf-8")
        (ROOT / "instructor" / "python" / (item["id"] + "-solution.py")).write_text(solution, encoding="utf-8")
    (OUT / "exercises.json").write_text(json.dumps(public, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "checker.py").write_text(CHECKER, encoding="utf-8")
    (OUT / "check.py").write_text(LOCAL_CHECK, encoding="utf-8")
    readme = (ROOT / "docs" / "python-practice.md").read_text(encoding="utf-8")
    with zipfile.ZipFile(OUT / "learner-pack.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("README.md", readme)
        archive.writestr("checker.py", CHECKER)
        archive.writestr("check.py", LOCAL_CHECK)
        archive.writestr("exercises.json", json.dumps(public, ensure_ascii=False, indent=2))
        for item in public:
            archive.writestr(item["id"] + ".py", item["starter"])
    guide = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Python practice: complete text and local route</title><link rel="stylesheet" href="../styles.css?v=20261101"><link rel="stylesheet" href="practice.css"><style>body{max-width:880px;margin:auto;padding:35px 25px}h1{font-size:3rem}section{margin:35px 0}</style></head><body><a href="index.html">← Interactive Python workspace</a><h1>Consolidate the idea in Python.</h1><p>Optional additions for Chapters 1–10: predict, read, run, explain, modify, check and critique. No instructor response is required. This text route uses the same scripts and checks on local Python; it has no JavaScript dependency. The core chapters also remain available without Python.</p><h2>Setup and retention</h2><p>Download and extract the <a href="learner-pack.zip">learner pack</a>. It includes the chapter starters, check.py, checker.py and exercises.json. Install Python 3 from <a href="https://www.python.org/downloads/">python.org</a> if necessary. No pip packages or keys are needed. Scripts use Python 3.8+ syntax and are locally tested on 3.8.2; choose a currently supported Python release for new installations.</p><p>Open a terminal in the extracted folder. On macOS/Linux run the commands below; on Windows use py in place of python3 if appropriate.</p><pre class="code-block">python3 --version\npython3 ch1-change.py\npython3 check.py ch1-change</pre><p>Then edit ch1-allocation.py, replace the TODO expression, save, run it and check it with python3 check.py ch1-allocation. Keep the check tools and exercises.json in the same folder. Keep notes on paper or in a local document. The text/local route does not synchronise with browser progress; retain your own script revisions, outputs and reflection.</p><h2>Syntax bridge and troubleshooting</h2><p>= stores a value, # begins a comment, * multiplies, / divides and ** raises to a power. ^ is not exponentiation. Four spaces indent function and loop bodies. return sends a value back; print shows it. A function uses named inputs so the calculation works on changed cases. Keep precision inside functions; round only displayed values.</p><p>NotImplementedError means a TODO remains. A TypeError involving None usually means a missing calculation. NameError points to an undefined or misspelled name. For SyntaxError or IndentationError, check spaces, parentheses, colons and quotes. Failed numerical checks give targeted method hints. Revise and try again; a printed hard-coded answer does not implement a reusable function.</p><h2>Time, criteria and assumptions</h2><p>Suggested extra time: Additional Python time is shown for each activity and chapter in the workspace and learner-pack README. Allow 10–15 minutes once for setup. These optional additions are beyond the 30-hour noncoding core. Timings are unvalidated. For each task, predict first, attempt the code, check every supplied numerical case, and write a correction/check and limitation. Confidence is optional and ungraded. These checks do not certify financial reasoning, independent coding proficiency or a credential.</p><p>All data and rates are hypothetical. Chapter 1 uses one annual holding period and cash/bond/share order. The first lab has zero costs; the optional cost extension charges a flat pound fee at year end consistently to both portfolios. Chapter 2 uses annual effective rates, year-end payments, no external deposits and no fees/taxes. Distributions are held in cash to period end. Bond principal appears once in the final payment. No live prices, forecast claims, broker connections or personal inputs are required.</p>'''
    for item in public:
        escape = html.escape
        guide += '<section><h2>' + escape(item["id"] + ': ' + item["title"]) + '</h2>'
        for label, key in [('Objective', 'objective'), ('Predict', 'prediction'), ('Task', 'instructions'), ('Python syntax', 'syntax')]:
            guide += '<p><strong>' + label + ':</strong> ' + escape(item[key]) + '</p>'
        guide += '<h3>Worked example</h3><pre class="code-block">' + escape(item['example']) + '</pre>'
        guide += '<h3>Starter script</h3><pre class="code-block">' + escape(item['starter']) + '</pre>'
        guide += '<p><a href="scripts/' + item['id'] + '.py" download>Download starter .py</a></p><h3>Hints</h3><ol>'
        guide += ''.join('<li>' + escape(hint) + '</li>' for hint in item['hints']) + '</ol>'
        guide += '<p>Run <code>python3 check.py ' + item['id'] + '</code>. It checks: ' + escape(', '.join(case['label'] for case in item['cases'])) + '.</p>'
        guide += '<p><strong>Explain and revise:</strong> ' + escape(item['reflection']) + '</p>'
        guide += '<p>After trying and revising, <a href="reference/' + item['id'] + '.py">compare with the reference solution</a>. Reference viewing is a learning aid, not evidence of independent authorship.</p></section>'
    guide += '<section><h2>Browser alternative and privacy</h2><p>The interactive workspace runs Pyodide 314.0.7 in a device-local worker, loaded on demand from jsDelivr. The runtime provider receives ordinary asset requests; the supplied scripts do not upload code to a course execution server. Use classroom data. Added code can use network features if you write them yourself. The browser saves scripts, predictions, feedback, reflections and attempts locally; resets are separate from core chapter records. Exports have no import/sync. Keep downloaded files until you choose to delete them.</p><p>Browser loading has a one-minute limit; execution has five seconds, capped output and a Stop control. These are responsiveness limits, not a guaranteed memory sandbox. Downloaded scripts need a local Python installation. Learner pilot, full assistive-technology testing and commercial release validation remain pending.</p><p>Optional references: <a href="https://docs.python.org/3/tutorial/introduction.html">official Python syntax tutorial</a>; <a href="https://pyodide.org/en/stable/usage/webworker.html">Pyodide worker documentation</a>. All ten chapters have optional Python activities, with additional time shown per activity.</p></section></body></html>'
    (OUT / "guide.html").write_text(guide, encoding="utf-8")
    print("Built", len(public), "Python activities, starter scripts, reference scripts and learner pack.")


if __name__ == "__main__":
    build()
