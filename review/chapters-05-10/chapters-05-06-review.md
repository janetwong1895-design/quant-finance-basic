# Independent Chapter 5–6 artifact review

Reviewer: separate chapter-author agent (`build_ch910`), 31 October 2026. Reviewed actual working-tree models, app controllers, lessons, HTML/text-guide builders and generated guides, data contracts, Python definitions, tests and chapter documentation. Baseline Git HEAD `5b1b7f17d93e29019b16c659ca5fd8ef86632797`; these are new working-tree artifacts, so hashes below identify inspected bytes. This review covers source, arithmetic, pedagogical construct and stated scope; root browser QA is separate. No claim of human learner validation or full accessibility conformance.

## Evidence

- Independently ran `node --test tests/chapter-05.test.mjs tests/chapter-06.test.mjs`: 16/16 pass. Covered sample denominators/scaling, initial peak, effective rate conversion, undefined ratios, long-only weights, drift/reset policies, beta versus correlation, critical gates, current-evidence binding and reconstructed restoration.
- Executed replacement-built standard-library Python references directly, without sharing browser output: all 13 cases pass across `ch5-risk`, `ch5-sharpe`, `ch6-weights`, `ch6-beta`.
- Hand-checked loss/recovery100→80→100 gives20%maximum drawdown but flat100→100→100 gives0%; sampleSD[−2,0,2]=2 and conditionalannualSD2√12. Sharpe[−1,1,3],Rf0 has mean1/sampleSD2 and annualised√12/2. Effective12%annual→monthly100(1.12^(1/12)−1), distinct from1%.
- Hand-checked constantmix50/50 on A[20,−20],B[0,0]:110×.9=99; buyhold48+50=98. Trendingcounterexample A[20,20] reverses relative result121vs122. Beta portfolio[−2,0,2] versusmarket[−1,0,1] gives4/2=2 whilecorrelation1. Constantportfolio withvaryingbenchmark beta0/correlationundefined; constantbenchmark beta/correlationundefined.
- Lessons declare percentage-point units, monthly frequency, n−1, annualisation assumptions, cost omissions and return basis. No positive-return reward or personal recommendation. Every substantive lesson has worked/guided/changed-case practice, numerical feedback, self-reviewed explanation and revision; independent assessment requires7/8 plus all critical conventions and a feedback response.
- Text routes include original data, worked examples, all practice and keys, prepared deterministic comparisons, calculator reproduction, independent assessment and criteria. Prepared outputs are explicitly distinguished from fresh browser runs. Optional Python time is additional35minutes per chapter. Learner timing and effectiveness remain unvalidated.
- Source markup has associated input labels, noncolour-only plot descriptions, exact underlying tables, status feedback, skip link, chapter-local reset and transparent retention. Full keyboard/screen-reader behaviour requires root actual-browser and later assistive-technology testing.

## Findings

| ID | Severity | Finding / required action | Status |
|---|---|---|---|
| C56-01 | Low | Both controllers converted a blank numeric lab parameter via `Number('')` to0, while evidence binding likewise treated blank as0. Clearing the visible required input could run/complete a0case without an explicit number. Reject trimmed-empty before conversion and in latest-run binding. | Author notified directly; recheck pending below. |

No unresolved high/critical arithmetic or learning-integrity finding identified in the inspected source. This is a prototype review, not a blanket release or accessibility certification.

## Inspected SHA-256 snapshots (before C56-01 correction)

```
15b07445a0daab48606c09effc86d623c96ab5440721f1866e195d15d78a0248  dist/chapter-05/model.mjs
7cc45da8dc5f12f1058e12af49005fbbb53ac3b0160fc655083982024f84565d  dist/chapter-05/app.js
4c9eb47082475c9dd71f21e190bb3e3f7ff3a03fc4eb3aadbc8a844f2e64f500  dist/chapter-05/lessons.mjs
a45b89d6c45d6c1f5403f38e2640145f09bfcf9ec23d7341986ff77294bedb88  dist/chapter-05/guide.html
bffefa1167e9c8021c0e7f4bb388aeba06012c4e9ae144a8f8c7667bb2bc9a0d  dist/chapter-06/model.mjs
de485fe69d8b3c7231f87aa9646c1db1a652c3303a5628e4726838ee774c991e  dist/chapter-06/app.js
3f98d4d06a4ff844ce2741229d82ce66e6e4122e846e3b0cf213906dbb91c67b  dist/chapter-06/lessons.mjs
53e3450dbfdde1ae6300e1e4addf47102a9cff3bcd1f808fbe05124dd055f953  dist/chapter-06/guide.html
16c8642287a1cd8b96bd2ad6c60fd92f4e73c20e5fec2585f431bce1176c3d03  scripts/python_chapter_05.py
04acec22e24a5f9a857396b77c69f3af0ee15cd9a4df9983a825aed15870ab70  scripts/python_chapter_06.py
```

## Integration/product-truth appendix

Inspected `dist/course-navigation.mjs`, `scripts/build-course-navigation.mjs`, `dist/course/index.html`, `README.md` and `docs/prototype-manifest.md`. The shared module supplies all ten chapters and adds a course-home link even where no select exists. Capturing change listener stops legacy select handlers after a valid selection; nested chapter routes resolve relative to the module root. Generator injects navigation into all ten index files idempotently. Root actual-browser routing remains a separate check.

The map and README clearly call these formative prototypes, proposed30-hour noncoding core with extra optional Python, no accredited credential or secure exam, no validated timing/effectiveness, and public client-side keys. The manifest states course-level assessment weights are proposed, not an implemented secure grade. It distinguishes frozen local sequencing from external preregistration/tamperproof blindness and retained learning records from import/sync. Synthetic-data and hosting/CDN privacy caveats are present. No unsupported commercial-readiness claim found.

Inspected integration snapshots:
`b8e1a143b352c222ba80fac88c24ec6e92ce44964b3109b9f5a19bc80ec10482` course-navigation.mjs;
`87336c73c3c8317eb2fdfa342d5aa2bc98fc51f49b540dcc08c8e01105f828ba` README.md.

Costs: review executed in existing session; actual model token/billing telemetry unavailable. No paid external API benchmark was dispatched; no zero-cost claim is made.

## C56-01 correction recheck

Author changed both controller Run handlers to reject an explicitly trimmed-empty parameter before numeric conversion, and both model evidence predicates reject blank parameters on live/reloaded completion. Existing untouched default values still work. I inspected the actual changes, reran all16 chapter tests including the added blank-current-input/restoration regression cases, and all pass. C56-01 is resolved for the prototype scope.

Rechecked changed snapshots:
```
c5dd8fe9c5f549ad1aec8fcf4df05444df3121c1d94cb0f0ce015891d6665d57  dist/chapter-05/model.mjs
5ffe4f99b1018eccf819a02730a51850fe7eab2088c9f676c62a5b3d77ad27f5  dist/chapter-05/app.js
51671edcce6ab575275e177bea0cd96855f245a28708d529a6ee011dadb1c5c1  dist/chapter-06/model.mjs
3ad9478c2728717d554ab37ad2e23599c640f3f6730662985d55a993c236d8dc  dist/chapter-06/app.js
```

No unresolved blocking finding in this source/arithmetic/curriculum review. Root actual-browser checks and explicitly unvalidated human/accessibility evidence remain separate release considerations.
