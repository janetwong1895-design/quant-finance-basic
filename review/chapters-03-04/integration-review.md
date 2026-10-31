# Independent integration, learner experience and product review

Reviewer: separate review agent; 31 October 2026. Candidate: working tree based on `df03edf3e0e92c602423aa1d31131cd4f981dfb0`, Chapters 3–4 update. This reviewer did not author implementation. Scope: shared Python integration, navigation, beginner learning sequence, source accessibility and truthful product/privacy claims. Root owns actual browser/keyboard testing; this report does not claim assistive-technology, target-learner pilot or deployment verification.

## Findings and acceptance checks

| ID | Severity | Evidence and learner consequence | Required correction / acceptance check | Owner / retest |
|---|---|---|---|---|
| INT-01 | Major | `dist/chapter-03/model.mjs` `restoreState` requires the current column to be adjusted and only an adjusted run. Live `app.js` lab-save requires both raw and adjusted runs, and accepts raw last. The prescribed adjusted → raw sequence can be saved but lose lab completion after reload. | Make restored lab evidence use the same predicate as live save, including both run bases, without rejecting the valid raw-last state. Save raw-last evidence and round-trip; change relevant input and ensure invalidation. | Root/chapter author; resolved; independent retest below. |
| INT-02 | Major | `dist/chapter-04/model.mjs` `invalidate` clears `handVerified` for reflection and criterion edits. Following hand-check → explanation → self-review → Save lab fails after the prose/checkbox inputs silently erase the successful hand check. | Clear numerical verification when the run or hand value changes; retain it for prose/self-review edits. A normal hand-check → reflection → criterion → save sequence must pass, while edited hand input and a new run require rechecking. | Root/chapter author; resolved; independent retest below. |
| INT-03 | Major | Both new `index.html` files use `href="#lesson"` for Skip to lesson; both new app renderers interpret the `lesson` hash as unknown and render start. Skipping navigation from lab/assessment changes the task. | Preserve the current page and focus the main element for the skip action. Verify from a non-start step that main receives focus and task/output remain unchanged. | Root/chapter authors; resolved; source retest and separately reported root browser checks below. |
| INT-04 | Minor | Chapter 3 selector labels Chapter 4 “Return and risk”, while Chapter 4 and the course map label it Probability & statistics. | Reconcile the label to the implemented chapter. | Chapter author; resolved; retest below. |
| INT-05 | Minor | `docs/python-practice.md` says Chapter 3 scripts embed “CSV text”; `python_chapter_03.py` embeds lists of dated teaching rows. The activities remain self-contained, but the description overstates their format. | Describe embedded teaching rows, rather than a CSV parsing task. | Root; resolved; retest below. |
| INT-06 | Minor | `python_chapter_04.py` correlation instructions claim the starter rejects “mismatched dates”. Its single date per paired row can detect duplicate dates but cannot establish that separate source series were matched correctly. | State that the starter rejects duplicate dates and assumes supplied x/y values share each row's date; require provenance/alignment verification when preparing actual paired input. | Chapter author; resolved; retest below. |

## Evidence inspected

- Shared Python `app.js`: chapters derive from exercise metadata, durations sum activity minutes, backlinks construct the correct chapter directory, previous/next use the full activity sequence. Existing completion remains separate from core chapters. The reference-fetch activity guard prevents late content from overwriting another activity.
- Shared builder extension uses separately authored standard-library chapter modules and retains the learner ZIP/reference separation. Final generated exercise count and local runnable package still require a post-build check when both modules land.
- Chapter 3 learner source distinguishes CSV storage from validity; preserves the original; declares synthetic GBP/share data, ISO dates and split-only adjustment; explains duplicates/conflicts/missingness and interval gaps. Guided lab and changed transfer case connect to the data card.
- Chapter 4 learner source gives worked numerical examples, states percentage/probability/SD units and quantile convention, aligns pairs and explicitly labels the seeded bootstrap as conditional sensitivity rather than a future forecast. Histogram has a table and complete replicate values.
- Both new apps use labelled fields, fieldset/legend for grouped Chapter 3 choices, table captions/headers, main focus on page change, live feedback, separate chapter storage and explicit reset/export limits. A source inspection is insufficient for a WCAG compliance claim.
- Product record discloses unvalidated timings, pending real-learner/assistive-technology evidence and unknown billing. Core data are original hypothetical material. No credential, live trading, market-data rights or demonstrated effectiveness is implied. Python CDN/device-local execution privacy wording remains appropriately bounded.

