# Taiwan currency and number correction

Base commit: add176e. Scope: Taiwan edition only; English currency examples remain GBP. The generated artifact manifest records the reviewed files by SHA-256.

Hypothetical teaching contexts now use TWD / NT$, not a claim of FX conversion. Numerical relationships, assessed answers and Python test arguments remain unchanged. Display numbers use zh-TW grouping and decimal separators; calculation examples may retain decimal places for checking. Numeric input controls and machine-readable CSV retain ungrouped numbers. Currency units, code suffixes, data dictionaries, downloads, graphics, assessments, first-sight language bar and marketing preview agree.

Independent reviews used existing agents under qf-review-release:

| Reviewer | Coverage | Finding and resolution | Scoped ratings |
| --- | --- | --- | --- |
| build_ch56 | Quantitative validity, Python execution, reproducibility | Remaining pounds code labels and contradictory old notices corrected; retest found no unresolved defects | Quantitative validity 3/3; reproducibility 3/3 |
| build_ch78 | Curriculum, feedback, accessibility and product truth | Python unit inconsistency corrected; authoring notes updated to acknowledge currency-specific identifier adaptation | Alignment 3/3; feedback 2/3; accessibility 2/3; product truth 3/3 |

Author browser checks: Taiwan landing preview selects NT$96 and explains the changed percentage base; Chapter2 growth lab records NT$1,000.00 and displays NT$1,628.89 after ten years at5%, with purchasing power NT$1,212.05 at3% inflation. Browser inspection additionally caught and fixed the obsolete word 便士, replaced by 小數點後兩位. Full assistive technology testing was not performed. Reviews do not demonstrate general learning effectiveness or commercial readiness.

Validation: 80 Node tests,8 Python test methods pass. Independent execution covered26 reference scripts/90 numerical cases; ZIP starters and specs match generated assets, and extracted checker runs. Recursive generated-asset checks reject UK currency labels and contradictory notices. English parity, separate progress storage, visual controls, locale guide links and capstone length checks pass.

Cost record: one authoring session plus two independent bounded review dispatches and review follow-ups. Exact model/provider usage, token totals and dated prices are unavailable; costs are unpriced, not zero. No external model benchmark or paid financial-data request was run.

Status: currency correction verified for publication; existing broader pilot/manual accessibility limitations remain. Historical review/zh-TW records the previous release and is retained as history.
