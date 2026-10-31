"""Optional reproducible capstone evidence, Python 3.8 standard library only."""
from textwrap import dedent

def code(s): return dedent(s).strip() + '\n'
def case(label,function,args,expected,hint): return dict(label=label,function=function,args=args,expected=expected,hint=hint)
EXERCISES=[dict(id='ch10-evidence',chapter=10,kind='Guided practice',minutes=15,title='Trace a net holding-period calculation',concept='Chapter 10 · hand check and calculation attachment',objective='Reproduce the first evaluation holding period with entry cost before return.',prediction='With £1000, entry101, exit97 and10bps entry cost, should end wealth be above or below £1000? Predict the approximate value.',instructions='Complete end_wealth for a fully invested long position entered from cash. Cost is charged against starting wealth at entry, before the open-to-open price ratio. This is one period, not the full strategy. A separate final exit, if applicable, would incur another cost; this function intentionally returns wealth before that exit.',syntax='10 basis points /10000 = .001. Multiply start by (1-cost_bps/10000), then by exit_open/entry_open. Do not subtract10 percent or use the close price.',hints=['Market factor = exit_open / entry_open.','The full expression is start * (1 - cost_bps / 10000) * exit_open / entry_open.'],reflection='State the information/execution timeline and explain why the result excludes a separate terminal-exit cost.',starter=code('''
    import math

    def holding_end(start, entry_open, exit_open, cost_bps):
        if not all(math.isfinite(x) for x in [start, entry_open, exit_open, cost_bps]) or min(start, entry_open, exit_open) <= 0 or not 0 <= cost_bps <= 100:
            raise ValueError("Use positive finite wealth/prices and cost 0–100bps.")
        return None  # TODO_END

    if __name__ == "__main__":
        print(holding_end(1000, 101, 97, 10))
'''),solution=None,replacements={'return None  # TODO_END':'return start * (1 - cost_bps / 10000) * exit_open / entry_open'},example=code('''
    start, entry, exit_price, bps = 1000, 100, 105, 10
    after_entry_cost = start * (1 - bps / 10000)
    print("After entry:", after_entry_cost)
    print("End before separate final exit:", after_entry_cost * exit_price / entry)
'''),cases=[case('Capstone first row','holding_end',[1000,101,97,10],959.4356435643564,'Charge£1 first, then the101→97 ratio.'),case('Changed cost','holding_end',[1000,101,97,30],957.5148514851485,'30bps is.003, not.03.'),case('Changed independent case','holding_end',[500,80,88,20],548.9,'Use the supplied starting wealth and both opens.')]),
dict(id='ch10-ledger',chapter=10,kind='Transfer challenge',minutes=20,title='Reproduce the full evaluation ledger',concept='Chapter 10 · rule, chronology, costs and same-date benchmark',objective='Complete the fixed rule ledger and reproduce both predefined cost cases.',prediction='Will the higher 30bps cost improve or reduce the fixed-position final wealth? Predict before running both cases.',instructions='The starter supplies all original synthetic opens/closes, chronological signal/entry/exit indices, switches and terminal liquidation. Complete the signal and cost-adjusted wealth expressions. It reports numeric summaries, while your core export retains complete rows. A signal at index t uses closes through t, executes open t+1 and earns open t+1→t+2. Do not shift returns backward.',syntax='Slice closes[t-2:t+1] contains three known closes. int(condition) converts a rule to0or1. abs(position-previous) is traded fraction. Final liquidation charges the final held position; benchmark pays entry and exit costs. No external packages or filesystem access.',hints=['position=int(closes[t] > sum(closes[t-2:t+1])/3).','wealth *= (1-turnover*c) * (1+position*(opens[t+2]/opens[t+1]-1)).'],reflection='Explain the first eligible entry and last exit, why all predefined costs must be retained, and why matching a synthetic ledger cannot prove real profitability.',starter=code('''
    def evaluate_block(cost_bps):
        if not 0 <= cost_bps <= 100:
            raise ValueError("Use cost0–100bps.")
        opens = [100,103,105,101,97,94,96,99,102,98,95,97,94,92,96,99]
        closes = [price + [1,-1,2,-2][i % 4] for i, price in enumerate(opens)]
        c = cost_bps / 10000
        wealth, previous, turnover_sum = 1000.0, 0, 0
        for t in range(2, len(opens) - 2):
            position = None  # TODO_SIGNAL
            turnover = abs(position - previous)
            wealth = None  # TODO_WEALTH
            turnover_sum += turnover
            previous = position
        wealth *= 1 - previous * c  # final liquidation, if invested
        benchmark = 1000 * (1-c) * opens[-1] / opens[3] * (1-c)
        return {"final": wealth, "benchmark": benchmark, "return_pct": (wealth/1000-1)*100, "traded_fraction": turnover_sum + previous}

    if __name__ == "__main__":
        print("10bps:", evaluate_block(10))
        print("30bps:", evaluate_block(30))
'''),solution=None,replacements={'position = None  # TODO_SIGNAL':'position = int(closes[t] > sum(closes[t-2:t+1]) / 3)','wealth = None  # TODO_WEALTH':'wealth = wealth * (1 - turnover * c) * (1 + position * (opens[t+2] / opens[t+1] - 1))'},example=code('''
    closes = [101, 102, 107]
    print("Known mean:", sum(closes) / 3)
    print("Position for next open:", int(closes[-1] > sum(closes) / 3))
    print("Do not earn returns before execution; retain all cost cases and losing results.")
'''),cases=[case('Base ledger','evaluate_block',[10],{'final':917.9113164465662,'benchmark':978.238603960396,'return_pct':-8.20886835534338,'traded_fraction':4},'Use t+1 entry and t+2 exit, cost before holding return.'),case('Cost sensitivity','evaluate_block',[30],{'final':910.582719824624,'benchmark':974.3256534653465,'return_pct':-8.94172801753761,'traded_fraction':4},'Keep the rule unchanged, with both cost cases reported.'),case('Zero-cost diagnostic','evaluate_block',[0],{'final':921.5921592159215,'benchmark':980.1980198019802,'return_pct':-7.8407840784078475,'traded_fraction':4},'Zero-cost is a diagnostic, not an extra selected headline trial.')])]
