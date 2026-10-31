# Proposal production record

Version 0.1 · 31 October 2026

## Manifest

| Artifact | Version | Status |
|---|---|---|
| course-brief.md | 0.1 | Filled studio brief; assumptions marked |
| course-proposal.md | 0.1 | Researched proposal; syllabus, alignment, assessment outline and planned lab contract |
| production-record.md | 0.1 | Manifest, source rights, checks, cost unknowns and remaining work |

Source links appear beside supported findings in the proposal. Referenced external courses and research are benchmarks, not licensed source content for reproduction. No third-party slides, course questions, datasets or video were copied into the package. Source and data rights must be checked for any subsequent incorporation. Proposed synthetic datasets have not yet been generated.

## Checkpoints and review ledger

| ID | Check / finding | Resolution / status |
|---|---|---|
| REV-01 | Course and activity workload | 10 × 180 minutes; activity categories and primary-outcome allocation each total 1,800 minutes. Checked locally. Actual learner timing remains untested. |
| REV-02 | Outcome alignment | Six CLOs map to module objectives, practice, evidence and criteria. Proposal-level author check; independent review not performed. |
| REV-03 | Scope inflation | Calculus, ML, formal optimisation and advanced pricing deferred. Option payoff intuition retained in one guided simulation module. |
| REV-04 | Beginner route | Prior Python removed as a prerequisite; equivalent calculation route specified. Usability and equivalent difficulty untested. |
| REV-05 | Financial claims | Synthetic results explicitly limited; no return-based grades; costs, timing, trial logging and evaluation limitations specified. Implementation audit pending because labs do not yet exist. |
| REV-06 | Publication state | Proposal only. Independent reviews, learner pilot and review/release gates remain pending. No publishing action taken. |
| REV-07 | Source discrepancy | Current CFA programme page states 35–65 hours; older flyers show other durations. Current official page used. |

## Cost checkpoint

The qf-costing accounting contract was read before the curriculum was planned. This work uses the existing chat and research tools. No separate paid model API run, benchmark, grader, hosted compute or background monitor was launched. The chat's provider-billed cost and tool charges are not exposed here and must not be reported as zero.

| Field | Recorded state |
|---|---|
| Budget currency / approved course or step caps | Unspecified / unset |
| Exact billable model, tier and reasoning setting | Not available in request-level billing telemetry |
| Input, output, cached and reasoning token counts | Not exposed |
| Provider-billed amounts and tool charges | Unknown |
| Known priced subtotal | Unavailable; no complete priced records |
| Review / retry / repair API requests | None separately dispatched |
| Active external spend reservations | None created |
| Headroom and forecast to completion | Cannot calculate without scope, approved caps, rates and usage evidence |
| Model comparison decision | No live comparison performed; current chat retained, no claim of cost optimality |
| Operational budget status | Unpriced / unapproved; future budgeted model dispatch requires explicit caps and a bounded forecast |

The proposal is not held out as a cost-certified production run. A prospective production plan should allocate authoring, independent review, repair and tooling costs separately. Token-priced equivalents, account subscription allocations and actual billed spend must remain distinct. Human labour, hosting, tax and data-licensing costs are also unestimated.

No operational per-request JSONL ledger was fabricated: this interface lacks the request identifiers and usage required to reconstruct one. This document records unknown coverage at the planning and completion checkpoints. Obtain authorised telemetry and approved caps before claiming a complete cost ledger or starting budgeted automated production.

## Remaining production deliverables

Learner lesson content; runnable notebooks and no-code pack; separate instructor solutions; assessment items, keys and feedback; source/data rights manifest; quantitative and accessibility evidence; independent review findings and revision/retest ledger; learner pilot evidence; final release gate. These are subsequent production work, not missing elements of the requested proposal.

## Chapter 1 prototype continuation

The user subsequently requested Chapter 1 as a standalone web-based self-learning experience. `chapter-01/` now supplies a buildless browser lesson, embedded setup/readiness bridge, instrument practice, worked comparison, synthetic allocation lab, two formative assessment cases, targeted feedback, a self-reviewed research card, local persistence, exports and a printable text route. Instructor guidance remains outside the served `dist/` directory. This adapts M01's internal pacing to seven web-learning steps totalling 180 proposed minutes.

Two independent reviewers inspected the actual assets and rechecked corrections. Deterministic and browser checks are recorded in `chapter-01/review/verification.md`. The chapter is a private owner-review prototype; learner pilot and complete accessibility verification remain pending. Existing-session build, review and revision costs remain unknown because billing telemetry is unavailable. The remainder of the course is still at proposal stage.

## Chapter 2 continuation

At the user's request, the same private site now includes Chapter 2 at `/chapter-02/`: total returns, compounding/CAGR, present value and bond payments, inflation-adjusted values, a controlled growth lab, two independent self-check cases and a calculation card. Original source checkout remains `chapter-01/`. Chapters have separate saved progress and links between them. Instructor alignment, two independent reviews, rechecks and actual browser evidence are under `chapter-01/instructor/chapter-02/` and `chapter-01/review/chapter-02/`. Total proposed chapter workload is 180 minutes; learner pilot, full accessibility testing and download completion remain unverified. Actual generation/review/tool cost is unknown. Chapters 3–10 remain at proposal stage.
