# Chapter 4: Describe the evidence

Standalone browser course at `/chapter-04/`, with a 180-minute noncoding core and an optional 45-minute Python extension. Target: adult beginners who can add, divide and use a calculator. No statistics background or instructor response is required. Calculator and paper are welcome. Each of four substantive lessons provides a worked example, prediction, checked guided task, new transfer task, explanation, actionable feedback and revision. Learner timings are proposed, not validated.

The outcomes are observed event frequencies and complements (CH4-01), arithmetic mean and median (CH4-02), sample standard deviation and inclusive quantiles (CH4-03), aligned Pearson correlation (CH4-04), and conditional sampling sensitivity with a seeded resampling demonstration (CH4-05). Eight steps total 180 minutes: setup10, probability25, centre25, spread30, correlation25, lab35, independent20, card10.

All data are original hypothetical six-month total-return pairs, with no fees or taxes. Dates label aligned examples, not market observations. Returns use percentage units; sample SD is in percentage points with n−1. Quantiles sort values and use zero-based h=(n−1)p interpolation; other conventions can differ. Pearson correlation is undefined if either series has zero variance. Correlation does not establish causation or future stability.

The lab draws six rows with replacement into each replicate and computes 100 sample means, using an explicit 32-bit LCG and a user-supplied seed. Same seed and code reproduce; all runs remain in local progress. Individual sampled values can only be source values; replicate means can be new values. The exchangeable/independent assumption and tiny invented sample make this a sensitivity demonstration, not a forecast distribution or validated confidence interval. Histogram bin tables and all replicate values provide text alternatives; every run exports to CSV.

The complete text route (`dist/chapter-04/guide.html`) includes the same content, checks, independent assessment, two prepared full 100-replicate runs, paper criteria and a worked hand check. It does not require JavaScript or Python. `returns.csv` and `resampling-examples.csv` are provided. The paper route discloses the difference between prepared runs and learner-generated experiments. No learning record sync is claimed.

Three optional standard-library Python activities (15 minutes each), defined in `scripts/python_chapter_04.py`: `ch4-summary`, `ch4-quantile`, `ch4-correlation`. They contain TODO implementations, worked examples, hints, numerical transfer checks and reference replacements. Python uses 3.8-compatible syntax and no external packages. Correlation's undefined report uses an explicit numeric flag to accommodate the existing public formative checker; placeholder r=0 is explicitly not an estimate.

State uses `qf-studio-chapter-04-v1` separately from other chapters and Python. Answers, timestamped concept attempts, independent attempts, predictions and runs save locally. The lab must match the latest recorded seed and prediction before completion. Numerical checks and current evidence are re-derived on restore; edited evidence invalidates completion. Export is a record, not restore/sync. Reset affects only this chapter, not downloaded files. Prose quality is self-reviewed; length checks establish completeness only.

Developer verification (Node24):

```sh
node scripts/build-chapter-04-guide.mjs
node --test tests/chapter-04.test.mjs
node --check dist/chapter-04/app.js
```

Primary sources, checked 31 October 2026: [NIST sample scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm), [official Python statistics documentation](https://docs.python.org/3/library/statistics.html), [NIST bootstrap replacement and seed](https://www.itl.nist.gov/div898/software/dataplot/refman1/ch2/bootstra.pdf). These support conventions and methods, not this course's educational effectiveness.

Release status: owner-review learning prototype, subject to root release review. Keyboard/visual checks and independent agent review are recorded by the parent release workflow. Full screen-reader compatibility, learner timing and learning effectiveness require human testing. This is not an accredited credential or commercial-readiness certification. Actual model usage and billing are unknown because session telemetry is unavailable; no paid external research or model dispatch is introduced by the chapter.
