# Independent curriculum, assessment and product review

Reviewer: independent curriculum/product agent, 31 October 2026. Scope: actual learner HTML, JavaScript and model, text/paper route, package metadata, and course-proposal.md. No browser checks, assistive-technology testing, target-learner pilot, external-source verification or paid API benchmarks were performed in this review. Root owns UI QA. No application files were edited. Actual model token billing is unavailable and remains unknown.

Version inspected: prototype 0.1.0. SHA-256: app.js `711ab7f90149254cd658a7700364b1248aa810a2859046d5d7493c7bf4739e31`; model.mjs `4f189be23e61a3d67902b95d7c54a887ed149a1f3e24254ff9ab2bf283afdfd9`; chapter-guide.html `56c99abcaf84c2278d744bcf8a391a65b15474a44bd3d0cd3098d3dda400d60b`; index.html `5f809f3b746e301d3644a6005e7b59870a85e6a9fd559cec06bd279f4fb6b270`.

## Findings

### CUR-01 — Major — completion can outlive its supporting evidence

- Location: dist/app.js input handler, `run`, `complete-lab`, `case-check`, `classify`; dist/model.mjs `chapterComplete`.
- Evidence: `complete-lab` requires paired scenarios, `handVerified` and a reflection, then marks `done.lab`. A subsequent `run` resets `handVerified=false` and clears `handCheck` but retains `done.lab`. Clearing `labReflection` also retains that completion flag. The page can therefore say the chapter is complete while its own lab checks would reject the current work. The same issue affects deleting the worked-case answer/prediction or changing previously correct instrument answers. In contrast, editing the research card invalidates `done.finish`, so the behavior is inconsistent.
- Consequence: novice learners cannot trust the checklist to indicate whether their current record meets the stated completion rules. This is an evidence-integrity gap even for formative study; it does not require secure exam grading to fix.
- Correction: invalidate affected completion flags when their supporting answers change, and when a new lab run resets the required latest-run hand check; or derive current completion from validated evidence. Preserve the earlier valid attempt explicitly if completion is intentionally historical, and label the checklist accordingly.
- Proposed acceptance check: complete lab; add another run; verify lab/chapter completion is withdrawn until the new latest-run hand check is correct. Clear the reflection and verify it cannot remain currently complete. After completing classifications and worked case, change or clear their answers and confirm the checklist reflects the new state or explicitly distinguishes the historical passing attempt.
- Owner: implementation author. Fix version: pending. Retest: pending; demonstrated by source tracing, not browser execution.

### CUR-02 — Minor — the alternative numeric check repeats a taught bridge example exactly

- Location: dist/app.js readiness bridge; dist/model.mjs ASSESSMENT_SETS case B question 5; dist/app.js assessment introduction.
- Evidence: bridge teaches 25% earning 8%, 75% earning 0%, yielding 2%. Case B uses the same weights and returns and simply asks for the £1,000 ending value. The assessment introduction says the cases use new numbers and examples. Case A does change the numeric combination.
- Consequence: a learner choosing B receives a weaker transfer opportunity than the description suggests, especially if they needed the bridge. This does not invalidate formative practice or imply that repeated retrieval is inappropriate.
- Correction: use a different weighted-return combination in case B, with a matching explanation, or describe this question as retrieval plus an ending-value step.
- Proposed acceptance check: compare bridge and both assessment cases; either numeric combinations differ or wording accurately describes the repetition. Recalculate the revised item and check distractors and feedback.
- Owner: content author. Fix version: pending. Retest: pending.

## Outcome and experience assessment

The actual chapter provides a complete novice route: browser setup, ungraded diagnosis, percentage/weight bridge, four investment claims, a fully explained hypothetical comparison, learner-selected scenario experiments, a numerical check with misconception explanations and correction, and a research card with explicit self-review. Sources are optional. The printable route contains the core reading, scenarios, independent questions, worked feedback and recordkeeping instructions. No instructor response or additional installation is required for the learner route once hosted.

