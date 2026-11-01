import {VISUALS,compound,allocation,callProfit,escape as e} from './concept-models.mjs';
const text=(x,y,value,cls='')=>`<text x="${x}" y="${y}" class="${cls}">${e(value)}</text>`;
const line=(x1,y1,x2,y2,cls='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${cls}"/>`;
const poly=(points,cls)=>`<polyline points="${points.map(p=>p.join(',')).join(' ')}" class="${cls}"/>`;
export function visualSvg(chapter,index){
 const v=VISUALS[chapter],frame=v.frames[index],W=640,H=300;let content='';
 if(v.kind==='compound'){
  const x=n=>65+n*100,y=n=>245-(n-100)*2;
  content=text(65,24,'Wealth (£)')+line(65,245,565,245,'axis')+line(65,245,65,50,'axis');
  for(const n of [100,125,150,175])content+=line(65,y(n),565,y(n),'grid')+text(22,y(n)+5,n);
  for(let n=0;n<=5;n++)content+=text(x(n)-7,273,n);
  content+=text(270,295,'Year')+poly(Array.from({length:6},(_,i)=>[x(i),y(compound(i).simple)]),'series secondary-series')+poly(Array.from({length:index+1},(_,i)=>[x(i),y(compound(i).compound)]),'series');
  content+=`<circle cx="${x(index)}" cy="${y(compound(index).compound)}" r="7" class="marker"/>`+text(370,24,'Solid: compound; dashed: simple');
 }else if(v.kind==='drawdown'){
  const pts=[[90,75],[320,215],[550,75]];
  content=text(22,25,'Wealth index')+line(90,75,550,75,'peak-line')+text(440,58,'Peak100')+poly(pts.slice(0,index+1),'series');
  for(let i=0;i<=index;i++)content+=`<circle cx="${pts[i][0]}" cy="${pts[i][1]}" r="7" class="marker"/>`+text(pts[i][0]-18,pts[i][1]-18,[100,80,100][i]);
  content+=text(62,272,'Start')+text(286,272,'After−20%')+text(518,272,'After+25%');
  if(index>=1)content+=line(335,80,335,210,'loss-line')+text(350,154,'20% below peak');
 }else if(v.kind==='allocation'||v.kind==='weights'){
  const parts=v.kind==='allocation'?[20,40,40]:[frame.weight,100-frame.weight],labels=v.kind==='allocation'?['Cash','Bonds','Shares']:['Asset A','Asset B'];let left=45;
  content=text(45,32,'Starting weights (%)');
  for(let i=0;i<parts.length;i++){let width=parts[i]/100*550;content+=`<rect x="${left}" y="65" width="${width}" height="60" class="sleeve sleeve-${i}"/>`;left+=width;content+=text(45+i*(v.kind==='allocation'?185:280),161,`${labels[i]} ${parts[i].toFixed(2)}%`);}
  if(v.kind==='allocation')content+=text(45,205,index>=2?'Contributions: 0.4 + 1.2 + 3.2 = 4.8 pp':'Same starting capital, separate sleeves')+text(45,251,index===3?'Ending wealth £1,048':'Each weight multiplies its own return');
  else{const a=allocation(frame.weight);content+=text(45,208,`(+10% × ${a.weightA.toFixed(2)}%) + (−5% × ${a.weightB.toFixed(2)}%)`)+text(45,257,`Portfolio return ${a.returnPct.toFixed(2)}%`,'big-value');}
 }else if(v.kind==='split'){
  content=text(45,30,'A change in units')+`<rect x="45" y="65" width="200" height="130" class="sleeve sleeve-0"/>`+text(76,223,'1 share×£100');
  content+=line(220,130,340,130,'series');
  if(index>=1)content+=`<rect x="370" y="65" width="100" height="130" class="sleeve sleeve-1"/><rect x="480" y="65" width="100" height="130" class="sleeve sleeve-2"/>`+text(415,223,'2 shares×£50');
  content+=text(64,270,'Value£100')+(index>=2?text(437,270,'Value£100'):text(380,270,'Next: split into two shares'));
 }else if(v.kind==='sample'){
  const a=[-3,-1,0,1,2,7],y=n=>218-n*22;
  content=text(30,25,'Monthly return (%)')+line(55,y(0),600,y(0),'axis');
  for(const n of [-3,0,1,4,7])content+=text(15,y(n)+5,n);
  a.forEach((n,i)=>{const x=65+i*90;content+=`<rect x="${x}" y="${Math.min(y(n),y(0))}" width="48" height="${Math.max(2,Math.abs(n)*22)}" class="sleeve sleeve-${n<0?2:0}"/>`+text(x+14,290,`M${i+1}`);});
  if(index>=1)content+=line(55,y(1),605,y(1),'peak-line')+text(425,180,'Mean1% (dashed)');
 }else if(v.kind==='call'){
  const x=p=>65+(p-60)*6,y=profit=>225-profit*4;
  content=text(18,24,'Expiry profit (£)')+line(65,y(0),555,y(0),'axis')+line(65,70,65,260,'axis')+poly([60,80,100,105,120,140].map(p=>[x(p),y(callProfit(p))]),'series');
  for(const p of [60,80,100,120,140])content+=text(x(p)-13,283,p);
  for(const profit of [-5,0,15,35])content+=text(18,y(profit)+5,profit);
  content+=`<circle cx="${x(frame.price)}" cy="${y(callProfit(frame.price))}" r="8" class="marker"/>`+text(280,299,'Terminal asset price (£)')+text(270,28,'Break-even:105; strike:100');
 }else{
  const labels=chapter===8?['Close[t]','Signal[t]','Open[t+1]','Open[t+2]']:chapter===9?['Develop','Freeze','Evaluate','Disclose']:['Input','Plan / ledger','Memo','Revise'];
  content=text(30,30,'Read from left to right; later evidence cannot travel backwards');
  labels.forEach((label,i)=>{let x=35+i*152;content+=`<rect x="${x}" y="90" width="125" height="100" rx="10" class="flow-node ${i<=index?'revealed':''}"/>`+text(x+13,128,`0${i+1}`)+text(x+10,166,label);if(i<3)content+=line(x+125,140,x+149,140,'axis');});
  content+=text(35,250,`Current step: ${index+1} of4`)+text(35,283,chapter===8?'Position earns the interval after execution.':'Keep the earlier record when you revise.');
 }
 return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="visual-title-${chapter} visual-desc-${chapter}"><title id="visual-title-${chapter}">${e(v.title)}</title><desc id="visual-desc-${chapter}">${e(frame.label+'. '+frame.detail)}</desc>${content}</svg>`;
}
export function frameHtml(chapter,index){const v=VISUALS[chapter],f=v.frames[index];return `<div class="concept-drawing" tabindex="0" role="region" aria-label="Concept diagram; scroll horizontally on a narrow screen">${visualSvg(chapter,index)}</div><p class="mini">On a narrow screen, scroll the diagram horizontally. Every value and step is also explained below.</p><p class="concept-current" role="status"><strong>Step ${index+1}/${v.frames.length}: ${e(f.label)}</strong><br>${e(f.detail)}</p>`;}
export function transcriptHtml(chapter){const v=VISUALS[chapter];return `<ol class="concept-transcript">${v.frames.map(f=>`<li><strong>${e(f.label)}</strong><p>${e(f.detail)}</p></li>`).join('')}</ol>`;}
