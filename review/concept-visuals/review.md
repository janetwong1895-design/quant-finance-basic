# Human feedback revision: explain with graphics and animation

1 November 2026. Human finding H1: add concept graphics and JavaScript animation when useful. Baseline: Git5c8ca4b. Revision: ten original SVG explanations, each mapped to an actual chapter lesson and available on its setup page. Compounding, changing allocations, wealth/drawdown, sample returns, split units and call profit use numerical diagrams; execution, analysis-plan and evidence sequences use staged process diagrams. The walkthrough sits between explanation and practice where the page structure permits. Every frame includes a prediction prompt, explanatory text and a stated limitation.

Playback is optional: Play/Pause, Previous, Next and Restart. No autoplay, repeat, scoring or answer changes. Playback stops on tab hiding, page exit or component removal. Reduced-motion preference disables timed playback while preserving manual steps and all content. These are 43 discrete explanatory stages, not decorative background movement. There are no external libraries, media downloads, font requests or new data services.

All ten static guide pages work without JavaScript, provide complete text for every stage and CSV downloads, and are linked from each chapter's text/paper route. The course map links the graphics library. Chapter9/10 diagrams do not reveal protected pedagogical evaluation values. The examples are original hypothetical illustrations, not forecasts or personalised recommendations.

## Independent review

Quant/curriculum reviewer build_ch56 inspected models, rendering definitions, all ten generated alternatives and lesson mappings. It independently checked weighted return4.8%, £1,048 ending wealth; compound/simple year5 £161.051/£150; split wealth£100; sample squared-deviation sum58 and SD≈3.406pp; maximum drawdown20% after recovery; one-third allocation break-even; call profit with explicit£5 premium; temporal and evidence sequencing. No numerical/curriculum blocker, major or minor found. This reviewer previously authored Chapters5–6, limiting author independence for those two source chapters; it did not author these visual revisions.

UX/accessibility/product reviewer build_ch910 inspected controller, SVG/CSS, 43 descriptions, all ten alternatives and lesson/guide integration. It found two issues:

| Finding | Severity | Correction | Retest |
|---|---|---|---|
| Scaled SVG labels become too small on narrow screens | Medium; required revision | Retain640px graphic width inside a labelled, focusable horizontal scroll region; visible instructions and complete responsive HTML text | Independent source recheck passed; root390px iframe screenshot and keyboard Right scrolling visibly move chart while preserving readable labels |
| Previous/Restart can retain stale Replay label | Minor | Recompute idle label in draw after changing index | Independent source recheck passed; root Restart displays step1 and Play |

No unresolved finding remains in this bounded review. The previous judge scores are historical scoped ratings; this revision has targeted review, not a new claim of a perfect course or proven learning effectiveness.

## Verification

Root browser: Chapter2 retains8/8 saved completion and prior answer/explanation fields. Next moves to year1; Play displays Pause and advances to final year5 £161.05 versus£150; Restart returns year0 and Play; immediate Play/Pause stays at year0 across later checks. Complete static guide renders in390px iframe; keyboard focus outline is visible and Right scrolls the chart horizontally. All text stages remain below the chart. Temporary QA wrapper removed before commit.

Tests:71 Node tests and6 Python unittest methods pass. New tests check numerical invariants, all valid lesson mappings, SVG accessible names, text/CSV alternatives and absence of capstone result values in plan/evidence graphics. Existing assessment and state tests pass. Generator rerun and syntax checks pass; git diff --check passes.

Limits: reduced-motion branch is source-reviewed, not exercised by changing the user's OS preference. Full screen-reader testing, physical mobile-device coverage, print preview and learner-effectiveness trials remain unverified. No assertion of WCAG certification or validated study duration is made.

## Cost/model record

Two initial independent review turns and one targeted UX recheck reused existing session agents with inherited settings. No external paid model API, model variant or benchmark was invoked. Exact model ID, request-level tokens and billed price are not exposed: review and root generation usage are unpriced, not zero. No monetary budget or priced budget clearance is inferred. Deterministic local compute costs are unmeasured. No new commercial service was provisioned.
