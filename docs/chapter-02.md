# Chapter 2: Make the numbers comparable

Standalone self-learning financial mathematics, added to the existing private course at `/chapter-02/`. It introduces one-period total return, compounding and CAGR, present value and bond cash flows, and exact real return and purchasing power. Every lesson includes explanation, a worked example, prediction, checked practice, a new transfer case and reflection. The lab supplies a year-by-year chart/table and controlled inflation comparison. Two independent assessment cases and a calculation card complete the proposed three-hour path.

Chapter 1 remains at `/`; both chapters have independent local progress keys and links between them. No installation, new learner service or remote calculation API is required. Core calculations are deterministic original teaching scenarios with explicit timing, rate and cost assumptions.

Serve and verify from this checkout:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
node scripts/build-chapter-02-guide.mjs
node --test tests/model.test.mjs tests/chapter-02.test.mjs
```

Use Node 24 for developer checks. The complete text route is `dist/chapter-02/guide.html`; it works without lesson JavaScript and includes supplied annual tables and self-check explanations. Only `dist/` is served. Instructor alignment and keys are separate in `instructor/chapter-02/`; review records are in `review/chapter-02/`.

This is an owner-review prototype. Timings, manual screen-reader compatibility and educational effectiveness await learner testing. Free-text quality is self-reviewed, and no credential is conferred. Exact session and review costs are unknown because billing telemetry is unavailable. See the verification record for actual checks and limitations.
