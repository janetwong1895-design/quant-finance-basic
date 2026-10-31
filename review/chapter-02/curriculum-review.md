# Chapter 2 independent curriculum and assessment review

Reviewer: delegated curriculum/assessment agent, independent of authoring. Date: 31 October 2026. Candidate version: model VERSION 1.0.0. Scope: actual `chapter-01/dist/chapter-02/` learner app, complete guide, `chapter-01/instructor/chapter-02/assessment-guide.md`, Chapter 1 links in `dist/index.html` and `dist/app.js`, course brief, studio production contract and review protocol. This is a private owner-review prototype. Browser/keyboard QA belongs to the root reviewer. No learner pilot, assistive-technology test or human scoring reliability was performed or inferred.

Initial artifact hashes: app.js `7b8c7982a077db76050518037c3f05176f889db45d980c199f5adef85d9a335b`; model.mjs `4696fb3fc152f959c42a0bcbec4b6044e4425aecf4a3f0579c4c4b5dabf0a797`; lessons.mjs `1ad8535657e06c47db7fd05b723b3f11d9b6172c545a7e639cd`; guide.html `464bc053e728e5fcd9dadba7ebba953f8c0d51f3bc44dc68c395cf9d5e322b90`.

## Findings

| ID | Severity | Artifact/location and evidence | Learner consequence | Correction and acceptance check | Owner / fix / retest |
|---|---|---|---|---|---|
| C2-CUR-01 | Major | `guide.html`, Paper growth lab, step 3 asks learners to make a year-by-year table for years 0–10 using the same formulas after calculating both inflation scenarios. The browser supplies these data automatically; the paper lab retains the same 35-minute allowance. | The alternative route adds dozens of repetitive computations for a novice, creating materially different workload and effort rather than equivalent interpretation evidence. No timing evidence supports this additional demand. | Supply complete static annual tables for the fixed scenarios. Require the same endpoint calculation and one independent annual check as the browser, then compare nominal value, real value and PV. Verify all table numbers and ensure the guide no longer requires manually generating the entire table. | Root author / revised candidate / see recheck below |
| C2-CUR-02 | Major | `app.js`, start hero and calculation-card exemplar; `guide.html`, lab feedback/card exemplar; instructor guide, lab default/exemplar. All state £1,212.55 buying power for £1,000 growing at 5% for 10 years with 3% inflation. Independent calculation is `1000 × 1.05^10 ÷ 1.03^10 = 1212.0505797930664`, or **£1,212.05**. `growthScenario` calculates the correct value. | A learner's correct model or calculator output conflicts with the worked text and assessor exemplar. The lesson's insistence on pennies makes this a core evidence defect. | Correct every source/template and regenerated artifact to £1,212.05. Search the chapter authoring tree for stale `1,212.55`/`1212.55`, and compare default runtime output, guide feedback, start hero and card exemplar to the independent formula. | Root author / revised candidate / see recheck below |
| C2-CUR-03 | Minor | `app.js`, independent-check criteria say “Round to two decimals where requested”; numeric currency questions do not individually request rounding, though checking expects tolerance ±£0.011. Practice gives clearer explicit currency guidance. | A novice entering a whole-pound rounded estimate may be rejected without understanding the expected precision at the assessment point. | State “Round all pound amounts and percentages to two decimal places; extra precision is accepted” in browser and paper assessment instructions. Confirm two-decimal answers pass both cases. | Root author / revised candidate / see recheck below |

## Alignment and review evidence

- CH2-01 is prepared by price-versus-total-return worked text and r1/r2, with a1 and reflection evidence. Distribution timing and double counting are explained.
- CH2-02 is prepared by separate FV, changing-return and CAGR examples, practised in c1/c2/c3, and assessed by a2/a3/a4. Arithmetic mean and forecast limitations are explicit.
- CH2-03 is prepared by dated bond payments and reverse compounding, practised in p1/p2, and assessed by a5/a6. Principal and timing are treated consistently.
- CH2-04 is prepared by exact real-rate and deflation examples, practised in i1/i2, and assessed by a7 plus lab comparison. The independent case tests the real rate; purchasing-power calculation evidence comes from practice and the lab rather than a separate independent item.
- CH2-05 is supported by conditional-claim a8, prediction, run log and calculation card. Prose is explicitly self-reviewed; character counts are disclosed as completeness checks. No claim of expert validation or secure/accredited assessment is made.
- Feedback uses a method hint, later worked explanation, required correction/check response and two declared fixed cases. Critical a3/a7/a8 criteria prevent passing by missing the main conceptual errors. Unlimited revision suits the formative purpose.
- Proposed step allocations total exactly 180 minutes. Timings are explicitly unvalidated; the paper-route imbalance in C2-CUR-01 must be addressed before treating the routes as comparable.
- Source code contains the Chapter 1 navigation link and completion link to `chapter-02/`; Chapter 2 return paths point back to Chapter 1. Link interaction/deployment verification is reserved for root browser QA.
- Seven existing model tests passed under `node --test chapter-01/tests/chapter-02.test.mjs`. Those tests do not verify prose examples. Separate calculator expressions confirmed default nominal £1,628.89, real value at 3% £1,212.05, real value at 6% £909.57, future-payment PV £1,227.83, bond case A £981.41, bond case B £981.14 and lump-sum PV case B £1,333.49.
- No separate paid benchmark or billing telemetry was available to this reviewer. Existing-session review effort is unpriced, not zero-cost evidence.

