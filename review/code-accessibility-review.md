# Independent quantitative/code and accessibility source review

Reviewed 31 October 2026. Artifact: private prototype v0.1.0 in `chapter-01/dist`; reviewer is an independent child agent covering two roles. This is a source and deterministic-model review, not a browser, screen-reader, learner-pilot or release-readiness endorsement. Root agent owns browser QA. No app files were edited by this reviewer.

Reviewed SHA-256: `app.js` = `711ab7f90149254cd658a7700364b1248aa810a2859046d5d7493c7bf4739e31`; `model.mjs` = `4f189be23e61a3d67902b95d7c54a887ed149a1f3e24254ff9ab2bf283afdfd9`; `styles.css` = `ae9d2dc90861d02f7b05ab42b31826a2bf686ef33bd31c89b5792140253e497f`; `index.html` = `5f809f3b746e301d3644a6005e7b59870a85e6a9fd559cec06bd279f4fb6b270`; `chapter-guide.html` = `56c99abcaf84c2278d744bcf8a391a65b15474a44bd3d0cd3098d3dda400d60b`.

## Findings

| ID | Role / severity | Location | Evidence and consequence | Correction / acceptance check | Owner / status |
|---|---|---|---|---|---|
| QA-01 | Quant/code / **major** | `app.js`, input handler line 42 and `run` handler line 52; completion handler line 54 | Original: completed lab remained marked complete after a new run cleared `handVerified` and `handCheck`; erasing `labReflection` also retained completion. | Required edits now invalidate the stage through `invalidateEvidence`; new run explicitly clears lab completion. Independent model and app-handler checks passed; details below. Actual browser reload/export interaction remains root QA scope. | Author / **fixed; independent source/model/app-handler retest passed** |
| AX-01 | Accessibility source / minor | `app.js`, baseline handler line 51 | Original: `render(false)` replaced the focused subtree without restoring focus. | Handler now calls `$('#weightCash').focus()` after rendering. Independent app-handler mock confirms the requested focus target. Browser acceptance remains: activate reset by keyboard; focus stays in the lab and next Tab follows its controls. | Author / **source fix verified; actual keyboard behavior pending browser QA** |

## Executed quantitative checks

Executed a Node ES-module assertion script importing the actual `model.mjs`:

- 10,302 allocations: every nonnegative integer weight triple totaling 100, in both regimes, checked against independently expressed contribution arithmetic and ending-value identity.
- Six worked paths: baseline steady 4.8% / £1,048; baseline stress −9.8% / £902; 50/40/10 steady 3% / £1,030 and stress −3.5% / £965; text-route 60/30/10 steady 2.9% / £1,029 and stress −2.9% / £971.
- All 1,458 answer combinations across the two six-question sets: score and pass criteria agree with five correct plus mandatory questions 3 and 6.
- Rejected zero-total, blank, negative, nonfinite and out-of-range weight examples.
- Valid saved-state JSON roundtrip and malformed-JSON reset passed. Step allocations total 180 minutes.

The worked-case stress gap is 6.3 percentage points and £63 on £1,000; steady opportunity cost is 1.8 percentage points and £18. Inputs have no dates or future observations: this deterministic one-period synthetic exercise has no train/test split or future-data leakage path. Independent scenario runs do not mutate return assumptions. No personally suitable portfolio or future-profit claim was found. Cost, tax, holding-period, no-rebalancing and synthetic-data assumptions are declared.

## Source inspection of saving, reset and export

`persist()` serializes state into one versioned localStorage key, announces storage failure, and retains session memory on write failure. Reset requires explicit native confirmation, replaces state, clears the chapter key and starts a fresh saved state; exported files remain, as disclosed. JSON export contains state, all submitted attempts and all runs. CSV export records every run and zero fees. Blob downloads use generated local content and revoke their URL. Neither path sends learner data to a server; no network request or analytics code is present in these assets. No import or device sync is promised. Browser downloads, blocked-storage behavior, native dialog cancellation and actual reload persistence were **not executed** in this source review.

Saved-state restore checks top-level shapes but does not deeply validate records. Deep corruption could still produce rendering failures; this is a future robustness improvement rather than a demonstrated ordinary learner-path blocker. No stale-version migration is promised.

## Accessibility evidence and limits

Source positives: language and viewport metadata; main/navigation landmarks; skip link; one page heading per rendered view; explicit labels; fieldset/legend question grouping; native radios/selects/checkboxes/buttons; visible focus styles; a labelled native progress element; status regions; focused feedback targets; titled and described illustrative SVG; numerical/text equivalents for allocation bars; table captions/header cells; textual errors; no timer or drag task; responsive grids; printable HTML text route with corresponding exercises, calculation methods and formative feedback.

The text route is a complete standalone HTML lesson and requires no interaction script. Its paper completion is explicitly separate from browser progress. This is a meaningful alternative route; equivalence and usability still need learner evidence.

Keyboard-only completion, screen-reader announcements/names, focus order/restoration, dialog behavior, contrast measurements, 200%/400% zoom, mobile reflow, table scrolling, download behavior and print rendering were **not executed**. A source review cannot establish WCAG compliance. Root browser QA and later manual assistive-technology testing remain necessary. No disabled-learner testing or learner timing pilot has occurred.

## Status and cost limits

No quantitative/code blocker or major remains open in the reviewed scope following the recheck below. Actual browser and assistive-technology checks remain distinct outstanding evidence. Token usage, exact tool billing and dollar cost were unavailable to this reviewer. No separate paid model benchmark was run. This record makes no pilot-ready, release-ready or commercial-readiness claim.

## Independent revision recheck — 31 October 2026

Inspected the actual revised `invalidateEvidence` function, its input-event integration, new-run clearing, reset-weight focus restoration, assessment dirty flag and stale-feedback guard. On the skip link's `#lesson` hash, the render function now focuses the existing lesson and returns instead of routing to the overview. This is a source finding, with actual keyboard behavior reserved for root browser QA.

Rechecked SHA-256: `app.js` = `1fcdc705abc073e66c5f173462b7d45a6169b076b3c465be23d9e7c988062cc8`; `model.mjs` = `2002edb4606d3d9a063e78fbe9ef01d4b24450a93c60e6a1d266e32a94ea09c8`.

Executed all six repository Node tests: all passed. Additionally executed an independently constructed VM app-handler harness against the actual revised `app.js`, with mocked DOM/storage (not a real browser). Starting from a completed chapter with paired lab runs and a passed assessment, it verified that a new run clears `done.lab`, clears the hand check, retains all runs, saves the invalidated state and makes chapter completion false. It also verified that resetting weights focuses `#weightCash`; editing a quiz answer marks assessment dirty and clears completion; and trying to save an old passed assessment's revision then produces the submit-current-answers error rather than restoring completion. The model regression directly verifies reflection/hand-check edit invalidation and other required-answer edit invalidations.

The revised case-B arithmetic is 40% × 5% + 60% × 0% = 2%, ending at £1,020. It is consistent with its answer key. Revised scenario validation rejects an unknown regime instead of silently treating it as steady.
