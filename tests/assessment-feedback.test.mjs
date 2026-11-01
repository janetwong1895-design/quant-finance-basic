import test from 'node:test';
import assert from 'node:assert/strict';
import {assessmentReviewHtml} from '../dist/assessment-feedback.mjs';
import {ASSESSMENTS,check,grade} from '../dist/chapter-05/model.mjs';
test('a seven-of-eight critical failure names the blocking item and provides targeted corrections',()=>{
 const answers=Object.fromEntries(ASSESSMENTS.map(q=>[q.id,q.answer]));
 const critical=ASSESSMENTS.find(q=>q.critical);answers[critical.id]=999;
 const result=grade(answers);assert.equal(result.score,7);assert.equal(result.passed,false);
 const html=assessmentReviewHtml(ASSESSMENTS,answers,result,check);
 assert.ok(html.includes(`critical questions ${critical.id} need correction`));
 assert.ok(html.includes(`id="review-${critical.id}"`));
 assert.ok(html.includes(`data-feedback-target="quiz-${critical.id}"`));
 assert.ok(html.includes('Critical question'));
 assert.equal((html.match(/data-feedback-target=/g)||[]).length,8);
});
test('feedback escapes source text rather than injecting it into the learner page',()=>{
 const html=assessmentReviewHtml([{id:'a1',hint:'<script>oops</script>',critical:false}],{a1:0},{score:0,passed:false},()=>false);
 assert.ok(!html.includes('<script>'));assert.ok(html.includes('&lt;script&gt;'));
});
