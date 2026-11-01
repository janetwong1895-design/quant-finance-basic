import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {VISUALS,compound,allocation,callProfit,drawdownPath} from '../dist/concept-models.mjs';
import {visualSvg,transcriptHtml} from '../dist/concept-render.mjs';
test('graphics preserve compounding, weighted returns, option premium and drawdown conventions',()=>{
 assert.ok(Math.abs(compound(5).compound-161.051)<1e-9);assert.equal(compound(5).simple,150);
 assert.ok(Math.abs(allocation(100/3).returnPct)<1e-12);
 for(const weight of [0,25,100/3,50,75,100]){const v=allocation(weight);assert.equal(v.weightA+v.weightB,100);assert.ok(v.returnPct>=-5&&v.returnPct<=10);}
 assert.equal(callProfit(80),-5);assert.equal(callProfit(100),-5);assert.equal(callProfit(105),0);assert.equal(callProfit(120),15);
 assert.ok(Math.abs(Math.max(...drawdownPath.map(r=>r.loss))-20)<1e-10);assert.equal(drawdownPath.at(-1).loss,0);
});
test('all ten graphics map to real lesson steps and supply every static frame without evaluation leakage',async()=>{
 for(let n=1;n<=10;n++){
  const v=VISUALS[n];assert.ok(v.prompt&&v.limit&&v.frames.length>1);
  const model=await import(new URL(n===1?'../dist/model.mjs':`../dist/chapter-${String(n).padStart(2,'0')}/model.mjs`,import.meta.url));
  assert.ok(model.STEPS.some(s=>s[0]===v.step),`chapter${n} ${v.step} must be a real lesson`);
  for(let i=0;i<v.frames.length;i++)assert.match(visualSvg(n,i),/role="img" aria-labelledby=/);
  const page=readFileSync(new URL(`../dist/visuals/chapter-${String(n).padStart(2,'0')}.html`,import.meta.url),'utf8');
  for(const f of v.frames)assert.ok(transcriptHtml(n).includes(f.label));
  assert.match(page,/No JavaScript|no JavaScript/);assert.match(page,/\.csv/);
 }
 assert.ok(!JSON.stringify(VISUALS[9]).includes('917.91'));assert.ok(!JSON.stringify(VISUALS[10]).includes('917.91'));
});
