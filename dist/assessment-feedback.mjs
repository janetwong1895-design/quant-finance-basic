const escape=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function assessmentReviewHtml(questions,answers,result,check){
 const missing=questions.filter(q=>q.critical&&!check(q,answers[q.id]));
 return `<p><strong>${result.score}/${questions.length}. ${result.passed?'Criteria met; now record a feedback response.':'Revise and resubmit.'}</strong></p>${missing.length?`<p>Not yet passed: required critical questions ${missing.map(q=>escape(q.id)).join(', ')} need correction, even if the total score meets the threshold.</p>`:''}<ol class="assessment-review">${questions.map(q=>`<li id="review-${escape(q.id)}"><strong>${escape(q.id)}: ${check(q,answers[q.id])?'Correct':'Revisit'}${q.critical?' · Critical question':''}</strong><p>${escape(q.hint)}</p><a href="#quiz-${escape(q.id)}" data-feedback-target="quiz-${escape(q.id)}">Return to question ${escape(q.id)}</a></li>`).join('')}</ol><p>This feedback is for your submitted attempt. After editing answers, check the attempt again before saving your response.</p>`;
}
export function showAssessmentReview(element,questions,answers,result,check,focus=true,stale=false){
 element.innerHTML=(stale?'<p><strong>Answers have changed since this submitted attempt. Check your current answers again.</strong></p>':'')+assessmentReviewHtml(questions,answers,result,check);
 element.className='feedback'+(result.passed?'':' error');
 for(const q of questions){const input=document.getElementById('quiz-'+q.id);if(input)input.setAttribute('aria-describedby','review-'+q.id);}
 element.onclick=event=>{const link=event.target.closest('[data-feedback-target]');if(!link)return;event.preventDefault();document.getElementById(link.dataset.feedbackTarget)?.focus();};
 element.tabIndex=-1;if(focus)element.focus();
}
