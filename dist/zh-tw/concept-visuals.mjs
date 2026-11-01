import {VISUALS,escape as e} from './concept-models.mjs';
import {frameHtml,transcriptHtml} from './concept-render.mjs';
const chapter=Number(location.pathname.match(/chapter-(\d+)/)?.[1]||1),v=VISUALS[chapter],lesson=document.getElementById('lesson');
const root=new URL('.',import.meta.url),reduced=matchMedia('(prefers-reduced-motion: reduce)');
let cleanup=()=>{};
function mount(){
 if(!lesson||!v)return;
 const step=location.hash.slice(1)||'start';
 if(!['start',v.step].includes(step)||lesson.querySelector('[data-concept-visual]'))return;
 cleanup();
 const section=document.createElement('section');section.className='concept-visual';section.dataset.conceptVisual='true';section.setAttribute('aria-labelledby','concept-heading');
 section.innerHTML=`<div class="concept-intro"><span class="concept-kicker">看懂概念</span><h2 id="concept-heading">${e(v.title)}</h2><p>${e(v.prompt)}</p></div><div data-frame></div><div class="concept-controls" role="group" aria-label="圖解播放控制"><button type="button" data-visual="previous" class="secondary">上一步</button><button type="button" data-visual="play">播放</button><button type="button" data-visual="next" class="secondary">下一步</button><button type="button" data-visual="restart" class="text-button">重新開始</button></div><p class="mini" data-motion></p><details><summary>不播放動畫，閱讀全部步驟</summary>${transcriptHtml(chapter)}</details><p class="concept-limit">${e(v.limit)}</p><a class="lesson-link" href="${new URL(`visuals/chapter-${String(chapter).padStart(2,'0')}.html`,root).href}">開啟完整圖解與文字指南</a>`;
 // Keep setup, explanation and assessment intact. The walkthrough is supplementary.
 const panels=lesson.querySelectorAll(':scope > .panel');const anchor=panels[1]||lesson.querySelector('.bottom-nav');if(anchor)anchor.before(section);else lesson.append(section);
 let index=0,timer=null,playing=false;
 const button=action=>section.querySelector(`[data-visual="${action}"]`);
 const stop=()=>{clearTimeout(timer);timer=null;playing=false;button('play').textContent=index===v.frames.length-1?'重播':'播放';};
 const draw=()=>{if(!playing)button('play').textContent=index===v.frames.length-1?'重播':'播放';section.querySelector('[data-frame]').innerHTML=frameHtml(chapter,index);button('previous').disabled=index===0;button('next').disabled=index===v.frames.length-1;button('play').disabled=reduced.matches;section.querySelector('[data-motion]').textContent=reduced.matches?'系統已啟用減少動態效果。請用上一步、下一步逐項閱讀。':'不會自動播放。播放時每 2.5 秒前進一步，可隨時暫停；也可直接逐步閱讀。';};
 const tick=()=>{if(!playing||!section.isConnected||document.hidden){stop();return;}if(index<v.frames.length-1){index++;draw();}if(index===v.frames.length-1)stop();else timer=setTimeout(tick,2500);};
 section.addEventListener('click',event=>{const action=event.target.closest('[data-visual]')?.dataset.visual;if(!action)return;if(action==='play'){if(playing){stop();return;}if(reduced.matches)return;if(index===v.frames.length-1){index=0;draw();}playing=true;button('play').textContent='暫停';timer=setTimeout(tick,2500);return;}stop();if(action==='next')index=Math.min(v.frames.length-1,index+1);if(action==='previous')index=Math.max(0,index-1);if(action==='restart')index=0;draw();});
 const motionChanged=()=>{stop();draw();};
 const visibilityChanged=()=>{if(document.hidden)stop();};
 reduced.addEventListener('change',motionChanged);document.addEventListener('visibilitychange',visibilityChanged);
 cleanup=()=>{stop();reduced.removeEventListener('change',motionChanged);document.removeEventListener('visibilitychange',visibilityChanged);};
 draw();
}
if(lesson){new MutationObserver(()=>{if(!lesson.querySelector('[data-concept-visual]'))cleanup();mount();}).observe(lesson,{childList:true});mount();window.addEventListener('hashchange',()=>{cleanup();mount();});window.addEventListener('pagehide',()=>cleanup());}
