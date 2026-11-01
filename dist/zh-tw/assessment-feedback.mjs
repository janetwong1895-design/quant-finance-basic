const escape=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function assessmentReviewHtml(questions,answers,result,check){
 const missing=questions.filter(q=>q.critical&&!check(q,answers[q.id]));
 return `<p><strong>${result.score}/${questions.length}. ${result.passed?'已符合條件，請儲存回饋回應。':'請修正後重新提交。'}</strong></p>${missing.length?`<p>尚未通過：必須正確的關鍵題 ${missing.map(q=>escape(q.id)).join(', ')} 仍需修正；即使總分達標，關鍵題也不能答錯。</p>`:''}<ol class="assessment-review">${questions.map(q=>`<li id="review-${escape(q.id)}"><strong>${escape(q.id)}: ${check(q,answers[q.id])?'正確':'重新檢查'}${q.critical?' · 關鍵題':''}</strong><p>${escape(q.hint)}</p><a href="#quiz-${escape(q.id)}" data-feedback-target="quiz-${escape(q.id)}">回到題目 ${escape(q.id)}</a></li>`).join('')}</ol><p>此回饋對應已提交的作答。修改答案後，先重新檢查，再儲存回應。</p>`;
}
export function showAssessmentReview(element,questions,answers,result,check,focus=true,stale=false){
 element.innerHTML=(stale?'<p><strong>答案已不同於上次提交，請重新檢查目前答案。</strong></p>':'')+assessmentReviewHtml(questions,answers,result,check);
 element.className='feedback'+(result.passed?'':' error');
 for(const q of questions){const input=document.getElementById('quiz-'+q.id);if(input)input.setAttribute('aria-describedby','review-'+q.id);}
 element.onclick=event=>{const link=event.target.closest('[data-feedback-target]');if(!link)return;event.preventDefault();document.getElementById(link.dataset.feedbackTarget)?.focus();};
 element.tabIndex=-1;if(focus)element.focus();
}
