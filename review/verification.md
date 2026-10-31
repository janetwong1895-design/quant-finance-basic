# Verification and release record

Artifact: Chapter 1 v0.1.0 · 31 October 2026

## Actual verification

- Node 24.21.0: six deterministic tests passed. They cover independently calculated weighted returns, invalid inputs, convex return bounds, critical assessment criteria, restoration and evidence invalidation.
- Independent quantitative reviewer checked 10,302 allocation/scenario combinations and 1,458 assessment combinations, then rechecked affected app handlers after revision. See code-accessibility-review.md.
- Independent curriculum reviewer traced actual lessons, feedback, transfer, assessment rules and product claims, then rechecked corrections. See curriculum-review.md.
- Browser learner walkthrough completed all seven steps. Tested a diagnostic misconception, four correct classifications, the 6.3-point stress gap, invalid weights, both scenario runs, hand calculation, reflection and final card.
- A 5/6 assessment with the evidence-limit critical item wrong correctly remained incomplete. Correcting and resubmitting, then saving a feedback response, completed the assessment.
- Adding a run after lab completion correctly removed lab completion. Rechecking the latest arithmetic and saving reflection restored it.
- Reload preserved seven completed steps, submitted attempts, experiment runs and the research card.
- CSV and JSON downloaded through the actual browser controls. The downloaded files were parsed and verified: three experiment runs; two assessment submissions (first failed, second passed); all seven steps complete and a saved research card. These were synthetic author-QA responses, not learner research data.
- Keyboard activation of Reset weights restored focus to the cash input. Keyboard activation of Skip to lesson focused the main lesson and preserved the current lab content.
- Narrow-screen browser inspection reported a 375 CSS-pixel content width and 375-pixel document width, with no page-level horizontal overflow in the lab. Mobile navigation and lab text remained visible. The temporary viewport override was reset.
- No browser error logs were returned in the tested session. Default-width and narrow-screen screenshots inspected. `chapter-preview.jpg` records the default-width author-QA view.

## Findings and corrections

| Finding | Severity | Correction | Recheck |
|---|---|---|---|
| CUR-01 / QA-01: stale completion after required evidence edits or a new run | Major | Central input invalidation, new-run invalidation, stale-assessment guard | Independent source/handler review plus browser new-run regression passed |
| CUR-02: second-case arithmetic reused bridge figures | Minor | New 40%-at-5% transfer item and equivalent text-route update | Independent source recheck passed |
| AX-01: reset lost keyboard focus | Minor | Restore focus to cash input | Independent source check and actual keyboard activation passed |
| Author: skip link could reset the current chapter step | Accessibility defect | Focus main without rerendering the current step | Keyboard browser check passed |

## Verification limits and release decision

Private owner-review prototype. No unresolved major/blocker reported by the two independent reviewers within their inspected scope. This record does not claim WCAG conformance, learner effectiveness, an accredited examination or commercial release readiness.

Manual screen-reader use, complete keyboard-only end-to-end completion, contrast/zoom audit, blocked-storage browser mode, cross-browser compatibility, reset confirmation/deletion, and a real beginner timing pilot remain unverified. Source contains native semantics, focus styles, table alternatives, a printable no-script path, storage-failure feedback and a reset confirmation; implementation presence alone is not proof of those checks.

Self-reviewed prose can satisfy completion without expert validation; the UI says so. Client-side quiz answers are visible by design for formative study. A high-stakes exam would need another architecture and human review.

Owner-private hosting is for reviewing a prototype, not a public course launch. Do not broaden access or advertise pilot/release-ready status without further evidence. Course-review skill was used for two independent reviews and rechecks; Sites skill was used for the private hosting workflow.

## Cost checkpoint: planning, build, review, revision, verification

All existing-session model, tool and review token/billing telemetry is unavailable. Per-call billed amounts, complete token counts, model-rate mapping, subtotal, budget headroom and completion forecast are unknown. The two agent reviews and rechecks are recorded as work performed; their cost is not assumed zero. No separately configured API calls or paid model benchmarks were launched. Course/step caps remain unset, so no cost-certified all-clear or further budgeted model-run approval is implied.

Local deterministic checks have no separately dispatched model call; local machine time, subscription allocation, hosting charges, tax and human labour are not priced. Before automated course production with paid model dispatch, supply explicit approved caps, applicable rate evidence, bounded generation/review/repair forecasts and provider usage telemetry.

## Source and rights

Original text, HTML/CSS/JavaScript, synthetic teaching figures and SVG. Optional official Investor.gov sources are linked beside further reading in the learner assets and were checked on 31 October 2026. No copied third-party course or media assets. Instructor guide and internal review records are outside the served static directory. Only `dist/` is deployed as learner content.