Alignment is appropriate for this first chapter. Instrument recognition is directly practised and checked; fair benchmark and evidence-limit reasoning are critical pass requirements; the allocation lab applies weighted returns; the research card moves beyond recognition into a self-reviewed construction task. The six-item quiz primarily measures recognition and a small calculation, so its pass should continue to be described as formative completion. Current learner-facing wording does this, and explicitly says character-count checks do not validate reasoning. It does not reward positive returns or imply professional competence.

The 5/6 rule permits the arithmetic quiz item to be wrong, but the separate required lab hand check supplies arithmetic practice/evidence. The displayed total makes that hand check vulnerable to copying; the page appropriately asks for a calculation and makes no independently verified proficiency claim. This is acceptable for the stated private formative prototype. Stronger verified-mastery or credential claims would require different evidence.

The step minutes sum to 180. The text openly states that this is an unvalidated design estimate, there is no countdown, and extra time is allowed. Whether the quantity and difficulty of tasks actually occupy three hours is unknown until a novice pilot; source inspection cannot establish timing or learning impact. A timed learner pilot remains a release dependency rather than a defect to hide with additional content.

## Product boundary and separation

The inspected dist directory contains only learner assets. The questions, correct choices and formative explanations in model.mjs/app.js are intentionally client-visible and also accessible through feedback. They are not secure instructor-only answer keys. This is appropriate because the package calls itself formative, has no proctored exam and confers no credential. Any subsequent instructor rubric, private review commentary, hidden summative bank or facilitator-only material must remain outside dist. No claim of secure grading should be added.

The app accurately discloses local saving, no sync/import, export sensitivity, private-browser loss and hosting-log limits; these were inspected as claims, not verified against future hosting infrastructure. No hosted support service, learner efficacy, accreditation, historical profitability, commercial readiness or full accessibility compliance is promised in the learner material. External text is linked rather than reproduced. A formal rights inventory, target-learner pilot, deployment/privacy review and scoped manual accessibility checks remain pending for release.

## Disposition

Candidate private prototype; CUR-01 must be resolved and independently rechecked before calling this pilot-ready. CUR-02 is a nonblocking content improvement. Curriculum alignment: 2/3; assessment/feedback: 1/3 pending CUR-01; product truth: 2/3 for the private prototype scope. Quantitative validity, execution reproducibility and accessibility are assigned to separate reviews and are not scored here. These scores are review conventions, not empirical evidence of effectiveness or permission to publish.

## Independent recheck after revision — 31 October 2026

Rechecked actual changed files, not only the author summary. Revised SHA-256: app.js `1fcdc705abc073e66c5f173462b7d45a6169b076b3c465be23d9e7c988062cc8`; model.mjs `2002edb4606d3d9a063e78fbe9ef01d4b24450a93c60e6a1d266e32a94ea09c8`; chapter-guide.html `46c85760136511f13a8e86124a8d948f5a2f43f811b40b5cdf85ff738808221e`.

- **CUR-01 resolved.** `invalidateEvidence` is invoked from the saved-input handler and invalidates instrument, worked-case, lab reflection/hand-check, diagnostic, assessment and research-card evidence. Editing a hand check also clears its verified flag. New lab runs explicitly delete `done.lab`. Editing quiz responses marks them dirty; saving a feedback response refuses to reuse the older attempt until current answers are submitted. Source tracing verifies the affected event wiring; browser behavior remains with root UI QA.
- **CUR-02 resolved.** Case B now uses 40% earning 5%, 60% earning 0%, giving 2% and £1,020. This differs from the bridge combination and has consistent distractors/explanation. The text route's alternative calculation was also changed.
- Executed the six model tests with `node --test tests/model.test.mjs`: 6 passed, 0 failed. The added regression covers completion invalidation and dirty assessment state. The first `npm test` attempt used an older Node executable and failed because it did not support `--test`; the explicit Node 24 execution above establishes the test result. It does not establish that all learner machines have that developer runtime.

No unresolved major or blocker remains in this review's curriculum/assessment/product scope. Revised assessment/feedback score: 2/3. Overall state still depends on separate quantitative and UI/accessibility evidence. The learner pilot, hosting/privacy review and manual assistive-technology evidence remain pending, so this review does not establish commercial release readiness or validated three-hour learning time. Actual billing remains unknown; no paid benchmarks were dispatched.