Initial disposition: candidate with two major findings awaiting correction and targeted re-review. See the final recheck below.


## Independent recheck, revised candidate

Reinspected current generated learner assets, model, guide builder and assessor guide after author revision. Original findings describe the earlier inspected snapshot; they are not claims that the revised files still contain the same defects.

- **C2-CUR-01 resolved at source/content level:** the paper lab now supplies both annual tables and explicitly says learners need not transcribe or recompute every row. It asks endpoint calculations, one intermediate-year check, a nominal hand check and the comparison. Table generation uses the same declared model as the app. Proposed timing still requires a real beginner pilot.
- **C2-CUR-02 resolved:** current app, generated guide, builder and instructor guide consistently use £1,212.05. No stale £1,212.55/1212.55 remains in these inspected authoring/learner files. Independent formula remains £1,212.0505797930664 before rounding.
- **C2-CUR-03 partially resolved, remaining minor:** browser assessment now explicitly requires all pound values and requested percentages to two decimals. The standalone paper assessment paragraph still lacks that precision instruction, although earlier practice mentions currency precision. Acceptance: add the same explicit sentence to the paper assessment and regenerate guide.
- New independent case A a7 uses 4% nominal return and 7% inflation. Independent arithmetic `(1.04 / 1.07 - 1) × 100 = -2.8037383177570097%`, correctly rounded to −2.80%. Model answer, generated guide and assessor guide agree. Existing seven model tests were rerun and all passed.

**C2-CUR-04 — minor, print-verification dependency:** the newly supplied annual tables are in closed `<details><div class="table-wrap">…</div></details>`. The current guide's print CSS sets `details>p,details>ol{display:block}` and hides `summary`, but does not expand `details>div`. This may omit the tables from a printout when the learner has not opened those disclosures. Root browser QA should inspect print output with both tables closed; acceptance is both complete tables visible in that printout. A source correction should cover all details content needed in the printable route. This is a source-level concern, not a claimed observed browser failure. Owner: root author/browser reviewer. Retest: pending browser print verification.

Final curriculum disposition: **no remaining blocker or major finding in the revised content**. Two minor follow-ups remain as scoped above. Private prototype candidate is suitable for owner review from the curriculum perspective, conditional on root's browser/accessibility and deployment checks. No learner pilot, assistive-technology, timing, commercial-readiness or publication evidence is implied. Existing-session billing telemetry remains unavailable; no separate paid model benchmark was used.

Rechecked hashes:
- `chapter-01/dist/chapter-02/app.js`: `c60a22679d9e972bfe0aa6aeea27a1d2384241431374b32eab1b17f578437ff2`
- `chapter-01/dist/chapter-02/model.mjs`: `4696fb3fc152f959c42a0bcbec4b6044e4425aecf4a3f0579c4c4b5dabf0a797`
- `chapter-01/dist/chapter-02/guide.html`: `ae6097ba4114ee06bc3f7543459ee226a67f27d2caa9e857baed57bcecb8d26b`
- `chapter-01/instructor/chapter-02/assessment-guide.md`: `162fb7f547d13a26563a7205a0e62f78175ae3eb0308bcf0bce5e84dc8bab833`


## Final minor-fix recheck

Reinspected regenerated `dist/chapter-02/guide.html` after the last fixes:

- **C2-CUR-03 resolved.** The paper assessment now explicitly says “Round all pound values and requested percentage results to two decimals”. This matches browser instructions.
- **C2-CUR-04 resolved at source/content level.** All 15 generated `<details>` elements have `open` set, including both supplied-table disclosures. The previous closed-div print dependency has been removed. Browser print rendering remains part of root QA; this reviewer makes no unperformed rendering claim.
- No stale £1,212.55/1212.55 occurs in the regenerated guide. Default buying power remains correctly stated as £1,212.05.
- Reran Chapter 2 tests under Node v24.21.0: **8 passed, 0 failed**, including the new malformed-record test. The author's combined 14-test count was not separately rerun by this curriculum reviewer.

**Final disposition: all four curriculum findings resolved; no remaining curriculum blocker, major or minor finding.** The content remains a private owner-review prototype. Learner pilot/timings, assistive-technology checks, commercial release and publication evidence are outside this review and are not implied.

Final recheck hashes:
- `chapter-01/dist/chapter-02/app.js`: `c60a22679d9e972bfe0aa6aeea27a1d2384241431374b32eab1b17f578437ff2`
- `chapter-01/dist/chapter-02/model.mjs`: `01efe9da6da3d5d497ec885c984b0fefe843939eafd5ff8bd6be5c9e458f283c`
- `chapter-01/dist/chapter-02/guide.html`: `bea730a8620b2f89e5292ef23b96ffc98c23875f26c83edca7603e267a9e4d0b`
