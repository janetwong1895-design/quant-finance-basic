# Independent quantitative, code and accessibility review

Reviewer: independent session agent `python_quant_review`. Date: 31 October 2026.
Scope: actual assets in `dist/python`, `scripts/build-python-practice.py`, `tests/test_python_practice.py`, `docs/python-practice.md`, and inherited `dist/styles.css`. Review is independent of the implementing agent. Browser and assistive-technology execution is owned by the implementing agent and was not simulated here.

Candidate identity: base Git commit `011d361b79829d37cba9702787a072e8f014fb46` plus uncommitted Python addition. SHA-256 values recorded during review (app value includes the PQA-01 and PQA-02 revisions):

| Artifact | SHA-256 |
|---|---|
| dist/python/app.js | 68bb52a9bcffdafdf631a250f4a0ffd07486cd33e30b96ec2838d9bc1ad0a7c3 |
| dist/python/worker.js | c46f7dc5ab738d43955f6e22db373e5fdabc21edd36054f0f0d959234f61c02a |
| dist/python/checker.py | 1bcb75ff0b333197f3e48ad4934584090b960714446ed9f8db2f6e2e6621fea7 |
| scripts/build-python-practice.py | 15a44229ee042086bb38dfee340222f03455059bfd980d5ba433b0ac6a6c138a |

## Findings requiring revision

### PQA-01 — Major — Reference-fetch navigation race

- Location: `dist/python/app.js`, `data-action="solution"` asynchronous handler.
- Evidence: the handler starts `fetch(reference/${selected.id}.py)`, awaits both the response and body, then writes to the current `#solution-code`. Activity navigation remains enabled during that fetch and replaces the lesson DOM. A slow response from activity A can therefore populate the reference panel in activity B. The closed-over `p` records A as having viewed a reference while B displays it.
- Consequence: a learner can be shown a different financial method as the reference for their current task, creating materially misleading formative guidance.
- Proposed correction: capture the activity identity before awaiting, obtain the text, and verify the same activity is still selected before updating the current DOM or reference-view state. A request generation guard also handles A → B → A navigation.
- Acceptance: delay reference A's response; navigate to B; resolve A; B must retain its own hidden reference panel and no reference content from A. Then reveal B and verify its correct function.
- Owner: implementing agent. Fixed by capturing `exerciseId`, obtaining the body, and returning if the selected identity differs. Independent retest executed the actual async click handler in a Node VM with a delayed response: while A's request was pending, selection changed to B; resolving A left B's panel unchanged and did not record A as revealed. A new B request populated B and recorded its view. Passed. Navigating A → B → A may show A's same static reference, which is appropriate; no different-activity content is presented. PQA-01 is resolved.

### PQA-02 — Minor — Autosave status updates on every keystroke

- Location: `dist/python/app.js` `save()`; `dist/python/index.html` `#storage-status[role=status]`.
- Evidence: every prediction, code and reflection input calls `save()`, which assigns the same success string to a live status region, even when the status has not changed. Repeated text-node replacement can queue redundant screen-reader announcements while a learner is writing.
- Consequence: potential distraction for assistive-technology users. Numerical feedback remains available, so this is nonblocking.
- Proposed correction: assign status text only when its value changes, or debounce successful-save announcements; announce a transition to storage failure immediately.
- Acceptance: several ordinary keystrokes do not repeatedly mutate the successful-save status text; a simulated storage failure still yields the warning. Actual screen-reader behaviour remains a manual-check item.
- Owner: implementing agent. Fixed by comparing `textContent` with computed `statusText` before assignment. Independent retest executed the actual `save()` source in a Node VM with a counted text setter: repeated successful saves caused zero text writes; simulated quota failure caused one warning write; repeated failures caused no additional writes; recovery caused one success write. Passed. Actual screen-reader behaviour remains untested. PQA-02 is resolved.

## Evidence and positive checks

Executed `python3 -m unittest discover -s tests -p 'test_python_*.py'`: all five test methods passed. This runs all reference functions against supplied changed-input cases; confirms incomplete starters fail except the explicitly complete worked example; checks extracted learner-pack scripts and CLI behaviour; and detects several seeded misconceptions.

Independently inspected every reference formula and case. Weighted baseline stress return is `0.2×1 + 0.4×−5 + 0.4×−20 = −9.8%`; the alternative is `0.5×1 + 0.4×−5 + 0.1×−20 = −3.5%`. A £1,000 balance at 4.8% less a £5 year-end fee is £1,043. The two-payment bond uses `20/1.05 + 1020/1.05² = £944.217687…`. A 3% nominal gain with 5% inflation yields `(1.03/1.05−1)×100 = −1.9047619…%`. The transfer report changes real value alone when inflation changes; nominal balance and the separately discounted payment are invariant. These results and units agree with the supplied solutions and stated conventions.

The deterministic teaching examples need no temporal split or random seed. Asset ordering, fee timing, distribution treatment, annual effective rates, principal inclusion, rounding, no external deposits and hypothetical provenance are documented. Checks reject boolean/nonfinite/string outputs and validate returned values rather than printed text. Public tests and separately available references are accurately described as formative; they do not certify independent proficiency or investment merit.

Code inspection supports worker termination on Stop, navigation and five-second execution timeout; a separate one-minute runtime download timeout; fresh Python execution dictionaries; escaped learner strings; separate storage key; stale code checks invalidated on edits; and explicit storage-failure messaging/export. These findings are source evidence, not proof of actual Pyodide execution. The local CLI executes user code without the browser time limit, consistent with the documentation's browser-specific limit.

Accessibility source evidence includes explicit editor/prose labels, a skip link and focusable main target, normal Tab behaviour in the editor, text results rather than colour-only state, named console, native disclosure/dialog controls, visible focus styles, responsive CSS, and a static complete text/local route. The core course remains independent of optional coding completion. No blanket WCAG or screen-reader compliance conclusion is supported by this inspection.

## Required remaining verification and limits

- Implementer must record actual browser Python examples, checks, error handling, Stop/timeout, stale-check invalidation, persistence/reset, activity navigation, and reference reveal. Implementer reports real-browser Pyodide execution succeeded using Python 3.14.2; all three initial numerical cases matched; changing the example produced −5%; an incomplete task failed 0/4 and its completed solution passed 4/4; reflection survived save/reload; editing invalidated checks; an infinite loop stopped after five seconds; and `runtime.globals.get('dict')` worked. This reviewer did not independently operate that browser.
- Implementer must record keyboard/reflow checks and identify the browser used. Screen-reader and target-learner pilot evidence remain unavailable in this review.
- Worker isolation does not constitute an untrusted-code security sandbox or guaranteed memory quota. Documentation correctly limits its claims and discloses CDN requests and learner-added network code.
- No commercial release or learner-efficacy approval is inferred from this review. No unresolved finding remains in this source/local-execution review after the PQA-01 and PQA-02 retests. Final pilot-readiness remains dependent on the implementer's recorded browser checks and the other independent review; screen-reader and target-learner pilot evidence remain pending.
