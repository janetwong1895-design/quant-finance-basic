# Chapter 1: Start with a good question

Version 0.1.0 · private self-learning prototype · 31 October 2026

## Run

The learner website is the buildless `dist/` directory. Serve it over HTTP(S):

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:8765`. JavaScript modules require an HTTP(S) server; opening `index.html` through `file://` is unsupported. Learners visiting a hosted version install nothing. No Node packages, remote fonts, analytics, external asset dependencies, server API, Python runtime or learner data uploads are used by the lesson. The private hosting wrapper may require the owner's existing sign-in.

Run deterministic checks with Node 24:

```sh
node --test tests/model.test.mjs
node --check dist/app.js
```

## Learning design

Chapter objective CH1-01: classify cash, bonds, shares and funds, including vehicle/holdings distinctions (course CLO-01 foundation). Evidence: corrected four-item practice and independent items a1–a2.

CH1-02: select a baseline appropriate to a stated comparison with matching periods and conventions (course CLO-05 preparation). Evidence: worked case, lab and independent critical item a3.

CH1-03: state a reproducible question with rule, benchmark, observation period, measurable evidence and limits (course CLO-06 preparation). Evidence: independent a4/a6 and self-reviewed research card. Free text receives criteria, an exemplar and a revision prompt; its substantive quality is not machine graded.

CH1-04: calculate a percentage change and a weighted portfolio return using small supplied tables (course CLO-01 preparation). Evidence: ungraded diagnostic/bridge, hand check and independent a5.

CH1-05: use the self-study workspace, locate feedback, retain an experiment log and export a record. Evidence: setup acknowledgement, local saved state and downloadable JSON/CSV. Download is available but not a mandatory completion gate because the app cannot verify a learner's file storage.

Sequence and proposed timings: setup 15; readiness/bridge or extension 30; market instruments 35; worked case 25; allocation lab 35; independent check/correction 25; research card/revision 15 = 180 minutes. The original M01 allocation has been adapted for a standalone browser experience. Times are proposed activity allowances, not measured completion times.

The prototype supplies the entire self-learning path rather than linking to an instructor or required external course. The text/paper route contains equivalent prompts, calculations and self-check explanations; it keeps a separate paper learning record. Browser progress and paper evidence do not synchronise.

## Practice and assessment contract

- All inputs start blank except the lab's declared baseline weights and scenario.
- Diagnostic: three ungraded items plus confidence, misconception feedback and bridge/extension choice.
- Classification: four claims, one semantic select each, targeted hints, repeated corrections; independent transfer writing and final new-case items.
- Worked case: predict/explain, complete stress calculation, receive arithmetic and interpretation feedback.
- Lab: predict → run → hand-check → compare paired scenarios → explain/revise. Every run retained; invalid weights are rejected. Full reset deletes the chapter; resetting weights retains experiment history.
- Independent check: two fixed cases, six questions each, at least 5/6 including critical benchmark and evidence-limit items. Confidence ungraded. All submissions retained with answers and reasons. A specific feedback response is needed for completion; switching cases preserves old attempts but clears current answers.
- Research card: four substantive fields, three self-review criteria, one revision field. Completeness checks are disclosed; no automated claim of research validity.
- Assessment is formative, with visible feedback and client-side answer data. No anti-cheating, proctoring, accreditation, high-stakes grading, employment eligibility or certification is claimed. A future consequential assessment would need secure delivery, human grading and an appeal route.

## Data and environment

Three synthetic teaching assets; deterministic one-year scenarios, no random seed needed. Steady returns: 2/3/8 percent; stress: 1/−5/−20 percent for cash/bonds/shares. Initial wealth £1,000. Buy at start and hold without intra-year trading. Costs, fees and taxes zero, explicitly disclosed. Baseline 20/40/40. No chronological train/test split applies to this scenario exercise because no historical series or tuned strategy is used; later backtesting chapters must add these controls. No broker integration, secrets or arbitrary code execution.

Original lesson text, examples, SVG illustration and synthetic figures. Investor.gov links are optional primary-source references checked 31 October 2026. No third-party media or dataset is redistributed. `instructor/` and `review/` are source-package documentation and excluded from the served `dist/` directory.

## Privacy and retention

Browser localStorage only, key `qf-studio-chapter-01-v1`. Saved responses, confidence, attempts, runs, progress and timestamps remain until browser data is removed or the chapter is reset. Local exports include responses and must be handled by the learner. No import or cross-device sync. Hosting access logs are outside the app's local answer storage. Storage failure displays an export reminder and preserves the in-memory session where possible.

## Release scope and costing

Candidate for private owner review. Completion-time pilot, disabled-learner participation, manual screen-reader testing, commercial terms and public course release remain pending. See `review/` for actual review evidence and verification limitations. Existing chat/tool/agent billing is unavailable: cost is unknown, not zero. No external paid model benchmark, separate API dispatch, paid market data or hosted compute lab was initiated. Budget caps remain unset; this does not constitute a cost-certified production run or approval for subsequent budgeted model dispatch.