## Review boundary

No approval for commercial release or efficacy claim. This is a formative prototype review. Later chapters remain proposed.

## Revision and independent verification

All six findings are resolved in the revised working tree:

- INT-01: shared Chapter 3 `labEvidence` predicate now governs live save and restoration. Independently executed Node assertions confirm valid adjusted → raw evidence survives reload; a single-basis record cannot restore lab completion.
- INT-02: reflection/criterion inputs retain numerical hand verification; hand-value changes clear it. Independently executed assertions cover all three transitions. New runs explicitly clear the hand value/verification in the app.
- INT-03: both skip click handlers prevent navigation and focus the current main. Chapter 4 also handles an initial `#lesson` without a blank main. Source reinspection passed; root reports browser confirmation from non-start lessons, separately recorded in the root verification evidence.
- INT-04: Chapter 3 selector now names Chapter 4 Probability & statistics.
- INT-05: revised `ch3-order` actually parses embedded CSV via `csv.DictReader` and converts prices with `float`, so the claimed CSV experience is now present. Other Chapter 3 activities use supplied rows as described in their task instructions.
- INT-06: correlation instructions now state the duplicate-date check and the source-alignment assumption explicitly.

Cross-review fixes were also independently checked: Chapter 4 lab completion is bound to the latest run's current prediction and seed; edited prediction/seed rejects save/restoration. Two recorded wrong/correct guided-practice attempts survive restoration. Node assertions passed. The current Chapter 3/4 Node suites passed 14/14; five Python unittest methods passed. The generated Python package has 14 metadata activities and corresponding starters, no reference-solution files in the ZIP, and actual CSV parsing in `ch3-order`.

Inspected completed `docs/chapter-03.md`, `docs/chapter-04.md`, `instructor/chapter-03.md`, `instructor/chapter-04.md`, and both static-guide generators. Outcomes, practice, feedback, declared conventions and pass criteria reconcile. Both noncoding routes total 180 proposed minutes and Python adds 50/45 minutes respectively. Chapter 3 transfer mainly tests recognition plus a self-reviewed card; its formative completion must not be promoted as proof of independent data-production mastery. Chapter 4's complete prepared paper resamples disclose their difference from learner-generated runs. Instructor keys are outside `dist`; learner keys remain public and expressly formative.

Source-accessibility/product scorecard: curriculum alignment 2/3; feedback/evidence 2/3; source reproducibility 3/3; source accessibility 2/3; product truth 3/3. These scoped scores do not replace numeric cross-review, root browser tests, complete assistive-technology testing, a learner pilot or commercial review. No unresolved major/blocker remains in this reviewer scope. Recommend the corrected formative prototype for owner review/publication within its existing authorized audience, subject to the root's complete release checks.

Reviewed candidate SHA-256 fingerprints:

```text
03bd2ff590a929b1df407c2d8cf5d04dc5213b908ed99078aab24c50d933b82a dist/chapter-03/model.mjs
436e142636ce8a44e6e3fd07969a3dcd376d43741223b8399743998e464a7797 dist/chapter-03/app.js
a4979d4f12f5a47d56760fa67a1fecd540e471d600ec2744bc696e0bfd71b23b dist/chapter-04/model.mjs
49ea6ad15f9261e8f4096f8b6cb2b8d9687776a417b18d925370d68369575e9d dist/chapter-04/app.js
d95d6b1cdeec8b9bc8c5d8a99b2e4295c638ae6f5a1c8433147fc4c2e8b82190 dist/python/exercises.json
```
