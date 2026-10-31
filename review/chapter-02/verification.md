# Chapter 2 verification and release record

Version 1.0.0 · 31 October 2026 · Owner-private review prototype

## Scope and manifest

The existing private course Site is extended at `/chapter-02/`, preserving its audience and Chapter 1 storage. The original checkout directory remains `chapter-01/`; it now contains both chapters.

| Artifact | Role |
|---|---|
| dist/chapter-02/index.html, chapter.css | Learner page shell and responsive styling |
| dist/chapter-02/lessons.mjs | Original explanations, worked examples, prediction and reflection prompts, sources |
| dist/chapter-02/model.mjs | Finance calculations, practice items, independent cases and state validation |
| dist/chapter-02/app.js | Browser activities, feedback, completion rules, local saving and exports |
| dist/chapter-02/guide.html | Complete text/paper route with precomputed tables and both assessment cases |
| scripts/build-chapter-02-guide.mjs | Reproducible static guide generation |
| tests/chapter-02.test.mjs | Eight meaningful calculation/state/scoring checks |
| instructor/chapter-02/assessment-guide.md | Outcome alignment, criteria, answer references and calibration |
| review/chapter-02/ | Independent findings, corrections and actual verification |
| dist/index.html, dist/app.js | Chapter 1 links to Chapter 2 |

All instructor/review documentation is outside the served static directory. Numerical answer data are necessarily present in client assets for formative self-checking; this is not a secure examination or a credential.

## Design and data contract

Audience: adult beginners, basic percentages and calculator skills, no programming. Chapter 2 can be completed independently. English asynchronous delivery with a complete no-script text/paper route. Proposed timings: 10 + 25 + 25 + 30 + 25 + 35 + 20 + 10 = 180 minutes. This adapts the course proposal's M02 to a standalone self-learning path. Timings have not been validated by a learner pilot.

Activity IDs r1/r2, c1/c2/c3, p1/p2 and i1/i2 map to CH2-01–04. Independent items a1–a8 and the lab/calculation card assess preparation toward CLO-01 and CLO-06. All nine numerical practice tasks must be corrected, with a specific method/limit reflection per lesson. Independent pass requires 7/8 including a3, a7, a8, followed by a feedback response. Text minimums are disclosed completeness checks; prose quality is self-reviewed.

All asset prices, cash flows, rates and scenario inputs are original hypothetical examples. No historical, live or personal financial data are used. Deterministic formulas mean no random seed, tuning or chronological train/test split is applicable. Cash-flow dates, reinvestment, annual effective rates and zero cost/tax assumptions are stated. The lab caps inputs for resource control and generates at most 41 annual rows per run. It has no external cash deposits, volatility, default, borrowing or broker connections. Only inflation changes in the controlled comparison; all runs are kept. Future cash-flow PV and inflation-adjusted buying power are explicitly distinguished.

The lesson has no third-party runtime packages, fonts or analytics. Browser localStorage key `qf-studio-chapter-02-v1` is distinct from Chapter 1. A full Chapter 2 reset is explicitly scoped; exports do not support import or sync. Hosting may retain access logs.

## Executed checks

