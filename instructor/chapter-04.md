# Chapter 4 instructor alignment and marking guide

This file is instructor-facing source, outside the served `dist/` directory. Learner-facing explanations and public formative keys remain in the text route. Audience and practical task: a beginner prepares a cautious statistics card from an invented return sample, with explicit units, conventions and inference limits.

| Objective | Bloom process / knowledge | Activity and evidence | Correctness convention |
|---|---|---|---|
| CH4-01 | Apply / conceptual-procedural | p1,p2; a1,a2; event-boundary explanation | Strict loss <0; complement ≥0; count/n |
| CH4-02 | Apply, analyse / procedural-conceptual | c1,c2; a3; outlier and CAGR distinction | Arithmetic mean, sorted median; no compound-growth inference |
| CH4-03 | Apply / procedural | s1,s2; a4,a5; calculation card | Sample SD n−1, percentage points; sorted inclusive h=(n−1)p |
| CH4-04 | Analyse, evaluate / conceptual | r1,r2; a6,a8; date pairing reflection | Same-date pairs; zero variance undefined; association not cause |
| CH4-05 | Analyse, evaluate / conceptual-procedural | two-seed log, hand check, comparison; a7 | Replacement, six rows, 100 repetitions; seed reproduction; conditional sensitivity only |

Pacing: 10+25+25+30+25+35+20+10 = 180 core minutes. Python +45 minutes plus one-time setup. Timing is a planning allowance, untested with learners. No instructor is required for self-study; hints, public feedback and a complete paper route support revision. Adult-learning design assumptions include control of pacing, applied tasks and reflection; these are not universal effectiveness claims.

Practice keys: p1=1/3, p2=.75; c1=1%, c2=2%; s1=2 percentage points, s2=7.5%; r1=1, r2=choice1. Each lesson requires both checked calculations plus a specific 30+ character explanation and self-review checkbox. The app checks completeness, not prose correctness. Recommended substantive rubric: accurately name event/denominator, mean vs growth, sample denominator/units/quantile interpolation, same-date pairing/undefined correlation, and limits on inference. A sentence containing a causal or guaranteed-future claim needs revision even if it meets character length.

Independent case: [-6,-2,0,4,9]% gives a1=.4, a2=.6, a3=1%; a4=4 percentage points for [-4,0,4]; a5=11% for [0,4,8,20] inclusive q.75; a6=choice2 undefined, a7=choice2 conditional sensitivity, a8=choice1 date alignment. Pass 7/8 plus all four critical questions a4,a6,a7,a8. The current answers must match the submitted attempt, and a specific feedback response is required. All attempts remain in the record. This is public formative assessment, not secure summative testing or independent authorship verification.

Lab rubric: prediction precedes runs; two distinct seeds; latest first replicate mean verified; comparison distinguishes Monte Carlo repetitions from original observations; limits include independence/exchangeability, representativeness and absent tail observations. Same seed reproduces exactly in the declared JavaScript algorithm. It is not a confidence interval, posterior, future-return simulation or forecast. Prepared text-route runs use seeds42 and99; the learner hand-checks and compares their full tables. A human review should assess explanation specificity beyond the app's completeness gate.

Statistics card rubric (self-review): method specifies a convention and inputs; check supplies number/units and reconstructible arithmetic; limit explains an unsupported inference and what further evidence would help. No credit should depend on positive returns. Optional Python uses standard-library functions or explicit formulas and tests numerical/dictionary outputs; hidden reasoning or independent coding proficiency is not inferred from those public checks.

Eight automated tests cover numeric conventions and independent arithmetic, input rejection, aligned/undefined correlation, seeded replacement/reconstruction, all critical pass gates, stale evidence invalidation, malformed storage and score rederivation. Browser/assistive-technology evidence and independent review are coordinated by the parent release workflow. No blanket WCAG, pilot, learner-effectiveness or sale-readiness claim. Exact authoring/review model token use and billing are unknown; no invented costs.
