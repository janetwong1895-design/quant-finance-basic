# Chapter 3: Trust the table

Version 1.0.0, 31 October 2026. Standalone beginner financial-data module; 180-minute core. Audience and prerequisite assumptions: adult self-study learners comfortable with subtraction, division and percentage change; optional Chapter 2 bridge. No financial account, software installation or live dataset required. Timing has not been learner validated.

The authentic task is to turn a deliberately messy synthetic price file into a reviewable data card, preserving the original, audit decisions, chronological interval returns and limitations. Learning objectives: CH3-01 identify provenance/units/conventions (understand/apply); CH3-02 order observations and interpret intervals (apply); CH3-03 classify quality issues and justify transformations (analyse); CH3-04 distinguish split-unit price changes from price return (analyse); CH3-05 transfer the method and produce a reproducible card (evaluate/create). These are intended Bloom classifications, not demonstrated learner outcomes.

| Step | Minutes | Evidence |
|---|---:|---|
| Setup | 10 | Diagnostic, download/dictionary/navigation confirmation |
| Provenance | 20 | Two checks; source/convention explanation |
| Order | 25 | Two checks; chronological interval explanation |
| Quality | 30 | Two checks; missing/conflict/duplicate decisions |
| Adjustment | 25 | Two checks; split share-count explanation |
| Audit lab | 35 | Prediction, both price bases, full retained/removal log, 2% hand check, reflection |
| Transfer | 25 | Changed-file five-question assessment, all correct after revision, response to feedback; optional additional changed-number case |
| Data card | 10 | Source, method/audit, limitations/revision; self-review |

Every concept includes original worked text, guided practice, targeted feedback and a reflection. The lab requires both raw and adjusted runs, not positive performance. Independent transfer changes asset, dates and amounts; all five questions must be correct and the latest submitted answers must match current fields. Prose criteria are self-reviewed; character length only establishes presence. No credential or independent coding/data expertise is certified.

The seven-row LANTERN CSV is synthetic original course material: 3 retained, 4 removed (two conflict rows, one unknown, one redundant exact duplicate). The conservative policy quarantines every conflicting observation pending source evidence, excludes missing prices without filling, keeps one exact duplicate and orders ISO dates. Split-only adjustment divides pre-split prices by two. Adjusted intervals are 2% and 2%, cumulative 4.04%; raw intervals −49% and 2%, cumulative −47.98%. The first adjusted interval spans 2→7 January; never label it daily. The dataset does not establish an expected market calendar or dividends. No trading strategy, forecast, benchmark or order execution is modelled.

Optional Python adds 50 minutes (CSV parsing/order 15, audit counts 20, split report 15), plus 10–15 minutes setup once. Standard-library scripts use synthetic embedded CSV/rows, DictReader string-to-number conversion, TODO functions, worked examples and changed numerical checks. They are integrated into the existing separate Python workspace. This time is beyond the 30-hour noncoding core, and is unvalidated.

Accessibility target: semantic headings, fieldsets/legends, radio labels, table captions and headers, live feedback, focusable main, non-navigating skip link, keyboard controls, no time limit, text/table alternative and generated complete static guide. WCAG 2.2 AA conformance and complete assistive-technology usability are not established. Core supports paper/calculator equivalence with the same task/feedback criteria. Browser storage is local, versioned and separate from other chapters/Python. Recovery revalidates completion against actual evidence; edits invalidate relevant completion and final card. JSON export contains responses and all recorded attempts/runs, but is not an import. Privacy/reset discloses browser retention, access logs and download persistence.

Primary references: Python csv documentation, Investor.gov stock split, Nasdaq provider-specific adjustment documentation. Full links are in learner sources and guide, checked 31 October 2026. No external media; all examples authored and synthetic under repository MIT licence. Actual model telemetry/cost unavailable; no paid model API calls dispatched by this module author. Review and deployment are coordinated by the root agent; learner pilot, full assistive-technology testing and commercial release remain pending.
