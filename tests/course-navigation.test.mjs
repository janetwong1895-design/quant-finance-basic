import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync} from 'node:fs';
const source=readFileSync(new URL('../dist/course-navigation.mjs',import.meta.url),'utf8').replace('export const CHAPTERS','const CHAPTERS').replace('import.meta.url',JSON.stringify('https://course.example/nested/course-navigation.mjs'));
test('ten-chapter navigation keeps nested hosting prefix and captures legacy selectors',()=>{
 for(const current of [2,5,10]){
  let handler,listenerCapture,stopped=false;
  const select={innerHTML:'',value:'10',addEventListener:(type,fn,capture)=>{assert.equal(type,'change');handler=fn;listenerCapture=capture;}};
  const location={pathname:`/nested/chapter-${String(current).padStart(2,'0')}/`,href:'unchanged'};
  const document={getElementById:id=>id==='chapter-select'?select:null,querySelector:()=>null};
  vm.runInNewContext(source,{URL,location,document});
  assert.equal((select.innerHTML.match(/<option /g)||[]).length,10);
  assert.match(select.innerHTML,new RegExp(`value="${current}" selected`));
  assert.equal(listenerCapture,true);
  select.value='1';handler({stopImmediatePropagation(){stopped=true;}});
  assert.equal(stopped,true);assert.equal(location.href,'https://course.example/nested/index.html');
  select.value='10';handler({stopImmediatePropagation(){}});
  assert.equal(location.href,current===10?'https://course.example/nested/index.html':'https://course.example/nested/chapter-10/');
 }
});
test('course map exposes ten direct no-script chapter links and accurate course information',()=>{
 const html=readFileSync(new URL('../dist/course/index.html',import.meta.url),'utf8');
 for(let n=1;n<=10;n++)assert.ok(html.includes(`Open Chapter ${n}`));
 assert.ok(html.includes('Optional Python activities add'));
 assert.ok(html.includes('not an accredited credential'));
});
