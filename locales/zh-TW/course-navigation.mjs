// A single table keeps all ten chapters discoverable.
export const CHAPTERS=[[1, "提出好問題", "金融工具與公平比較"], [2, "金融數學", "報酬率、複利、現值與通膨"], [3, "金融資料", "CSV、清理與分割調整"], [4, "機率與統計", "樣本摘要、相關與不確定性"], [5, "風險與績效", "波動度、回撤與夏普比率"], [6, "投資組合分散", "權重、再平衡、相關與貝他"], [7, "模擬與損益", "情境、遠期契約與買權"], [8, "透明的回測", "訊號、成交、成本與基準"], [9, "研究可靠性", "偏誤、試驗紀錄與計畫"], [10, "專題與研究溝通", "可重現證據、撰寫與修正研究備忘錄"]];
const root=new URL('.',import.meta.url);
const route=n=>new URL(n===1?'index.html':`chapter-${String(n).padStart(2,'0')}/`,root).href;
const current=Number(location.pathname.match(/chapter-(\d+)/)?.[1]||1);
const selector=document.getElementById('chapter-select');
if(selector){selector.innerHTML=CHAPTERS.map(([n,title])=>`<option value="${n}" ${n===current?'selected':''}>${String(n).padStart(2,'0')} · ${title}</option>`).join('');selector.addEventListener('change',event=>{event.stopImmediatePropagation();const n=Number(selector.value);if(CHAPTERS.some(([id])=>id===n)&&n!==current)location.href=route(n);},true);}
const sidebar=document.querySelector('.sidebar');
if(sidebar&&!sidebar.querySelector('[data-course-home]')){const a=document.createElement('a');a.href=new URL('course/',root).href;a.className='text-button';a.dataset.courseHome='true';a.textContent='完整課程地圖';const anchor=sidebar.querySelector('.sidebar-title');if(anchor)anchor.before(a);else sidebar.append(a);}
