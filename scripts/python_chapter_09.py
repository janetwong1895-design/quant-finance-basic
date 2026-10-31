"""Optional Chapter 9 Python consolidation. Original synthetic inputs; no network."""
from textwrap import dedent

def code(s): return dedent(s).strip() + '\n'
def case(label,function,args,expected,hint): return dict(label=label,function=function,args=args,expected=expected,hint=hint)
EXERCISES=[dict(id='ch9-audit',chapter=9,kind='Guided practice',minutes=15,title='Check information and execution dates',concept='Chapter 9 · chronological audit',objective='Count invalid timing rows without using future information.',prediction='If a signal is available on day 3 but execution is day 2, can that trade use the signal? Predict the audit count.',instructions='Rows are [available_day, execution_day]. Day numbers are ordered integers in one synthetic calendar. The close-based signal must execute on a STRICTLY LATER day. Count executions at or before information availability. This is a mechanical timing screen, not proof that all leakage is absent.',syntax='sum(condition for row in rows) counts True values. A <= comparison includes equality. Dictionary outputs are numeric so the shared checker can compare them.',hints=['A close-based signal available on day t cannot execute at an earlier day or that same day open.','Count execution <= available. Return total, invalid and valid counts.'],reflection='Explain the same-day open violation and name one leakage source that this tiny date screen cannot detect.',starter=code('''
    def timing_audit(rows):
        if any(len(row) != 2 or not all(isinstance(v, int) for v in row) for row in rows):
            raise ValueError("Use [available_day, execution_day] integer pairs.")
        invalid = None  # TODO_INVALID
        return {"total": len(rows), "invalid": invalid, "valid": len(rows) - invalid}

    if __name__ == "__main__":
        print(timing_audit([[1, 2], [3, 2], [4, 4]]))
'''),solution=None,replacements={'invalid = None  # TODO_INVALID':'invalid = sum(execution <= available for available, execution in rows)'},example=code('''
    rows = [[1, 2], [3, 2], [4, 4]]
    for available, execution in rows:
        print(available, execution, "invalid" if execution <= available else "later execution")
'''),cases=[case('Earlier and same-day errors','timing_audit',[[[1,2],[3,2],[4,4]]],{'total':3,'invalid':2,'valid':1},'Same-day open is before the signal close.'),case('Changed dates','timing_audit',[[[5,6],[7,9],[8,7],[9,9]]],{'total':4,'invalid':2,'valid':2},'Use the available/execution pair, not list order.'),case('No rows','timing_audit',[[]],{'total':0,'invalid':0,'valid':0},'An empty audit counts zero; it establishes no evidence.')]),
dict(id='ch9-trials',chapter=9,kind='Transfer challenge',minutes=20,title='Keep the losing trials',concept='Chapter 9 · selection and trial retention',objective='Summarise every supplied trial without filtering by sign.',prediction='For net trial returns [-4, 0, 6, -2]%, how many losing trials and what mean do you expect?',instructions='Inputs are percentage-unit net returns from ALL supplied trials. Complete loss count and arithmetic mean. This descriptive mean is not expected future strategy return and does not correct multiple testing. Zero is neither a win nor a loss. Retain all four values in your log.',syntax='sum(values)/len(values) is the arithmetic mean. sum(x < 0 for x in values) counts losses. Do not replace the input with positive returns.',hints=['Keep negatives and zero in the denominator.','Count values strictly below zero; mean all values, not just the winning trial.'],reflection='Why would reporting only the maximum create a misleading impression? Explain why averaging all tried strategies still does not establish deployability.',starter=code('''
    import math

    def trial_summary(values):
        if not values or not all(math.isfinite(x) for x in values):
            raise ValueError("Use a nonempty complete list of finite trial returns in %.")
        losses = None  # TODO_LOSSES
        average = None  # TODO_MEAN
        return {"trials": len(values), "losses": losses, "mean_pct": average, "best_pct": max(values)}

    if __name__ == "__main__":
        print(trial_summary([-4, 0, 6, -2]))
'''),solution=None,replacements={'losses = None  # TODO_LOSSES':'losses = sum(x < 0 for x in values)','average = None  # TODO_MEAN':'average = sum(values) / len(values)'},example=code('''
    values = [-4, 0, 6, -2]
    print("All trial count:", len(values))
    print("Complete-log sum (%):", sum(values))
    print("Reporting only", max(values), "would hide losses and selection.")
'''),cases=[case('Complete log','trial_summary',[[-4,0,6,-2]],{'trials':4,'losses':2,'mean_pct':0,'best_pct':6},'Include all four trials.'),case('All unfavourable','trial_summary',[[-1,-3]],{'trials':2,'losses':2,'mean_pct':-2,'best_pct':-1},'The best trial can still be negative.'),case('Zero and changed cases','trial_summary',[[0,2,4]],{'trials':3,'losses':0,'mean_pct':2,'best_pct':4},'Zero is not a loss; do not omit it.')])]
