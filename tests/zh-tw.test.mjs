import {taiwanCurrency} from '../scripts/taiwan-currency.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import path from 'node:path';
const root=new URL('../dist/',import.meta.url),read=p=>readFileSync(new URL(p,root),'utf8');
const han=s=>/[\u3400-\u9fff]/.test(s);
test('Taiwan edition preserves all chapter numerics, IDs and critical answer contracts with isolated storage',async()=>{
 for(let n=1;n<=10;n++){
  const rel=n===1?'model.mjs':`chapter-${String(n).padStart(2,'0')}/model.mjs`;
  const en=await import(new URL(rel,root)),zh=await import(new URL('zh-tw/'+rel,root));
  assert.deepEqual(zh.STEPS.map(s=>[s[0],s[2]]),en.STEPS.map(s=>[s[0],s[2]]));
  assert.ok(zh.STEPS.every(s=>han(s[1])));assert.equal(zh.STORAGE_KEY,en.STORAGE_KEY+'-zh-TW');
  for(const key of ['DATA','A','B','RAW','TRANSFER','TRANSFER_DATA','EVALUATION_DATA'])if(en[key])assert.deepEqual(zh[key],en[key],`ch${n} ${key}`);
  const contract=q=>({id:q.id,answer:q.answer,critical:!!q.critical,type:q.type,tolerance:q.tolerance});
  for(const key of ['ASSESSMENTS','AUDIT','DIAGNOSTIC','INSTRUMENTS'])if(Array.isArray(en[key])){
   assert.deepEqual(zh[key].map(contract),en[key].map(contract));assert.ok(zh[key].every(q=>!q.title||han(q.title)));
  }
  if(en.ASSESSMENT_SETS)assert.deepEqual(zh.ASSESSMENT_SETS.map(a=>a.map(contract)),en.ASSESSMENT_SETS.map(a=>a.map(contract)));
  if(en.PRACTICE)for(const id of Object.keys(en.PRACTICE))assert.deepEqual(zh.PRACTICE[id].map(contract),en.PRACTICE[id].map(contract));
 }
 const en=await import(new URL('model.mjs',root)),zh=await import(new URL('zh-tw/model.mjs',root));
 for(const regime of ['steady','stress'])for(const weights of [[20,40,40],[50,40,10],[100,0,0]])assert.deepEqual(zh.allocate(weights,regime),en.allocate(weights,regime));
});
test('all26 translated Python activities retain executable code and test inputs/answers',()=>{
 const en=JSON.parse(read('python/exercises.json')),zh=JSON.parse(read('zh-tw/python/exercises.json'));
 assert.equal(zh.length,26);
 for(let i=0;i<en.length;i++){
  for(const key of ['id','chapter','minutes'])assert.deepEqual(zh[i][key],en[i][key]);
  for(const key of ['starter','example'])assert.equal(zh[i][key],taiwanCurrency(en[i][key]));
  for(const key of ['title','objective','prediction','instructions','syntax','reflection'])assert.ok(han(zh[i][key]),`${en[i].id} ${key}`);
  assert.ok(zh[i].hints.every(h=>han(h)||h.includes('=')), `${en[i].id}: translated explanation or an unchanged formula`);
  assert.deepEqual(zh[i].cases.map(({function:f,args,expected})=>({function:f,args,expected})),en[i].cases.map(({function:f,args,expected})=>({function:f,args,expected})));
  assert.ok(zh[i].cases.every(c=>han(c.label)&&han(c.hint)));
 }
});
test('Chinese capstone counts Han characters and keeps the English word criterion separate',async()=>{
 const m=await import(new URL('zh-tw/chapter-10/model.mjs',root));
 assert.equal(m.wordCount('研究 ABC123，測試。'),4);assert.equal(m.wordCount('evidence '.repeat(650)),0);
 const page=read('zh-tw/chapter-10/worked-memo.html');
 const article=page.match(/<article[^>]*id="worked-memo"[^>]*>([\s\S]*?)<\/article>/)?.[1];
 assert.ok(article,'worked memo article must exist');const count=m.wordCount(article.replace(/<[^>]*>/g,''));assert.ok(count>=1200&&count<=1600,`memo Han count ${count}`);
});
test('Taiwan graphics preserve numeric frames and expose Chinese text alternatives',async()=>{
 const en=await import(new URL('concept-models.mjs',root)),zh=await import(new URL('zh-tw/concept-models.mjs',root));
 for(let n=1;n<=10;n++){
  assert.equal(zh.VISUALS[n].step,en.VISUALS[n].step);assert.equal(zh.VISUALS[n].frames.length,en.VISUALS[n].frames.length);
  assert.ok(zh.VISUALS[n].frames.every(f=>han(f.label)&&han(f.detail)));
  for(const key of ['weight','price'])assert.deepEqual(zh.VISUALS[n].frames.map(f=>f[key]),en.VISUALS[n].frames.map(f=>f[key]));
 }
 assert.deepEqual(zh.compound(5),en.compound(5));assert.equal(zh.callProfit(105),0);
});
test('both landing pages and language counterparts link to real local pages',()=>{
 for(const lang of ['', 'zh-tw/']){
  const html=read(lang+'learn/index.html');assert.match(html,/data-demo-answer="1"/);assert.match(html,/100×1\.20×0\.80=96/);
  assert.match(html,/data-language-switch/);assert.match(html,lang?/lang="zh-Hant-TW"/:/lang="en"/);
  assert.match(html,/400/);assert.match(html,/jsDelivr/);
  for(const suffix of ['index.html','course/index.html','python/index.html','python/guide.html',...Array.from({length:9},(_,i)=>`chapter-${String(i+2).padStart(2,'0')}/index.html`)]){
   const text=read(lang+suffix);assert.match(text,/data-language-switch/);
   const links=[...text.matchAll(/(?:href|src)="([^"#]+)"/g)].map(x=>x[1]).filter(u=>!/^https?:|^mailto:|^data:/.test(u));
   for(const link of links){const file=link.split(/[?#]/)[0];if(!file)continue;let p=new URL(file,new URL(lang+suffix,root));if(file.endsWith('/'))p=new URL('index.html',p);assert.ok(existsSync(p),`${lang+suffix}: missing ${link}`);}
  }
 }
});

test('display translation preserves learner prose and code fragments',async()=>{
 const {translateHtml}=await import(new URL('zh-tw/chapter-05/zh-ui.mjs',root));
 const user='Chapter 5 spread < 5; print("Read risk in context.")';
 const escaped=user.replaceAll('<','&lt;');
 for(const tag of ['textarea','pre','code']){
  const fragment=`<${tag} id="user-work">${escaped}</${tag}>`;
  assert.equal(translateHtml(fragment),fragment);
 }
 assert.notEqual(translateHtml('<p>Read risk in context.</p>'),'<p>Read risk in context.</p>');
});

test('localized graphic controller mounts all ten walkthroughs and manual steps work with reduced motion',async()=>{
 const vm=await import('node:vm');
 const {VISUALS}=await import(new URL('zh-tw/concept-models.mjs',root));
 const {frameHtml,transcriptHtml}=await import(new URL('zh-tw/concept-render.mjs',root));
 const source=read('zh-tw/concept-visuals.mjs').replace(/^import .*;\n/gm,'').replace('import.meta.url',JSON.stringify('https://example.test/zh-tw/concept-visuals.mjs'));
 for(let chapter=1;chapter<=10;chapter++){
  let section,listener;
  const nodes=new Map();const node=selector=>{if(!nodes.has(selector))nodes.set(selector,{textContent:'',innerHTML:'',disabled:false});return nodes.get(selector);};
  const lesson={querySelector:()=>null,querySelectorAll:()=>[],append(s){section=s;}};
  const document={hidden:false,getElementById:()=>lesson,addEventListener(){},removeEventListener(){},createElement(){return {dataset:{},isConnected:true,setAttribute(){},querySelector:node,addEventListener(type,fn){if(type==='click')listener=fn;},innerHTML:''};}};
  const context={VISUALS,frameHtml,transcriptHtml,e:v=>v,URL,location:{pathname:chapter===1?'/zh-tw/index.html':`/zh-tw/chapter-${String(chapter).padStart(2,'0')}/`,hash:'#'+VISUALS[chapter].step},document,matchMedia:()=>({matches:true,addEventListener(){},removeEventListener(){}}),window:{addEventListener(){}},MutationObserver:class{observe(){}},setTimeout(){throw Error('Reduced motion must not schedule playback');},clearTimeout(){}};
  vm.runInNewContext(source,context);
  assert.ok(section.innerHTML.includes(`/zh-tw/visuals/chapter-${String(chapter).padStart(2,'0')}.html`));
  assert.equal(node('[data-visual="play"]').disabled,true);
  listener({target:{closest:()=>({dataset:{visual:'next'}})}});
  assert.ok(node('[data-frame]').innerHTML.includes(VISUALS[chapter].frames[1].label));
 }
});

test('language links track section changes after initial page load',async()=>{
 const vm=await import('node:vm');let hashHandler;
 const link={href:'https://course.test/zh-tw/chapter-05/index.html',addEventListener(){}};
 const location={search:'?practice=1',hash:'#start'};
 vm.runInNewContext(read('language-switch.mjs'),{URL,location,document:{querySelectorAll:()=>[link]},window:{addEventListener(type,fn){if(type==='hashchange')hashHandler=fn;}}});
 assert.equal(link.href,'https://course.test/zh-tw/chapter-05/index.html?practice=1#start');
 location.hash='#assessment';hashHandler();assert.equal(new URL(link.href).hash,'#assessment');
});

test('Taiwan currency and number conventions are visible and consistent across all generated assets',async()=>{
 const {readdir}=await import('node:fs/promises');
 async function walk(dir){let files=[];for(const d of await readdir(dir,{withFileTypes:true})){const u=new URL(d.name+(d.isDirectory()?'/':''),dir);if(d.isDirectory())files.push(...await walk(u));else files.push(u);}return files;}
 for(const p of await walk(new URL('zh-tw/',root)))if(/\.(html|js|mjs|json|csv|py|txt)$/.test(p.pathname))assert.doesNotMatch(readFileSync(p,'utf8'),/便士|\bpence\b|新臺幣，不是新臺幣|£|GBP|gbp|英鎊|en-GB|\bpounds?\b|_pounds?\b/,p.pathname);
 assert.match(read('zh-tw/learn/index.html'),/NT\$100/);
 assert.match(read('zh-tw/learn/index.html'),/新臺幣 NT\$ · 1,234\.56/);
 assert.match(read('zh-tw/python/guide.html'),/並非按匯率換算/);
 assert.match(read('zh-tw/chapter-02/app.js'),/Intl.NumberFormat\('zh-TW'/);
 assert.match(read('zh-tw/python/scripts/ch1-comparison.py'),/fee_twd/);
 assert.match(read('learn/index.html'),/£100/);
 assert.equal(taiwanCurrency('£1234.56, fee_gbp, starting_pounds; compound'), 'NT$1,234.56, fee_twd, starting_twd; compound');
});