- Fourteen Node 24 tests passed across both chapters: eight Chapter 2 and six Chapter 1 regression tests. Tests cover total return, compounding, CAGR, dated discounting, exact real return, controlled inflation invariance, invalid values/bounds, both assessment cases, evidence invalidation and malformed saved-state recovery.
- Independent quantitative reviewer recomputed answer keys, headline examples, endpoint cases and state-hardening edge cases; independent curriculum reviewer inspected the actual lessons, paper route, assessment and pacing claims. Both completed rechecks. See the separate review files for exact hashes and limits.
- Actual browser walkthrough reached all eight completed steps. It included a wrong price-only return and targeted correction, all nine numerical lesson checks, lesson reflections and self-review criteria.
- Lab rejected fractional years, then recorded two runs differing only in inflation. Correct displayed nominal £1,628.89, purchasing power £1,212.05 at 3% inflation and £909.57 at 6%, simple interest £1,500, separate payment PV £1,227.83. Latest hand calculation and reflection were saved.
- Independent case A with 7/8 but the cumulative-return critical item wrong did not pass. Correcting that answer, resubmitting and saving a response passed. Editing another answer invalidated completion and prevented an old response from reusing the stale grade. Resubmission restored it.
- Final calculation card reached 8/8. Editing it immediately changed both sidebar and final checklist to incomplete; saving again restored completion. Reload preserved evidence and completion.
- Actual chapter selector returned to Chapter 1 with its existing local QA record intact; the new Chapter 1 link returned to Chapter 2 with its 8/8 record intact. Hosted learner records were not altered during this local QA.
- Keyboard activation of Reset inputs focused the principal field. Keyboard activation of Skip to lesson focused the main lesson without changing its content.
- A narrow-screen lab check reported document width 375 CSS pixels matching viewport width 375, with chart and tables present and no document-level horizontal overflow. Temporary viewport override was reset.
- Text route had 15 open disclosures, no closed disclosures and three data tables; all provided annual data and explanations are present in the default text view. Explicit currency rounding verified. Physical print output was not separately tested.
- JSON/CSV export controls were exercised and the app announced export initiation. File completion/content on disk was not verified in this run; an attempted read found no completed JSON at the expected Downloads path. No claim of actual downloaded-file verification is made.
- Browser error log query returned no errors in the tested session. This is a scoped observation, not a cross-browser guarantee.

## Findings and corrections

| ID | Finding | Correction / verification |
|---|---|---|
| C2-CUR-01 | Paper lab added substantial transcription/calculation burden | Provide annual tables and ask endpoints plus one intermediate check; independently rechecked |
| C2-CUR-02 | Static default buying-power typo | Correct to £1,212.05 in UI, source templates and assessor guide; rebuild and independently verify |
| C2-CUR-03/04 | Rounding and paper-table print visibility | State currency precision; emit all text-route disclosures open by default; independently rechecked |
| QA2-01 | Malformed same-version storage could crash a view | Validate field types/quiz set, run/attempt/card shapes; recompute outputs/scores; regression and independent edge checks passed |
| QA2-02 | Final completion summary stale after editing card | Update the summary during persistence without replacing inputs; source recheck and actual browser edit test passed |

No unresolved major/blocker was reported within the reviewers' scope. Prototype publication for owner review does not mean pilot-ready or commercially release-ready status.

## Remaining verification limits

No real learner pilot, validated 180-minute workload, manual screen-reader session, full keyboard-only end-to-end completion, comprehensive contrast/zoom audit, blocked-storage browser test, reset/deletion browser test, actual download completion or cross-browser matrix. No WCAG conformance or educational-effectiveness claim. Consequential assessment would need secure delivery, expert grading and an appeal route. Chapter 3 remains planned, not included.

## Sources and rights

Original lesson text, code, tables, examples and synthetic input values. General concepts were checked against official Investor.gov compound-interest tools, OpenStax time-value-of-money materials and Bank of England purchasing-power guidance on 31 October 2026. Links are in the learner source sections; no third-party dataset, course questions, media or text excerpts are redistributed. Optional external reading is not required for completion.

## Cost checkpoint: plan → author → review → revise → verify → package

Existing-session model/tool/agent usage and billed amounts are not exposed. Generation, two independent reviews and rechecks are recorded as performed, with financial cost unknown rather than zero. Exact billable model/tier, token counts, tool charges, known priced subtotal, budget headroom and forecast to completion cannot be calculated. Course/step caps remain unset. No separate paid API model benchmark or paid market-data job was launched.

The current chat/model was retained without claiming price optimality. Local deterministic tests dispatch no additional model requests, but machine time, hosting, subscription allocation, labour and tax are not priced. This is not a cost-certified production run; subsequent budgeted automated model dispatch requires approved caps, rate evidence, bounded forecasts and usage telemetry. No pricing snapshot was used to invent a session bill.
