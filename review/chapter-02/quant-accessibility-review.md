# Chapter 2 quantitative and source accessibility review

Reviewer: independent delegated quant/code and source accessibility reviewer. Date: 31 October 2026. Artifact: private prototype 1.0.0. No learner asset edits made by this reviewer. Author owns fixes and browser QA.

Inspected learner model, application, lessons, styles, index, generated paper guide, guide generator, tests and instructor assessment guide. Applied qf-review-release and qf-accessibility production contract. Browser and assistive-technology checks explicitly excluded from this assignment.

Snapshot SHA-256:

- model.mjs: `14560b255fed1ade2fa962853e0624e3acedab0fe1828bf21732a164e9d1fb41`
- app.js: `c60a22679d9e972bfe0aa6aeea27a1d2384241431374b32eab1b17f578437ff2`
- guide.html: `bea730a8620b2f89e5292ef23b96ffc98c23875f26c83edca7603e267a9e4d0b`
- lessons.mjs: `1ad8535657e06c47db7fd05b723b3b009d951287b3f11d9b6172c545a7e639cd`

## Executed evidence

Ran `node --test chapter-01/tests/chapter-02.test.mjs` from the workspace. All 7 tests pass, including rounded practice answers, blank/unit rejection, invalid bounds, paired-run isolation, critical questions, invalidation and basic malformed JSON recovery. Reran after author's static-example and case-A-a7 revision; all 7 pass again.

Independent arithmetic agrees with both current assessment keys: A = 8%, £5,618, 0%, 10%, £1,088.44, £981.41, −2.80%, second option. B = 5%, £899.89, −1%, 10%, £1,333.49, £981.14, −2.83%, second option. Checked all lesson example/practice answers against their stated arithmetic and the instructor answers.

For the default lab, separately calculating `1000*1.05**10/1.03**10` gives £1,212.050579793..., now correctly displayed as £1,212.05. Nominal £1,628.89, simple £1,500, separate-payment PV £1,227.83. Inflation-only change to 6% gives buying power £909.57 and real annual return −0.94%; nominal and separate-payment PV remain fixed. The former static £1,212.55 typo was corrected by the author; current app, guide and instructor exemplars agree. The reviewer initially overstated headline-value coverage in a progress message before separately computing that amount; this report records the actual subsequent check.

Executed 48 lab endpoint combinations: principal in {1,1000,1000000}, growth in {0,25}, inflation in {0,20}, years in {1,40}, goal in {1,10000000}. All outputs finite, row count years+1, purchasing power equals nominal divided by cumulative inflation within floating-point tolerance. These endpoint checks are additional reviewer checks, not committed tests.

Source inspection confirms Chapter 1 key `qf-studio-chapter-01-v1` differs from Chapter 2 key `qf-studio-chapter-02-v1`; each reset only removes its own key. Quiz answer edits dirty the current submission and clear assessment completion; switching clears current inputs and revision while retaining submissions. Current criterion-checkbox invalidation clears the relevant done flag. New runs clear lab hand verification/completion. Run controls can change without altering recorded runs, explicitly explained in the lab. JSON export retains all runs, attempts, fields and card; CSV exports finite numerical run fields at full precision. No external dataset or chronological leakage claim applies to this deterministic synthetic lab.

## Findings ledger

