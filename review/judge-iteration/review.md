# Judge iteration results

1 November 2026. Baseline Git402603aa6c8f26fb2d4ae84169a11867e65b05c4. Two independent reviewer roles assessed the actual materials and a fixed six-dimension0–3 rubric. See protocol.md and ratings.csv. Exact learner artifact hashes are in artifact-manifest.json; publication.json records pushed/deployed revisions after publication.

| Dimension | Baseline | Main revision | Final targeted recheck |
|---|---:|---:|---:|
| Alignment | 2 | 3 | 3 |
| Assessment and feedback | 2 | 2 | 3 |
| Quantitative validity | 1 | 3 | 3 |
| Local reproducibility | 3 | 3 | 3 |
| Accessibility / learner experience within inspected scope | 2 | 3 | 3 |
| Product truth | 3 | 3 | 3 |
| Internal total /18 | 13 | 17 | 18 |

These ratings are reviewer judgments about inspected artifacts, not measured learner success, a commercial readiness grade, a complete accessibility audit or a percentage of course quality. A final3 means the criterion was demonstrated within the stated scope. It does not mean no undiscovered defects exist. The UX reviewer also reported a separate standalone-experience diagnostic2/3 initially; it is not double-counted in the fixed total.

## Findings and revisions

| ID | Role and evidence | Severity | Correction and acceptance evidence |
|---|---|---|---|
| Q1 | Quant reviewer reproduced Ch4 constant [.3]×12 SD≈5.8e−17 and r=1, instead of0/undefined, in browser model and Python reference | Major | Recognise exactly identical observations before centring. Tests cover either/both constant series and genuinely varying nearconstant series. Python spec, starter, reference, guide, instructor reference and ZIP regenerated. Independent recheck passed. |
| U1 | UX reviewer found all26 Python activities above the mobile lesson and forced page-top scrolling | Medium usability / treated as required revision | Native chapter-grouped activity selector replaces expanded list below700px. Focus and scroll go to selected lesson. Root390px iframe directCh10 entry and native selection to next activity show requested heading and retain prior saved script/prediction/checks. Independent source recheck passed. |
| U2 | Ch4–7 critical criteria were hard to locate; feedback flattened eight answers into prose | Medium usability / treated as required revision | Critical questions labelled inline. Shared structured feedback names blocking critical failure, gives item hints and links/ARIA associations. Root7/8 with faileda3 remains blocked; link focusesa3 without hash navigation;8/8 resubmission passes. Scoring and revision gates unchanged. |
| A1 | Quant reviewer found only abstract capstone calibration descriptions | Minor | Complete692-word memo, exact current-model ledger, allfive rubric annotations and specific flawed-claim revision. Interactive and complete text routes link it with evaluation-exposure warnings. Independent word count and numerical reconciliation passed. |
| D1 | Both reviewers found obsolete opening scope in brief/proposal | Minor | Current10chapter/26optional-script delivery leads brief; original proposals explicitly labelled historical. Independent recheck passed. |
| U3 | Round2 quant reviewer found restored assessments lose structured correction details | Minor | Render reconstructs prior submitted feedback, marks changed answers as stale and preserves attempt count/focus. Root reload+editedanswer check and targeted independent helper/source recheck passed; assessment rating2→3. New submissions refresh the displayed attempt log. |

## Review roles and independence

Quant/curriculum reviewer build_ch56 covered alignment, assessment, quantitative validity and reproducibility. Inspected brief/proposal/manifest, Chapters1–4 and7–10, Python references/pack, and spot calculations in5–6. It previously authored Chapters5–6; those spot checks are not independent author review. Its initial representative checks included bond PV£1,000, compounded +20/−20%=−4%, drawdown10% for[-10,+10], first capstone interval£959.4356436 and both cost cases. The reviewer did not author this revision.

UX/product reviewer build_ch910 covered navigation/accessibility structure across1–10, deeper sampled1,3,5–10, setup/practice/assessment/text alternatives, all26 Python contracts, course map, brief and product claims. It did not author these revisions. Ratings are source/targeted-test judgments; the root's browser observations are separately described, not represented as reviewer browser work.

Two full judge rounds plus one bounded targeted recheck were used. No fixed desired rating was supplied to either reviewer. The intermediate17/18 and remaining minor are retained rather than replaced by final ratings.

## Verification and limits

Final checks:69 Node tests and6 Python unittest methods pass; syntax checks and git diff --check pass. New coverage includes decimal constant/nearconstant correlation,7/8 critical-failure correction mapping, HTML escaping and current-model worked-memo evidence reconciliation. All generated guides/Python assets remain reproducible. Temporary390px QA wrapper was removed before committing.

Root browser walkthrough: inspected critical markers; submitted7/8 with criticala3 incorrect; correction focusesquiz-a3 with hash#assessment unchanged; reopening/reloading retains detailed feedback; editinga3 flags stale feedback without new submission; resubmission8/8 succeeds. Native activity selection in an actual390px iframe switches Ch10activities, focuseslesson and preserves saved work. This is responsive-frame testing, not a physical-device claim. Capstone review link opens the example, disclosures and allfive annotations; prior local Chapter10 record remains6/6.

Full assistive-technology testing, physical mobile-device coverage, independent human reasoning grades, rubric reliability, target-learner workload/effectiveness, rights/legal/commercial readiness remain unverified. Synthetic data and public/local plan-gate limitations are retained. Internal full scores do not establish these external validations.
