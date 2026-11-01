# Design refresh review — 1 November 2026

Candidate base: GitHub 1115202474faa6e791f85e2b4b6ef87cb855f947 plus this design refresh. Scope: course map, all ten chapters, optional Python workspace and generated text guides. Learner-facing production-stage labels were removed; historical production records remain intact.

Independent reviewers: build_ch56 inspected actual diffs for curriculum, assessment and quantitative regression; build_ch910 inspected source for accessibility, learner experience and product truth. Neither authored the changes. No blocker or major found. All 65 Node checks and five Python unittest methods passed both root and quantitative review.

| Finding | Severity | Correction | Retest |
|---|---|---|---|
| Ch5/6 caption described a green line after navy restyling | Minor | Colour-independent “Solid line” | Independent source recheck passed |
| Syllabus chapter numbers had 4.448:1 contrast | Minor | Darkened to #526a8b | Independent contrast recheck: 5.536:1 on white |
| Late Python editor CSS overrode earlier print colours | Minor | Final print rules restore dark text on white | Independent source recheck passed |

Root browser evidence: course map redesign inspected visually; start link navigates to Chapter 1; existing Chapter 1 record still shows seven completed steps; new chapter selector navigates to Chapter 5 with its saved record intact; Python link opens corresponding activity; worked example executes in real Python 3.14.2 and reports sample SD 2, annualised SD 6.928203230275509 and drawdown approximately20%; Tab from code editor reaches Run my script. Shared stylesheet versioned to refresh existing caches.

Final generation completed for all chapter guides, Python activities/ZIP and course navigation. Final tests:65/65 Node,5/5 Python, git diff --check passed. Learner HTML/JS/module/Markdown scan finds no “prototype”. Quantitative models, state, graders, answer data and exercise definitions remain unchanged. ZIP payload matches the prior version, apart from archive metadata.

Limits: no target-learner pilot, full manual assistive-technology test, mobile-device or actual print-preview verification was performed. These remain unvalidated learning materials with formative self-review, hypothetical data, estimated pacing and no accredited credential. Publishing the visual update does not establish commercial release readiness.

Cost/model evidence: official Claude frontend-design plugin loaded in a restricted CLI invocation; the default model was rejected, and explicit Sonnet returned ECONNREFUSED. No implementation, token usage or price telemetry was returned by Claude. Root and two independent agent review calls have no exact per-request price telemetry; usage is unpriced, not claimed free. No benchmark or budgeted model experiment was run.

Publishing destination: existing owner-private Sites project appgprj_6ae634c5fe48819199f34c5ff6a3c1a2; preserve existing audience. GitHub main remains the requested source destination. Exact pushed/deployed SHAs and deployment ID are recorded in publication.json after publication.
