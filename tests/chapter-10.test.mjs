import test from 'node:test';
import assert from 'node:assert/strict';
import * as m from '../dist/chapter-10/model.mjs';
const setup=()=>{const s=m.freshState();s.fields={setup:'yes',question:'Does the fixed rule improve the observed trade-off after all costs?',prediction:'I predict higher costs reduce final wealth; I disclose this teaching exposure.'};m.freeze(s);const r=m.evaluate(s);s.fields.hand=String(r.base.rows[0].endWealth);s.fields.memo=Array(650).fill('evidence').join(' ');for(const[id]of m.CRITICAL)s.fields['critical-'+id]='yes';for(const q of m.RUBRIC)s.fields[q.id]=String(q.weight);s.fields.reviewNote='The memo needs an explicit statement that these synthetic losses cannot predict future real-market results.';return s;};
test('Chapter10: length is only a submission check; every integrity item and current numerical evidence required',()=>{const s=setup();s.fields.hand='';assert.throws(()=>m.selfReview(s),/hand check/);s.fields.hand='959.4356435643564';s.fields.memo='short';assert.throws(()=>m.selfReview(s),/600/);s.fields.memo=Array(650).fill('evidence').join(' ');s.fields['critical-timing']='';assert.throws(()=>m.selfReview(s),/integrity/);assert.equal(m.completion(s).finish,false);});
test('Chapter10: genuine memo revision after self-review produces coherent all-step evidence and survives reload',()=>{const s=setup();m.selfReview(s);s.fields.revisionNote='I revised the conclusion to reject deployment because the deterministic synthetic block and simplified costs cannot establish real performance.';assert.throws(()=>m.saveRevision(s),/Change the memo/);s.fields.memo=s.fields.memo.replace('evidence','revised-evidence');m.saveRevision(s);assert.equal(m.revisionValid(s),true);assert.ok(Object.values(m.completion(s)).every(Boolean));const r=m.restoreState(JSON.stringify(s));assert.ok(Object.values(m.completion(r)).every(Boolean));assert.equal(r.reviews.length,1);assert.equal(r.revisions.length,1);});
test('Chapter10: modified inputs, numerical evidence, reviewed score or revised text invalidates completion',()=>{for(const change of [s=>s.fields.question+=' changed',s=>s.fields.hand='1000',s=>s.fields.dataScore='0',s=>s.fields.memo+=' another',s=>s.fields['critical-costs']='']){const s=setup();m.selfReview(s);s.fields.memo=s.fields.memo.replace('evidence','revised-evidence');s.fields.revisionNote='I replaced a profitability overclaim with a conditional conclusion grounded in both cost cases and three concrete limitations.';m.saveRevision(s);change(s);assert.equal(m.revisionValid(s),false);assert.equal(m.restoreState(JSON.stringify(s)).done.finish,false);}});
test('Chapter10: plan snapshots immutable; stale self-review cannot validate a new version even with same textual signature',()=>{const s=setup();m.selfReview(s);m.freeze(s);m.evaluate(s);s.fields.memo=s.fields.memo.replace('evidence','revised-evidence');s.fields.revisionNote='A specific revision states current evidence and acknowledges prior evaluation exposure as exploratory work.';assert.throws(()=>m.saveRevision(s),/Self-review/);assert.equal(s.plans.length,2);assert.equal(s.runs.length,2);});

test('worked capstone memo traces its stated figures to the current model',async()=>{
 const {readFile}=await import('node:fs/promises');
 const evidence=JSON.parse(await readFile(new URL('../dist/chapter-10/worked-memo-evidence.json',import.meta.url),'utf8'));
 const html=await readFile(new URL('../dist/chapter-10/worked-memo.html',import.meta.url),'utf8');
 const s=m.freshState();s.fields={question:evidence.plan.question,prediction:evidence.plan.prediction};m.freeze(s);const r=m.evaluate(s);
 for(const key of ['base','sensitivity']){
  assert.deepEqual(evidence[key],r[key]);
  for(const field of ['finalWealth','benchmarkFinal'])assert.ok(html.includes('£'+r[key][field].toFixed(2)));
 }
 assert.ok(evidence.memoWords>=600&&evidence.memoWords<=800);
 for(const q of m.RUBRIC)assert.ok(html.includes(q.title));
});
