# Independent Chapter 3 review

Reviewer: Chapter4 author, independent of Chapter3 implementation. Actual artifacts inspected 31 October 2026: Chapter3 model, app, lessons, complete generated guide and its builder, dictionary, both data definitions/CSVs, tests, docs, and optional Python definitions. No Chapter3 production files were edited by this reviewer.

## Outcome

No release-blocking quantitative or curriculum issue found in the inspected version. This is approval for an owner-review learning prototype, not evidence of learner efficacy, complete assistive-technology conformance or commercial readiness. Parent release workflow owns browser verification and deployment.

## Quantitative and data evidence

- Independently checked audit conservation: seven original observations, three retained, four removed; removed counts decompose into two conflicting-date rows, one unknown and one redundant identical copy. Original rows are not mutated. Conflict quarantine is explicitly a conservative teaching choice, not universal financial-data advice.
- Verified chronological endpoint identity separately from the chapter test suite: adjusted LANTERN 52.02/50−1 = 4.04%; changed transfer 103.02/100−1 = 3.02%. Both equal compounded observed interval returns. Raw LANTERN first interval −49% is correctly distinguished from split-only adjusted +2%; split wealth uses one £102 share versus two £51 shares.
- Verified ISO date validation, unique chronological calculation requirements, missing/zero handling, raw versus split-only adjustment, dividend exclusion and non-daily interval labels. Synthetic dates and lack of expected trading calendar are disclosed. No market-performance or forecast claim found.
- All six supplied Chapter3 Node24 tests passed, covering audit classifications, changed data, invalid dates/prices/order, completion recovery/invalidation, two-column evidence, 180-minute pacing, and source/text-route contracts.
- All ten independently executed Chapter3 Python reference checks passed: three ordering/CSV cases, three audit cases, four split cases. Formulas use supplied inputs and public changed cases; no external packages. Python audit's single-basis missing-first policy is explicitly stated and is narrower than the two-price browser audit, avoiding a false equivalence.

## Learning and accessibility inspection

Core pacing totals 180 minutes and optional Python is separately 50 minutes plus setup. The chapter is self-contained with percentage bridge, data dictionary, original/transfer CSVs, worked examples, response-before-feedback tasks, targeted explanations and revision. Independent transfer changes dates/prices, enforces all five substantive questions, requires current submitted answers and a feedback response. Final card requires preceding evidence and self-review. Prose quality is explicitly self-reviewed rather than inferred from length or automated numerical checks.

The complete static guide includes every lesson, data, lab policy and computations, changed transfer, feedback keys, alternate changed-number exercise and card exemplar. It can run without JavaScript or Python. Source code provides fieldset/legend choice groups, labelled controls, table captions, focusable main, non-navigating skip link, live feedback, no time limit, separate local storage and reset, export and retention disclosures. Full screen-reader use was not performed by this reviewer.

## Revision recheck

Both nonblocking improvement suggestions were implemented and source-rechecked: saving assessment feedback now snapshots `latestAttempt.revision`, with a string validation during restore; the paper-guide builder now uses explicit column scopes and date row-header scopes, and its generated output was regenerated. No remaining finding from this review is open.

Billing and model-token telemetry were unavailable; review cost is unknown, not zero.
