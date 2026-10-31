# Independent artifact review: Chapters 7–8

Reviewer: `/root/build_ch56`, author of Chapters 5–6, not of Chapters 7–8. Review date: 31 October 2026. Scope: actual chapter models, apps, lessons, index/privacy text, static-guide generators and generated guides, CSV/data dictionaries, Python definitions and chapter tests. Root owns browser QA and release integration. This source/arithmetic review is not a human pilot, full assistive-technology audit or a proficiency validation.

## Findings and author revision

| ID | Severity | Evidence and implication | Resolution and independent recheck |
|---|---|---|---|
| R78-01 | Medium | Both initial `q()` helpers omitted `type:'choice'`; although `check()` had an exact-choice branch, discrete answers such as 2.01 passed for choice 2. This weakened the specified discrete critical-convention evidence. | Author supplied explicit choice IDs in both models and added regressions. Independently checked every declared choice accepts its exact answer and rejects answer+.01. Resolved. |
| R78-02 | Low | Chapter 8 Run and lab binding converted an explicitly cleared cost input with `Number('')`, silently treating it as zero. A cleared required field could therefore stand in for the selected experimental input. | Author rejects trim-empty before UI Number conversion and in shared live/restored `labEvidence`; explicit `'0'` remains valid. Added regression passes. Source checked and chapter tests independently rerun. Resolved. |
| R78-03 | Low | Copied interface feedback said “all four critical conventions” although Chapter 8 has six critical assessment questions, and saved-card feedback called the result a statistics card. | Changed to “all critical conventions” and “Evidence card”; source rechecked. Resolved. |

No unresolved high or medium finding was identified in this review. That is bounded to the inspected prototype artifacts and checks below.

## Quantitative and learning evidence inspected

- Chapter 7 forward payoff retains negative values; call payoff floors at zero and excludes premium; undiscounted call profit subtracts the supplied premium once. The no-financing/discounting convention and absence of a pricing claim are explicit. Cases below strike, above strike but loss-making, and break-even are covered.
- Three-period compounding, discrete equal-probability independent-return assumptions, exact 32-bit LCG mapping and path ordering are declared. Same-seed spread comparison preserves draw signs and changes magnitudes. Seed42 gives terminal81 at spread10 and64 at spread20. All 100 paths are accessible as a table and CSV. Conditional outcomes are explicitly distinguished from forecasts, calibrated probabilities and worst-case guarantees.
- Chapter 8 signal uses trailing three closes through t; executes at open t+1 and earns open t+1→t+2. Warm-up and last eligible interval are explicit. Rule/tie behavior, cash0%, no leverage/shorting, original positive synthetic prices, absent corporate actions, weekend teaching-session labels and the exposed transfer set are disclosed.
- Costs are turnover times bps/10000, charged before the holding return, including entry and final liquidation. A 1→0 exit costs wealth before cash earns zero. Matched buy-and-hold uses the same eligible opens, initial wealth, entry and exit cost convention. First development row independently agrees with1000×.999×100/103. Benchmark agrees with1000×.999×108/103×.999. Transfer strategy final903.127352687409 and benchmark941.5103773584904 were independently checked against the executable ledger.
- Tests perturb future prices and preserve earlier positions; fixed-path higher costs do not improve terminal strategy/benchmark wealth. Flat-price benchmark still pays both sides. Neither these tests nor exposed synthetic transfers are represented as external strategy validation.
- Both 180-minute cores include setup, worked concepts, numerical guided checks, prediction-before-run lab, changed-input comparison, latest hand check, independent transfer, feedback response and final card. Optional Python is explicitly additional30minutes. Prose is self-reviewed, not automatically graded. All numerical attempts and runs are retained; no favourable outcome is needed for completion.
- Static routes contain explanations, source/dictionary links, original tables, prepared two-run evidence, hand-check feedback, independent questions/keys and revision criteria. They distinguish paper records from local browser progress. Runtime apps use labeled fields and semantic status feedback, focus the lesson on skip activation, preserve hand verification through prose edits, and share current-evidence validators for save and restore. Root must validate actual rendered keyboard/mobile behavior.
- Malformed field/done/checked/run/attempt states reset safely; stale stored completion flags do not restore without evidence. A changed prediction/input cannot keep lab completion. Separate storage keys, chapter-only reset, record-only exports and no personal account data are described.

## Reproduction and results

Executed independently after author fixes:

```sh
node --test tests/chapter-07.test.mjs tests/chapter-08.test.mjs
node --check dist/chapter-07/app.js
node --check dist/chapter-08/app.js
```

Result: all8 chapter Node tests pass; both app syntax checks pass. Additional direct assertions cover exact declared choices, malformed/stale restoration and transfer terminal arithmetic. Actual shared `dist/python/checker.py` was used with all replacement-generated reference solutions for `ch7-payoffs`, `ch7-path`, `ch8-timing`, `ch8-costs`: all14 reference cases pass under local Python3.8.2. These runs establish the stated examples, not exhaustive correctness.

Primary methods cited in learner artifacts include USACE Monte Carlo workflow, Options Industry Council long-call mechanics, MIT derivative teaching sequence, Bailey et al. repeated-trial risk and Investor.gov fee effects. Their links support method/context; original data and learner explanations are authored material, with no copied long quotations or claim that these sources validate this course.

Release recommendation: suitable for owner-review prototype integration after root browser/package checks. Learner pacing, educational effectiveness and full assistive-technology compatibility remain unverified. Actual model usage/cost telemetry is unavailable; no numeric cost or free-review claim is made.
