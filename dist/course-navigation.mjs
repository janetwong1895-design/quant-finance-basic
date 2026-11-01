// A single table keeps all ten chapters discoverable.
export const CHAPTERS=[
 [1,'A good question','Markets, instruments and a fair comparison'],
 [2,'Financial mathematics','Returns, compounding, present value and inflation'],
 [3,'Financial data','CSV, cleaning decisions and split adjustments'],
 [4,'Probability and statistics','Sample summaries, correlation and uncertainty'],
 [5,'Risk and performance','Volatility, drawdown and Sharpe conventions'],
 [6,'Portfolio diversification','Weights, rebalancing, correlation and beta'],
 [7,'Simulation and payoffs','Seeded scenarios, forwards and calls'],
 [8,'A transparent backtest','Signals, execution, benchmark and costs'],
 [9,'Research reliability','Bias, trial logs and a frozen analysis plan'],
 [10,'Capstone and communication','Reproduce evidence, write and revise a research memo']
];
const root=new URL('.',import.meta.url);
const route=n=>new URL(n===1?'index.html':`chapter-${String(n).padStart(2,'0')}/`,root).href;
const current=Number(location.pathname.match(/chapter-(\d+)/)?.[1]||1);
const selector=document.getElementById('chapter-select');
if(selector){selector.innerHTML=CHAPTERS.map(([n,title])=>`<option value="${n}" ${n===current?'selected':''}>${String(n).padStart(2,'0')} · ${title}</option>`).join('');selector.addEventListener('change',event=>{event.stopImmediatePropagation();const n=Number(selector.value);if(CHAPTERS.some(([id])=>id===n)&&n!==current)location.href=route(n);},true);}
const sidebar=document.querySelector('.sidebar');
if(sidebar&&!sidebar.querySelector('[data-course-home]')){const a=document.createElement('a');a.href=new URL('course/',root).href;a.className='text-button';a.dataset.courseHome='true';a.textContent='Course map';const anchor=sidebar.querySelector('.sidebar-title');if(anchor)anchor.before(a);else sidebar.append(a);}