| ID | Severity / status | Location and evidence | Consequence | Acceptance check / owner |
|---|---|---|---|---|
| QA2-01 | Minor / resolved at final recheck | model.mjs restoreState (line 5) validates array containers but not their contents or scalar field types. Same-version JSON with `runs:[{}]` is accepted; results() later assumes `rows.map`. A non-string reflection is also accepted and later used with `.trim()`. | Malformed same-version local storage can make a lesson or action fail until reset. Normal app-written state is valid; no import feature exists, so this is resilience hardening rather than a normal learner-path failure. | Reject malformed saved runs/attempts and invalid field types or recover them safely. Restore same-version malformed state with run `{}`, null attempt, and numeric reflection; each must render usable UI or fresh state. Author owns fix; not retested. |
| QA2-02 | Minor / source-resolved at recheck | app.js finish(), input handler and invalidate(). finish() renders its own completion checklist and chapter-complete callout once. Input edits clear `done.finish`, update nav/feedback, but do not refresh the existing checklist/callout. | After a complete card is edited, sidebar correctly drops progress while the finish checklist and headline can still say complete until navigation/rerender. The saved state/export is correctly invalidated. | Complete chapter; edit card text or uncheck card criterion; verify sidebar, local checklist, completion headline and export agree immediately without disrupting typing/focus. Author owns browser confirmation and fix; source finding only, not browser reproduced. |
| QA2-03 | Major / corrected by author, source reverified | Static default buying-power exemplars previously said £1,212.55 despite model value £1,212.05058. Current app, generated guide and instructor guide now say £1,212.05. | Earlier discrepancy could undermine the learner's independent hand check. | Current static exemplars match `1000*1.05**10/1.03**10` to pennies; verified in current source. No open major remains from this finding. |

## Accessibility evidence and limits

Final-fix recheck: 8/8 tests pass, including the new malformed-record regression. Reviewer separately confirmed `runs:[{}]`, null attempts, numeric reflections and checked arrays reset safely; valid runs restore with calculated rows/outputs and attempts restore with recomputed scores. A forged run output of zero is recomputed to £1,628.89 nominal/£1,212.05 real; an empty-answer attempt claiming 8/8 is recomputed to 0/8 and failed. QA2-01 is partially addressed: boolean reflection fields and invalid quizSet strings are still accepted and can reach `.trim()`/undefined-question errors. This remains minor resilience hardening; no normal app path generates these records. Parent notified.

QA2-02 is source-resolved in the final-fix snapshot: `persist()` refreshes `#completion-summary` through `finishSummary()` after invalidation, without replacing card inputs. Browser verification of focus preservation remains root-owned. QA2-03 remains resolved. Current static guide supplies both year-by-year lab tables directly from growthScenario, default-open feedback and tables, and an explicit two-decimal currency convention. Checked final rows against independently calculated £1,212.05/£909.57 purchasing power. This improves static-route effort and print availability; actual print remains untested here.

Source provides native labels, radio fieldset/legend, navigation current-step state, skip link, semantic headings, explicit chart title/description, non-colour solid/dashed distinctions, captions and header cells in data tables, visible focus CSS, native dialog, status regions, focused feedback, and route focus management. No drag task or time limit is required. Calculator bridge, glossary and text/paper route preserve the numerical and interpretation constructs; external readings are optional. Prose quality is correctly labelled self-reviewed. Paper guide has both assessment cases, answers, lab instructions and record requirements.

Source inspection does not prove screen-reader behaviour, keyboard-only completion, dialog focus recovery, live-region verbosity, zoom/reflow/contrast, mobile scrollable-table access, downloaded-file contents, or printed closed-details answers. Those require browser/assistive-technology checks; the root reviewer owns available browser QA. No WCAG conformance or disabled-learner validation is claimed. Exact WCAG criteria are not quoted in this review. External source availability/content has not been re-fetched by this reviewer.

No blocker or open major identified within executed quantitative checks and source scope. Quantitative validity and reproducibility are usable for a private prototype. Accessibility remains partially verified pending browser and assistive-technology evidence. This review does not establish pilot effectiveness, learner timing, commercial readiness, hosting terms or secure examination validity. Actual model/tool billing is unavailable and unknown; no paid model benchmark was run.

## Final residual-hardening recheck

All 8 tests pass again on final model hash above. Independently verified that boolean reflections, invalid/string-out-of-range/boolean quizSet, and string-valued setup/handVerified/quizDirty recover to fresh state. Genuine boolean setup/lesson criterion fields and literal quizSet strings 0/1 preserve their values, as do ordinary reflection strings. QA2-01 is now closed. Earlier residual descriptions are retained as review history. No open quantitative or source-level finding remains. Browser/assistive-technology and pilot limitations above still apply.
