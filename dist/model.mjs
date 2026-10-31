export const VERSION='0.1.0';
export const STORAGE_KEY='qf-studio-chapter-01-v1';
export const STEPS=[['start','Welcome & setup',15],['readiness','Check your starting point',30],['markets','Meet the instruments',35],['case','Follow a worked case',25],['lab','Try the allocation lab',35],['assessment','Your independent check',25],['finish','Build your research card',15]];
export function freshState(){return {version:VERSION,fields:{},done:{},diagnostic:null,classification:null,labRuns:[],assessmentAttempts:[],plan:null,updated:null};}
export function restoreState(raw){try{const s=JSON.parse(raw);if(s?.version!==VERSION||!s.fields||typeof s.fields!=='object'||Array.isArray(s.fields)||!s.done||typeof s.done!=='object'||Array.isArray(s.done)||!Array.isArray(s.labRuns)||!Array.isArray(s.assessmentAttempts))return freshState();return {...freshState(),...s};}catch{return freshState();}}
export function allocate(weights,regime='steady'){
 if(!['steady','stress'].includes(regime))throw new Error('Choose the steady or stress scenario.');
 const values=weights.map(v=>v===''?NaN:Number(v));
 if(values.length!==3||values.some(v=>!Number.isFinite(v)||v<0||v>100)||Math.abs(values.reduce((a,b)=>a+b,0)-100)>0.001)throw new Error('Enter three weights from 0 to 100 that add to 100%.');
 const returns=regime==='stress'?[1,-5,-20]:[2,3,8];
 const gross=values.reduce((sum,w,i)=>sum+w/100*returns[i],0);
 return {weights:values,regime,returns,gross,ending:1000*(1+gross/100),benchmark:regime==='stress'?-9.8:4.8,fees:0};
}
export const DIAGNOSTIC=[
 {id:'d1',title:'£100 rises to £110. What is the percentage increase?',options:['10%','£10%','110%'],answer:0,feedback:['Correct: £10 ÷ £100 × 100 = 10%.','The change is £10, but the percentage is 10%. Units matter.','110% is the ending value as a percentage of the starting value. The increase is 10%.']},
 {id:'d2',title:'Half of a portfolio earns 4% and half earns 0%. What does the whole portfolio earn?',options:['4%','2%','8%'],answer:1,feedback:['Only half the money earns 4%. Multiply each return by its weight.','Correct: 0.5 × 4% + 0.5 × 0% = 2%.','Adding returns ignores how much money is in each investment.']},
 {id:'d3',title:'Which value can you use to describe a price change over time?',options:['A dated starting price and a dated ending price','Only the highest price','An unlabeled upward line'],answer:0,feedback:['Correct: both values and their dates are needed.','A maximum alone does not give the starting value, ending value or period.','Without dates and values, you cannot calculate the change.']}
];
export const INSTRUMENTS=[
 {id:'cash',name:'A deposit in a bank account',answer:'cash',hint:'It is a balance held at a bank; it is not ownership of a business.',explanation:'Cash deposit: access, interest and bank risk depend on the account and jurisdiction. Cash can lose purchasing power through inflation.'},
 {id:'bond',name:'A company promises interest and repayment at maturity',answer:'bond',hint:'Focus on the promise to repay borrowed money.',explanation:'Bond: a debt claim. Repayment is subject to default risk; market value can change before maturity.'},
 {id:'share',name:'A small ownership stake in one listed company',answer:'share',hint:'Ownership differs from lending money to the company.',explanation:'Share: part ownership. Dividends and price gains are uncertain, and losses are possible.'},
 {id:'fund',name:'A listed vehicle holding a basket of investments',answer:'fund',hint:'The vehicle pools investments; it is not necessarily one direct company stake.',explanation:'Fund / ETF: a pooled investment vehicle. The holdings determine its risks; a narrowly focused fund may not provide broad diversification.'}
];
export const ASSESSMENT_SETS=[
 [
  {id:'a1',clo:'CH1-01',title:'A city issues a security promising interest and repayment in five years. What is it?',options:['A share','A bond','A cash deposit'],answer:1,why:'A bond is a debt claim; the promise is subject to the issuer’s ability to pay.'},
  {id:'a2',clo:'CH1-01',title:'A fund invests only in three airline companies. Which statement is justified?',options:['It eliminates investment risk','It may remain concentrated in one sector','Its name guarantees diversification'],answer:1,why:'A fund can hold several investments while remaining concentrated in the same sector.'},
  {id:'a3',clo:'CH1-02',title:'Your rule is a 20% cash / 80% share portfolio over one year. Which is the fairest supplied benchmark?',options:['A matching 20% cash / 80% share buy-and-hold portfolio over the same dates and cost conventions','A bond fund over a different year','Whichever index makes the rule look best'],answer:0,critical:true,why:'Match the intended exposure and evaluate both approaches over the same dates and declared cost conventions.'},
  {id:'a4',clo:'CH1-03',title:'Which question is ready to investigate?',options:['Which strategy is best?','Will shares always rise?','Over the supplied 12 months, does rule A have a smaller maximum drawdown than its matching buy-and-hold benchmark, after the same declared costs?'],answer:2,why:'A testable question states a rule, comparator, period and measurable criterion. Maximum drawdown measures a fall from an earlier peak.'},
  {id:'a5',clo:'CH1-04',title:'On a hypothetical £1,000 portfolio, half earns 6% and half earns 0%. What is the ending value?',options:['£1,060','£1,030','£1,003'],answer:1,why:'The portfolio return is 0.5 × 6% = 3%. £1,000 × 1.03 = £1,030.'},
  {id:'a6',clo:'CH1-03',title:'The classroom simulation favours rule A. What can you conclude?',options:['Rule A will make money in real markets','The result holds in the supplied scenario; more evidence is needed for broader claims','A positive return proves the question was well designed'],answer:1,critical:true,why:'Synthetic data illustrate assumptions and mechanics. They do not establish real-world performance.'}
 ],
 [
  {id:'a1',clo:'CH1-01',title:'An investment gives you part ownership of a listed manufacturer. What is it?',options:['A bond','A share','A cash deposit'],answer:1,why:'A share represents ownership. It does not promise interest or repayment.'},
  {id:'a2',clo:'CH1-01',title:'An ETF owns businesses from a single industry. What should you check?',options:['Whether the holdings leave sector concentration','Only whether the label says ETF','Whether it can guarantee a positive return'],answer:0,why:'The holdings and their shared risks matter more than the pooled vehicle label.'},
  {id:'a3',clo:'CH1-02',title:'A rule targets a 40% cash / 60% bond allocation. Which benchmark fits?',options:['A stock index from a different decade','The worst-performing available fund','A 40% cash / 60% bond buy-and-hold baseline, using identical dates and cost conventions'],answer:2,critical:true,why:'Choose the benchmark for the intended exposure before seeing which comparison looks favourable.'},
  {id:'a4',clo:'CH1-03',title:'Which research question specifies observable evidence?',options:['Are ETFs good?','Over the supplied period, does the stated rebalancing rule reduce maximum drawdown against its matching baseline after declared costs?','What will definitely make me rich?'],answer:1,why:'The question names a rule, a comparator, a period and a measurable criterion rather than a promise.'},
  {id:'a5',clo:'CH1-04',title:'A hypothetical £1,000 portfolio has 40% earning 5% and 60% earning 0%. What is the ending value?',options:['£1,050','£1,005','£1,020'],answer:2,why:'0.40 × 5% + 0.60 × 0% = 2%. £1,000 × 1.02 = £1,020.'},
  {id:'a6',clo:'CH1-03',title:'Your toy portfolio loses money in the stress scenario. What is the appropriate next step?',options:['Hide the stress result','Record it, explain the assumptions and reconsider the claim','Repeat scenarios until one looks positive and report only that one'],answer:1,critical:true,why:'Losses are valid evidence. Report all tested scenarios and revise the claim when the evidence warrants it.'}
 ]
];
export function gradeQuestions(questions,answers){const details=questions.map(q=>({id:q.id,correct:Number.isInteger(answers[q.id])&&answers[q.id]===q.answer,critical:!!q.critical}));return {score:details.filter(d=>d.correct).length,total:questions.length,passed:details.filter(d=>d.correct).length>=5&&details.filter(d=>d.critical).every(d=>d.correct),details};}
export function currentAssessment(state){return ASSESSMENT_SETS[Number(state.fields.assessmentSet||0)%ASSESSMENT_SETS.length];}
export function chapterComplete(state){return STEPS.every(([id])=>state.done[id]===true);}
export function invalidateEvidence(state,id){
 let feedbackId=null;
 if(id==='setupConfirmed'&&!state.fields.setupConfirmed)delete state.done.start;
 if(['d1','d2','d3'].includes(id)){state.diagnostic=null;delete state.done.readiness;feedbackId='diagnostic-feedback';}
 if(id.startsWith('instrument-')){state.classification=null;delete state.done.markets;feedbackId='classification-feedback';}
 if(['casePrediction','caseGap'].includes(id)){delete state.done.case;feedbackId='case-feedback';}
 if(['labReflection','handCheck'].includes(id)){delete state.done.lab;feedbackId='lab-completion';if(id==='handCheck')state.fields.handVerified=false;}
 if(id.startsWith('quiz-')){state.fields.assessmentDirty=true;state.fields.revisionSaved=false;delete state.done.assessment;feedbackId='assessment-feedback';}
 if(id==='assessmentRevision'){state.fields.revisionSaved=false;delete state.done.assessment;feedbackId='revision-feedback';}
 if(id.startsWith('plan')){state.plan=null;delete state.done.finish;feedbackId='plan-feedback';}
 return feedbackId;
}
