import test from 'node:test';
import assert from 'node:assert/strict';
import {allocate,ASSESSMENT_SETS,gradeQuestions,freshState,restoreState,chapterComplete,STEPS,invalidateEvidence} from '../dist/model.mjs';

test('weighted returns match independently calculated baseline and stress trade-off',()=>{
 const baselineSteady=allocate([20,40,40],'steady');
 const baselineStress=allocate([20,40,40],'stress');
 const cautiousSteady=allocate([50,40,10],'steady');
 const cautiousStress=allocate([50,40,10],'stress');
 assert.ok(Math.abs(baselineSteady.ending-1048)<1e-9);
 assert.ok(Math.abs(baselineStress.ending-902)<1e-9);
 assert.ok(Math.abs(cautiousSteady.ending-1030)<1e-9);
 assert.ok(Math.abs(cautiousStress.ending-965)<1e-9);
 assert.ok(Math.abs(cautiousStress.gross-baselineStress.gross-6.3)<1e-9);
 assert.ok(Math.abs(baselineSteady.gross-baselineSteady.benchmark)<1e-9);
 assert.ok(Math.abs(baselineStress.gross-baselineStress.benchmark)<1e-9);
});
test('no leverage, missing values or invalid totals enter the model',()=>{
 for(const weights of [[20,40,30],[-1,50,51],[101,0,-1],['',50,50],[NaN,50,50],[Infinity,0,0],[20,80]])assert.throws(()=>allocate(weights));
});
test('all allowed allocations stay within the supplied asset return bounds',()=>{
 for(const regime of ['steady','stress'])for(let cash=0;cash<=100;cash+=5)for(let bonds=0;bonds<=100-cash;bonds+=5){const r=allocate([cash,bonds,100-cash-bonds],regime);assert.ok(r.gross>=Math.min(...r.returns)-1e-9&&r.gross<=Math.max(...r.returns)+1e-9);}
});
test('both assessment cases require 5/6 plus every critical item',()=>{
 for(const qs of ASSESSMENT_SETS){const correct=Object.fromEntries(qs.map(q=>[q.id,q.answer]));assert.equal(gradeQuestions(qs,correct).passed,true);
 for(const q of qs){const oneWrong={...correct,[q.id]:(q.answer+1)%q.options.length};assert.equal(gradeQuestions(qs,oneWrong).passed,!q.critical);}
 assert.equal(gradeQuestions(qs,{}).passed,false);
 }
});
test('a fresh or corrupt record cannot claim chapter completion',()=>{
 assert.equal(chapterComplete(freshState()),false);
 assert.equal(chapterComplete(restoreState('{bad json')),false);
 assert.equal(chapterComplete(restoreState('{"version":"999","done":{"finish":true}}')),false);
 const s=freshState();for(const [id]of STEPS)s.done[id]=true;assert.equal(chapterComplete(restoreState(JSON.stringify(s))),true);
});
test('changing required evidence invalidates its completion and prevents stale grading',()=>{
 for(const [id,step] of [['instrument-cash','markets'],['caseGap','case'],['labReflection','lab'],['handCheck','lab'],['quiz-a1','assessment'],['assessmentRevision','assessment'],['planRule','finish'],['d1','readiness']]){
  const s=freshState();s.done[step]=true;s.fields.handVerified=true;invalidateEvidence(s,id);assert.equal(s.done[step],undefined);
  if(id==='quiz-a1')assert.equal(s.fields.assessmentDirty,true);
  if(id==='handCheck')assert.equal(s.fields.handVerified,false);
 }
 assert.throws(()=>allocate([20,40,40],'unknown'));
});
