# Optional Python consolidation: Chapters 1–10

You can practise real Python in the course's Python workspace or run the same scripts locally. The browser route needs no installation or account. On first execution it downloads the pinned Pyodide runtime from jsDelivr; that provider receives ordinary asset requests. Learner code is executed on your device, not sent to a course execution server. Use the supplied classroom values, not personal data or credentials. Browser code can use Python/JavaScript network features if you add them yourself; the supplied scripts make no network calls.

## Your learning sequence

1. Predict an output and explain why before running your practice code.
2. Read and run the worked example. Notice the names, units and indentation.
3. Complete the TODO expressions in the starter script.
4. Run, explain an error, revise, and use **Check my script** on changed cases.
5. Change an input or assumption, predict again, and compare the output.
6. Save a short reflection: what changed, what you checked, and what the model leaves out.

All activities are formative. Numerical checks validate the supplied test cases, not all possible programs or the quality of a financial claim. Reference solutions are available separately after an explicit reveal. The learner ZIP includes starters and local check tools, not the complete reference solutions. Chapter 3 uses embedded teaching CSV text/rows so scripts run without uploading or fetching files. The first Chapter 1 percentage activity is a completed worked example, not an independent coding assessment.

## Browser route

Open `/python/` on the course site. Choose a chapter and activity. Run a worked example to see Python syntax, then edit the labelled code area. **Run my script** displays output. **Check my script** calls the supplied functions on several inputs. Errors have hints and a revision route. **Stop Python** terminates a busy worker; the next run starts a fresh runtime. Code and prose save locally on this browser. Export the learning record before changing devices; there is no import or cross-device sync.

Each execution has fresh Python variables. No variables carry over between activities or runs. Use named values in the script rather than `input()`. The browser runner does not install extra Python packages. It caps script length and console output and stops execution after five seconds; runtime loading has a separate one-minute limit. Browser memory is not a guaranteed hard quota. A failed download or worker does not prevent downloading and running the standard-library scripts locally.

## Local setup: Windows, macOS or Linux

