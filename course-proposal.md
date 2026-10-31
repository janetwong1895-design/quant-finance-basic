# Quantitative Finance Foundations: Data, Risk and Investment Decisions

Version 0.1 · 31 October 2026 · Research-backed curriculum proposal

## Recommendation

Offer a 30-hour introduction for adults who want to interpret financial data and evaluate basic investment research. The course follows one question: **Does a simple investment rule provide convincing evidence of improvement over a reasonable benchmark, after risk and costs?**

Learners progress from compounding and data handling to risk measurement, diversification, simulation and a small, reproducible research report. The finish line is a defensible analysis; a decision that the evidence is insufficient is a successful outcome.

Assume English-language, asynchronous delivery over six weeks at five hours per week. The 30 hours include setup, required readings, practice, assessment and revision. These are design assumptions rather than confirmed preferences. A facilitated version could use ten sessions with three hours of learning per session; breaks would extend elapsed attendance time.

## Research and rationale

The following are curriculum benchmarks and research inputs, not evidence of demand or of this proposed course's effectiveness. Sources were checked on 31 October 2026.

| Source | Finding | Design implication |
|---|---|---|
| [Open University: Managing my investments](https://www.open.edu/openlearn/money-business/managing-my-investments/) | An introductory, 24-hour course covers investment choices, risk, historical performance and behavioural influences, without previous subject study. | A beginner offering can focus on investment interpretation. Our proposal adds structured quantitative practice and research evidence. |
| [CFA Institute: Investment Foundations](https://www.cfainstitute.org/programs/investment-foundations-certificate) | The current official page describes a foundational, self-paced programme with a 35–65-hour study estimate and broad industry coverage. | Thirty hours require selective scope. This proposal does not claim equivalent coverage or credential value. Older public flyers show different durations; the current programme page governs this comparison. |
| [MIT: Finance Theory I topic sequence](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/) | Topics include present value, fixed income, equities, derivatives, risk and return, and portfolios. | Use present value, risk and portfolios as foundations; include simple derivative payoffs, while reserving formal pricing for subsequent study. |
| [Bailey et al.: The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) | Repeated strategy selection can overfit backtests; familiar holdout methods have limitations in this setting. | Introduce trial logs, chronological evaluation and cautious conclusions. A held-out period is a teaching safeguard, not proof that overfitting has been eliminated. |
| [Investor.gov: Diversification](https://www.investor.gov/introduction-investing/getting-started/asset-allocation) and [fees](https://www.investor.gov/introduction-investing/getting-started/understanding-fees) | Diversification and fees affect investment outcomes; a narrowly focused fund need not be diversified. | Make portfolio comparisons and net-of-cost results core tasks. |
| [Iowa State: Bloom's taxonomy](https://celt.iastate.edu/prepare-and-teach/design-your-course/blooms-taxonomy/) and [CAST UDL](https://udlguidelines.cast.org/) | These provide frameworks for outcome alignment and flexible participation and expression. | Move from calculations to interpretation and justified evaluation; offer equivalent ways to produce evidence. These frameworks do not establish the effectiveness of this course. |

This is an introductory investment-research course within quantitative finance. Stochastic calculus, machine learning, formal portfolio optimisation, advanced derivatives pricing, live execution and specialist credit modelling belong in later courses.

## Audience, prerequisites and support

Target adults, early-career finance staff, students and career changers with basic arithmetic, percentages, simple algebra and ordinary computer skills. No finance qualification, calculus or prior programming is assumed. Python is introduced through small edits to prepared notebooks; this is not a standalone programming course.

The first module includes a 15-minute diagnostic covering percentages, weighted averages, chart reading, spreadsheet cells and file handling. Learners who need help take a 30-minute targeted bridge; others use the same slot for an extension. Both routes remain inside the 30-hour budget. A learner needing more extensive foundational support should be offered preparatory study with its additional time clearly disclosed.

Proposed support: a setup troubleshooting guide, module checklists, misconception feedback and a facilitator response target of two working days. Staffing and delivery of that service remain to be arranged. Required readings should be short extracts or original summaries, timed within the modules; external courses are references rather than mandatory extra study.

## Course learning outcomes

| ID | Observable performance and criterion | Bloom process / knowledge type |
|---|---|---|
| CLO-01 | Given a cash-flow table, calculate simple and compounded returns and present values; achieve at least 80% on a five-item check. | Apply / procedural |
| CLO-02 | Given a supplied dataset, produce an analysis-ready return table and identify all planted date, missing-value and price-adjustment defects. | Apply and analyse / procedural |
| CLO-03 | Calculate and interpret volatility, maximum drawdown, correlation and a clearly defined Sharpe ratio; reproduce reference values within stated rounding tolerance and explain two limitations. | Apply and analyse / conceptual and procedural |
| CLO-04 | Compare two supplied portfolio allocations over the same period and justify a risk/return trade-off, with a correct weighted-return calculation and two evidence-based observations. | Analyse / conceptual |
| CLO-05 | Evaluate a predefined strategy against a benchmark using chronological evaluation, explicit timing, costs and a trial log; satisfy every research-integrity checklist item. | Evaluate / procedural and metacognitive |
| CLO-06 | Produce a reproducible research memo with traceable results, justified conclusions and at least three material limitations; achieve at least 70% on the capstone rubric and pass integrity requirements. | Create / procedural and metacognitive |

## Syllabus: ten modules of three hours

Each row represents 180 minutes of total learner work. Every module has an original worked example, a prediction before seeing the result, guided practice, independent transfer and feedback followed by a learner correction. `OBJ-Mxx`, `ACT-Mxx` and `CHK-Mxx` are stable objective, activity and assessment identifiers; details below define their scope.

| Module / objective ID | Content and observable objective | Worked and guided activity | Independent transfer and evidence |
|---|---|---|---|
| M01 / OBJ-M01 | **Markets, decisions and setup.** Distinguish shares, bonds, cash and funds; state a testable investment question; open and reset the learning environment. | ACT-M01: inspect a hypothetical investor case, complete the diagnostic/bridge and load a supplied dataset. | CHK-M01: classify instruments, choose a benchmark and submit a research question with a setup confirmation. |
| M02 / OBJ-M02 | **Financial mathematics.** Calculate percentage changes, total return, compounding, annualised growth and present value; distinguish nominal and real returns. | ACT-M02: follow a £1,000 growth example and discount a simple bond cash-flow schedule. | CHK-M02: compare two cash-flow scenarios and correct an arithmetic-versus-geometric return error. |
| M03 / OBJ-M03 | **Financial data and tools.** Read a CSV, inspect dates, select columns, calculate returns and detect defects. Introduce notebook cells, variables and tables as needed. | ACT-M03: repair duplicate dates, missing prices and an adjusted/unadjusted price mismatch in a prepared example. | CHK-M03: repair a different small dataset and provide a provenance and cleaning note. |
| M04 / OBJ-M04 | **Probability and descriptive statistics.** Calculate mean, dispersion, quantiles and correlation; distinguish an estimate from a reliable forecast. | ACT-M04: use a small return sample and a visual resampling demonstration to compare sample estimates. | CHK-M04: interpret a new sample, explain correlation versus causation and describe estimation uncertainty. |
| M05 / OBJ-M05 | **Risk and performance.** Calculate volatility, drawdown and Sharpe ratio; compare growth and benchmark-relative performance. | ACT-M05: compare paths with similar ending values and different losses along the way. | CHK-M05: produce a one-page risk dashboard with units, frequency and two limitations. |
| M06 / OBJ-M06 | **Portfolio diversification.** Calculate weighted portfolio returns and compare correlation, rebalancing and concentration. Explain beta using a supplied plot. | ACT-M06: compare a single asset with a hypothetical two-asset portfolio and test a supplied rebalancing schedule. | CHK-M06: assess a different weight combination using the same dates and justify a trade-off. |
| M07 / OBJ-M07 | **Simulation and derivative intuition.** Interpret simulated outcomes and calculate simple forward and call-option payoffs and profits. | ACT-M07: run a prepared, seeded scenario model; contrast payoff with profit after the option premium. | CHK-M07: change one assumption, compare outcomes and explain why model outputs are conditional. No option-pricing derivation is assessed. |
| M08 / OBJ-M08 | **A transparent backtest.** Translate a supplied rule into positions and compare net returns with a benchmark. | ACT-M08: trace a moving-average rule from information to the next eligible execution point, then add turnover costs. | CHK-M08: reproduce the result on a second supplied dataset and submit an execution-timing diagram. |
| M09 / OBJ-M09 | **Research reliability.** Identify look-ahead bias, repeated testing, survivorship bias and sensitivity to costs or market period. | ACT-M09: audit a deliberately flawed strategy claim; document all supplied trials and inspect chronological results. | CHK-M09: repair the claim and submit a preregistered capstone analysis plan before seeing its evaluation segment. |
| M10 / OBJ-M10 | **Capstone and communication.** Execute the prepared analysis plan and write a concise research memo with reproducible evidence. | ACT-M10: annotate a sample memo and use a supplied notebook or equivalent calculation template. | CHK-M10: submit the memo, evidence and trial log; use rubric feedback to revise one weak claim. |

### Exact workload allocation

| Modules | Orientation / diagnostic / bridge | Explanation, worked example and prediction | Guided practice | Independent work / assessment | Feedback and revision | Total |
|---|---:|---:|---:|---:|---:|---:|
| M01 | 60 | 45 | 35 | 25 | 15 | 180 |
| M02–M09, each | 0 | 45 | 60 | 50 | 25 | 180 |
| M10 | 0 | 20 | 20 | 110 | 30 | 180 |
| **Course total** | **60** | **425** | **535** | **535** | **245** | **1,800 minutes / 30 hours** |

M01's orientation allocation includes 15 minutes for the diagnostic, 30 for the bridge or extension, and 15 for initial setup. Guided practice in later modules includes debugging and reset time. M09's planning task prepares M10, so the final project does not begin from an empty page. These timings require pilot validation; unusually long setup or revision needs should be recorded as a workload finding.

## Teaching and accessible participation

Use short explanations, small tables and visible calculations before introducing larger datasets. Begin each module with the practical decision it helps make. Gradually remove scaffolding and offer portfolio or trading examples where the same outcome can be assessed.

Provide two equivalent routes: prepared Python notebooks and a no-code calculation/interpretation pack with small tables, formulas and supplied outputs. Both require learners to perform selected calculations, record assumptions and justify decisions; reading a chart alone does not satisfy a calculation outcome. Independent transfer uses different data or assumptions. The certificate, if later offered, should describe quantitative-finance foundations rather than programming proficiency.

Plan keyboard-operable materials, descriptive chart text, underlying data tables, readable equations, non-colour-only distinctions and captions/transcripts for any audio or video. Target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/). Actual compliance and assistive-technology compatibility remain untested until materials exist.

## Assessment and alignment

| Evidence | Weight | Outcomes | Proposed proficiency rule |
|---|---:|---|---|
| A01: short checks from M01, M02, M04 and M07 | 20% | CLO-01, CLO-03 | At least 80% on the CLO-01 five-item check; feedback permits a correction. |
| A02: practical portfolio from M03, M05, M06, M08 and M09 | 40% | CLO-02–CLO-05 | Correct calculations and units; all planted data defects found; every timing/cost/trial-log integrity item resolved. |
| A03: capstone memo and evidence from M10 | 40% | CLO-03–CLO-06 | At least 70% on the rubric and all integrity requirements satisfied. |

Proposed course pass: at least 70% overall, the stated CLO-specific thresholds, and no unresolved critical data, timing or unsupported-claim defect. These are design criteria awaiting pilot calibration. Positive investment returns earn no marks by themselves. Mark the quality of the reasoning and evidence, including a supported decision to reject the strategy.

The capstone is a 600–800-word memo plus a compact calculation file or notebook. Learners ask: **Does the supplied rule improve the chosen risk/return trade-off over its benchmark after costs, and what remains uncertain?** Use one predefined rule and a small supplied set of sensitivity cases, not an open-ended search for the best parameters.

Capstone rubric: data provenance and reproducibility 20%; calculations and conventions 25%; timing, benchmark, costs and evaluation design 25%; evidence-based interpretation and limitations 20%; clarity and response to feedback 10%. A learner must correct future-data use, mismatched evaluation periods or an untraceable headline result before passing, regardless of total score.

### Alignment map

Rows map the module objectives, practice and assessed evidence. Minutes are attributed once per module to a primary outcome for accounting; modules can support several outcomes.

| CLO | Prerequisite | Objective IDs | Activity IDs | Evidence | Primary minutes |
|---|---|---|---|---|---:|
| CLO-01 | Percentages, simple algebra | OBJ-M01, OBJ-M02 | ACT-M01, ACT-M02 | CHK-M01, CHK-M02 / A01 | 360 |
| CLO-02 | CLO-01 basics; file handling | OBJ-M03 | ACT-M03 | CHK-M03 / A02 | 180 |
| CLO-03 | CLO-01–02 basics | OBJ-M04, OBJ-M05, OBJ-M07 | ACT-M04, ACT-M05, ACT-M07 | CHK-M04, CHK-M05, CHK-M07 / A01–A03 | 540 |
| CLO-04 | CLO-03 basics | OBJ-M06 | ACT-M06 | CHK-M06 / A02 | 180 |
| CLO-05 | CLO-02–04 | OBJ-M08, OBJ-M09 | ACT-M08, ACT-M09 | CHK-M08, CHK-M09 / A02–A03 | 360 |
| CLO-06 | CLO-01–05 | OBJ-M10 | ACT-M10 | CHK-M10 / A03 | 180 |
| **Total** | | | | | **1,800** |

## Planned lab and data contract

Use original synthetic datasets for the core course, with a documented generator, seed, scenario assumptions and clear synthetic labels. They support mechanics and reasoning, not claims of real market profitability. An optional historical extension requires a verified redistribution licence, snapshot date, corporate-action treatment and survivorship disclosure before inclusion. No live market feed is required.

Plan a browser-accessible notebook with a local fallback, pinned dependencies, a reset guide and learner starter files. Freeze and fresh-run test the actual environment during production. Maintain instructor solutions separately. Do not promise a free hosted service or unverified software version.

For introductory calculations, declare return frequency, annualisation factor, sample standard-deviation convention and risk-free-rate conversion. Volatility scaling uses an explicitly stated simplifying assumption. Define drawdown relative to a running peak and use matching dates and conventions for every comparison. Introduce a one-period hand calculation before an automated result.

For strategy examples, declare a chronological development/evaluation boundary, log every trial and withhold evaluation results until the rule is frozen. Define information availability and execution explicitly: a signal using a closing price cannot earn the return ending at that same close. If execution is at the next open, supply opening prices and calculate holdings and returns accordingly. Teach this timeline with a hand-worked example before relying on code.

Specify transaction costs per traded notional, turnover conventions, any slippage and benchmark costs. Label cash returns, taxes, borrowing and liquidity assumptions. Use no leverage or shorting in the core strategy. Include an unseen-future-data check, a cost arithmetic check and reproducibility checks when labs are built. A single evaluation period and synthetic data provide limited evidence; no inference of deployability follows.

## Production recommendation and status

Proceed to detailed authoring after the scope is accepted: build M01–M03 first to test beginner accessibility and timing, then M04–M09 and the capstone. Prepare original explanations, examples, starter files, independent exercises, feedback, instructor solutions and a facilitator guide. Use a small learner pilot to measure actual completion time, diagnostic suitability and error patterns before finalising the 30-hour claim.

This deliverable is a **curriculum proposal**. Learner lessons, runnable labs, answer keys and validated assessments have not been produced. Independent quantitative, accessibility and teaching reviews, followed by recorded revisions and fresh-run checks, are required before a pilot-ready package is claimed. Publication would additionally invoke the studio's review-and-release workflow. No learner outcomes, accreditation, commercial demand, data rights or release readiness are asserted.

Open decisions: intended audience segment; whether 30 hours means total study time or contact time; preferred delivery format; expected Python depth; facilitator availability; production budget; and any commercial destination. None prevents this proposal from being reviewed.
