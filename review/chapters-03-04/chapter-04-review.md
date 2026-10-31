# Independent Chapter 4 quant, code and curriculum review

Reviewer: Chapter 3 author, independently inspecting the other author's actual Chapter 4 artifacts. Date: 31 October 2026. Scope: dist/chapter-04/{model.mjs,app.js,lessons.mjs}, tests/chapter-04.test.mjs, docs/chapter-04.md, Python definitions. This is agent review, not human pilot or complete accessibility certification.

## Findings requiring revision

**CH4-R1 · P2 · Current lab prediction and seed are not bound to recorded evidence.** app.js save-lab checks two distinct seeds, handVerified, reflection and criterion, but not that current fields.prediction and fields.seed match the latest recorded run. restoreState in model.mjs has the same omission. Editing either field invalidates completion, but immediately clicking Save can restore it without a new experiment. Reproduction executed: two recorded runs with seeds42/99 and prediction 'Original prediction only.', current prediction 'A changed prediction never recorded in any run.', valid latest handcheck/reflection/criteria; restoreState returned done.lab=true. Required fix: shared current-evidence validator binds current prediction and seed to latest run, along with handcheck and two-seed evidence. Regressions: prediction-only edit, seed-only edit, valid latest state and default seed.

**CH4-R2 · P2 · Retention claim exceeds concept-attempt record.** start text says 'Progress and all attempts save locally', and docs says 'Answers, all attempts, predictions and runs'. Concept action practice only overwrites checked[q.id] and current fields; a wrong first answer/check is lost when revised. Assessment attempt history and resampling history are retained. Required fix: append per-concept snapshots (id/raw/correct/time) and restore/export them, or accurately qualify retention claim. For this course's formative revision purpose, retention is preferred.

**CH4-R3 · P3 · Independent card completion is intentional but differs from Chapter 3 final-card gate.** Chapter 4 allows a card to be saved before preceding steps and labels missing evidence. It only claims chapter completion if all eight are done. This is coherent if retained as 'card saved' rather than a whole-chapter certificate; no release block provided that distinction remains explicit.

## Quant and curriculum checks

Confirmed arithmetic from source and tests: A mean1%, median0.5%, sample SD√(58/5) percentage points; strictly negative frequency2/6. B pairing gives cross-product40 and squared sums58/34; r=40/√(58×34). Zero-variance Pearson is undefined. Quantile implementation sorts a copy and uses h=(n−1)p interpolation with correct endpoints. Assessment quantile [0,4,8,20] at .75 is11. Critical SD/alignment/undefined-correlation/resampling-limit errors block passing at7/8. Practice wording distinguishes percentage-unit returns, percentage-point SD and 0–1 frequencies. Mean versus compound-growth caution is explicit.

Seeded resampling implementation is reconstructible: 100 repeats, six draws with replacement from six original synthetic A values. Seed42 first indices[1,0,3,1,2,0] zero-based; all repeated means recompute correctly. Histogram covers possible mean range−3..7 and supplies exact bin/replicate table alternatives. No future-distribution, causality, strategy-performance or confidence-interval claim is made. Independence/exchangeability and tiny invented sample limitations are substantive and clear.

Curriculum provides standalone setup, syntax/arithmetic bridge, four worked lessons with changed-case practice, actionable hints and reflection, seeded exploratory lab, changed-number independent assessment and feedback response, final self-reviewed statistics card. Core minutes sum180; optional Python45 is disclosed beyond the core. Prose gates explicitly check presence rather than validated reasoning. Text route and downloaded synthetic files are documented; browser interaction is independently checked by the root workflow.

## Executed verification

`node24 --test tests/chapter-04.test.mjs`: 7/7 passed at initial review. Additional direct model reproduction confirmed R1 despite passing existing tests. No paid external model/API dispatch made; actual session usage and billing unknown. Final disposition pending author fixes and reviewer recheck below.

## Fix and independent recheck

Both P2 findings resolved before release. Actual updated model exports shared labEvidence; app save and restore use it. It requires current seed and prediction equal the latest run, two distinct seeds, checked latest mean, sufficient reflection and criterion. Independent reproduction rerun: valid evidence true and restores complete; changed unrecorded prediction false and restores incomplete; changed current seed false. Updated test suite 8/8 passed, including new current-evidence regression. Actual concept action now appends practiceAttempts with id/raw/correct/time; restore preserves valid snapshots and state export naturally includes them. Independently restored an incorrect first p1 attempt and confirmed it remains present. Skip link prevents default hash navigation and focuses main. R3 remains an explicit design choice with accurate 'card saved' versus whole-chapter completion messaging.

Disposition: no unresolved P1/P2 findings within this quant/code/curriculum review scope. Ready for root integration/browser checks and owner pilot review, with previously stated human-testing limits.