Install Python 3 from [python.org](https://www.python.org/downloads/) if it is unavailable. These scripts use only the standard library and syntax compatible with Python 3.8+, tested locally on Python 3.8.2. A current supported Python release is recommended. No pip installation, API key, market-data subscription or broker account is needed.

After downloading and extracting the learner ZIP, open a terminal in the extracted folder:

```sh
python3 --version
python3 ch1-change.py
python3 check.py ch1-change
```

On Windows, use `py` instead of `python3` if that is your Python command:

```text
py ch1-change.py
py check.py ch1-change
```

Next open `ch1-allocation.py` in a text editor, replace the TODO expression, save, and run:

```sh
python3 ch1-allocation.py
python3 check.py ch1-allocation
```

Choose an activity ID from the workspace or the table below. Each `.py` file can run alone; `check.py`, `checker.py` and `exercises.json` should stay together for local checks. Python `*` multiplies, `/` divides and `**` raises to a power. Python `^` is not exponentiation. Lines beginning with `#` are comments. Indented lines belong to the function or loop above them. `return` sends a result back; `print` displays it.

## Activities and suggested extra time

| ID | Core concept | Type | Extra minutes |
|---|---|---|---:|
| ch1-change | Chapter 1 · readiness and percentage changes | Worked example | 10 |
| ch1-allocation | Chapter 1 · allocation lab | Guided practice | 15 |
| ch1-comparison | Chapter 1 · fair benchmarks, optional cost extension | Transfer challenge | 15 |
| ch2-return | Chapter 2 · measure a return | Guided practice | 10 |
| ch2-growth | Chapter 2 · compound over time | Guided practice | 15 |
| ch2-discount | Chapter 2 · present value and bonds | Guided practice | 15 |
| ch2-inflation | Chapter 2 · purchasing power | Guided practice | 10 |
| ch2-transfer | Chapter 2 · calculation card and reproducibility | Transfer challenge | 15 |
| ch3-order | Chapter 3 · chronological observations | Guided practice | 15 |
| ch3-audit | Chapter 3 · transparent quality audit | Guided practice | 20 |
| ch3-split | Chapter 3 · split-adjusted price returns | Transfer challenge | 15 |
| ch4-summary | Chapter 4 · observed frequency, centre and sample spread | Guided practice | 15 |
| ch4-quantile | Chapter 4 · sorted linear interpolation | Guided practice | 15 |
| ch4-correlation | Chapter 4 · Pearson correlation and undefined cases | Transfer challenge | 15 |
| ch5-risk | Chapter 5 · sample spread and observed drawdown | Guided practice | 20 |
| ch5-sharpe | Chapter 5 · monthly excess returns and Sharpe | Transfer challenge | 15 |
| ch6-weights | Chapter 6 · weighted return, constant mix and buy-and-hold | Guided practice | 20 |
| ch6-beta | Chapter 6 · sample beta and Pearson correlation | Transfer challenge | 15 |
| ch7-payoffs | Chapter7 · terminal payoff versus undiscounted profit | Guided practice | 15 |
| ch7-path | Chapter7 · compounding and fixed-generator simulation | Transfer challenge | 15 |
| ch8-timing | Chapter8 · trailing3-close signal | Guided practice | 15 |
| ch8-costs | Chapter8 · turnover fee before return | Transfer challenge | 15 |
| ch9-audit | Chapter 9 · chronological audit | Guided practice | 15 |
| ch9-trials | Chapter 9 · selection and trial retention | Transfer challenge | 20 |
| ch10-evidence | Chapter 10 · hand check and calculation attachment | Guided practice | 15 |
| ch10-ledger | Chapter 10 · rule, chronology, costs and same-date benchmark | Transfer challenge | 20 |

Allow another 10–15 minutes once for first-time Python setup. These are optional additions: about Chapter 1: 40 minutes, Chapter 2: 65 minutes, Chapter 3: 50 minutes, Chapter 4: 45 minutes, Chapter 5: 35 minutes, Chapter 6: 35 minutes, Chapter 7: 30 minutes, Chapter 8: 30 minutes, Chapter 9: 35 minutes, Chapter 10: 35 minutes, beyond the existing three-hour core chapter estimates. The original 30-hour core remains the noncoding path. A future timed pilot can determine which exercises can replace equivalent core practice without increasing total workload. These estimates are not learner-validated.

## Hypothetical data and conventions

Chapter 1 asset order is cash, bonds, shares. Weights are percentages adding to 100. Steady annual returns are 2%, 3%, 8%; stress returns are 1%, −5%, −20%. The baseline is 20/40/40. Start-of-year allocation is held for one year without rebalancing. The first lab has zero costs; the optional cost-repair script deducts one specified flat pound fee at year end from both comparisons. It does not model turnover, bid/ask spreads, borrowing or taxes.

Chapter 2 uses annual effective growth/discount rates, year-end cash flows, constant assumed inflation and no external deposits. Distributions in the total-return script are held to the period end, with no reinvestment return. Bond principal is included in the final scheduled payment. Keep full calculation precision and round only printed output. Growth, inflation and discounting are conditional teaching assumptions, not forecasts or claims of suitability. No historical data, random seed or train/test split applies to these deterministic arithmetic exercises.

Functions use the stated teaching domain: positive starting values, unleveraged returns, nonnegative cash receipts/fees, annual positive whole-year horizons and discount/inflation rates above −100%. They are learner exercises, not hardened financial production libraries. Their small supplied tests do not establish correctness on every input. Do not interpret a positive return or a passed check as proof of an investment strategy.

Chapter 3 adds original embedded CSV strings with ISO dates, split-only adjustments, conservative duplicate quarantine and transparent gaps. Split-adjusted price returns exclude dividends. Chapter 4 uses hypothetical monthly percentage returns, sample SD with n−1 in percentage points, and inclusive quantiles with h=(n−1)p; correlation preserves observation pairs and is undefined for constant inputs. These statistics describe a sample, not reliable forecasts.

## Reset, retention and troubleshooting

Browser answers, code, checks and reflections use a separate Python-practice storage key. Resetting Python practice does not reset the core chapter records. Resetting a script to its starter retains the attempt log but invalidates its current coding completion. A full practice reset removes the local Python record, not downloaded files. Deleting browser storage or private browsing may lose work. Local files remain until you remove them.

- `NotImplementedError`: replace the TODO line rather than deleting the function.
- `TypeError` involving `None`: a placeholder remains where a number is needed.
- `NameError`: check spelling, capitals and whether a name was defined.
- `IndentationError` or `SyntaxError`: check four-space indentation, parentheses, colons and quotation marks.
- Correct-looking printed text but failed checks: return numeric values from the named functions; do not just print a hard-coded answer. Keep percentages and decimals distinct.
- Download or runtime failure: retry with a network connection or use the ZIP and local Python. External runtime requests and local Python setup are separate from your financial reasoning.

## Sources and future chapters

Original tasks and scripts. Runtime design follows [Pyodide worker guidance](https://pyodide.org/en/stable/usage/webworker.html); Python syntax follows the [official Python tutorial](https://docs.python.org/3/tutorial/introduction.html). No third-party course questions or datasets are copied. The runtime has its own upstream licence; it is loaded from its official documented CDN, not redistributed in the learner ZIP.

Chapters 3–4 now add CSV inspection, cleaning and descriptive-statistics exercises. Chapters 5–10 now extend the script route to risk, portfolios, scenario simulation, payoff arithmetic, timing/cost checks and reproducible capstone evidence. Every activity has a starter, worked example, changed-input checks and reference solution. Numerical checks do not validate a research conclusion. The proposed 30-hour core excludes these additional coding activities.
