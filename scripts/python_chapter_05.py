"""Optional Chapter 5 exercises; standard-library Python 3.8+ only."""
from textwrap import dedent

def code(s):
    return dedent(s).strip() + '\n'

def case(label, function, args, expected, hint):
    return dict(label=label, function=function, args=args, expected=expected, hint=hint)

EXERCISES = [
    dict(id='ch5-risk', chapter=5, kind='Guided practice', minutes=20,
         title='Include the initial peak', concept='Chapter 5 · sample spread and observed drawdown',
         objective='Calculate sample monthly SD, conditional annualised SD and a positive maximum-drawdown magnitude.',
         prediction='Compare [-20,25]% with [0,0]%. Both end where they started: will SD and maximum drawdown match?',
         instructions='Complete the sample-SD, annual scaling, wealth-update and loss-from-peak expressions. Returns use percentage units. Start wealth at100 and include it in the running peak. Maximum drawdown is a positive magnitude; individual drawdowns could be signed negative elsewhere. At least two finite returns above -100% are required. Annual SD uses sqrt(12), conditional on independent, identically distributed monthly returns. No fees or flows.',
         syntax='stdev uses sample n-1. math.sqrt is square root. wealth *= factor updates a variable by multiplication. max compares the running peak and current wealth. Dictionaries return named numeric results.',
         hints=['Use stdev(returns_pct), then monthly_sd * math.sqrt(12).', 'Update wealth *= 1 + value/100; update peak before computing 100*(1-wealth/peak).'],
         reflection='Explain the initial peak, positive loss-magnitude convention, SD units and a limitation of square-root-of-time scaling or monthly observations.',
         starter=code('''
            import math
            from statistics import stdev

            def risk_summary(returns_pct):
                if len(returns_pct) < 2 or not all(math.isfinite(x) and x > -100 for x in returns_pct):
                    raise ValueError("Use at least two finite monthly returns above -100%.")
                monthly_sd = None  # TODO_SD
                value, peak, largest_loss = 100.0, 100.0, 0.0
                for monthly_return in returns_pct:
                    value *= None  # TODO_GROW
                    peak = max(peak, value)
                    loss = None  # TODO_LOSS
                    largest_loss = max(largest_loss, loss)
                return {"monthly_sd": monthly_sd,
                        "annualised_sd": None,  # TODO_ANNUAL
                        "maximum_drawdown": largest_loss, "ending_wealth": value}

            if __name__ == "__main__":
                print(risk_summary([-20, 25]))
         '''), solution=None,
         replacements={'monthly_sd = None  # TODO_SD':'monthly_sd = stdev(returns_pct)', 'value *= None  # TODO_GROW':'value *= 1 + monthly_return / 100', 'loss = None  # TODO_LOSS':'loss = 100 * (1 - value / peak)', '"annualised_sd": None,  # TODO_ANNUAL':'"annualised_sd": monthly_sd * math.sqrt(12),'},
         example=code('''
            import math
            from statistics import stdev
            values = [-2, 0, 2]
            print("Monthly sample SD (percentage points):", stdev(values))
            print("Annualised estimate, IID-month assumption:", stdev(values) * math.sqrt(12))
            wealth = [100, 80, 100]  # [-20%, +25%], including initial wealth.
            print("Observed maximum drawdown (% magnitude):", 100 * (1 - min(wealth) / 100))
            print("This observed loss is not a future bound.")
         '''),
         cases=[case('Initial peak and recovery', 'risk_summary', [[-20,25]], {'monthly_sd':45/(2**.5),'annualised_sd':45/(2**.5)*12**.5,'maximum_drawdown':20,'ending_wealth':100}, 'Include initial100; sample SD uses n-1.'),
                case('Same ending, different path', 'risk_summary', [[0,0]], {'monthly_sd':0,'annualised_sd':0,'maximum_drawdown':0,'ending_wealth':100}, 'Constant wealth has no spread or observed drawdown.'),
                case('New transfer path', 'risk_summary', [[-2,0,2]], {'monthly_sd':2,'annualised_sd':2*12**.5,'maximum_drawdown':2,'ending_wealth':99.96}, 'Sample SD2; initial100 still belongs in peak history.')]),
    dict(id='ch5-sharpe', chapter=5, kind='Transfer challenge', minutes=15,
         title='Match the risk-free frequency', concept='Chapter 5 · monthly excess returns and Sharpe',
         objective='Convert an annual effective risk-free rate, calculate a declared annualised Sharpe and report zero-variance cases explicitly.',
         prediction='For [-1,1,3]% monthly, predict whether moving annual effective risk-free from0% to12% changes sample excess SD or Sharpe.',
         instructions='Complete the effective monthly rate, excess list and ratio. The report flag defined=0 means Sharpe is undefined; its sharpe=0 placeholder is not an estimate. The starter handles constant excess returns explicitly. Annualisation by sqrt(12) assumes independent stationary monthly excess returns; no future-performance inference follows. Keep percentage units throughout.',
         syntax='** raises a power; 1/12 is a fraction. [value - monthly_rf for value in returns_pct] transforms every monthly return. stdev supplies n-1; mean supplies arithmetic mean. Return numeric flags for the public checker.',
         hints=['monthly_rf = 100 * ((1 + annual_effective_pct / 100) ** (1/12) - 1).', 'Compute excess at monthly frequency, then sqrt(12) * mean(excess) / stdev(excess).'],
         reflection='State the frequency conversion and sample denominator, explain why a constant risk-free shift leaves SD unchanged, and qualify annual scaling.',
         starter=code('''
            import math
            from statistics import mean, stdev

            def sharpe_report(returns_pct, annual_effective_pct):
                if len(returns_pct) < 2 or not all(math.isfinite(x) for x in returns_pct):
                    raise ValueError("Supply two or more finite monthly returns.")
                if not math.isfinite(annual_effective_pct) or annual_effective_pct <= -100:
                    raise ValueError("Annual effective rate must exceed -100%.")
                monthly_rf = None  # TODO_RF
                excess = None  # TODO_EXCESS
                if all(x == excess[0] for x in excess):
                    return {"defined": 0, "sharpe": 0, "monthly_rf": monthly_rf}
                ratio = None  # TODO_RATIO
                return {"defined": 1, "sharpe": ratio, "monthly_rf": monthly_rf}

            if __name__ == "__main__":
                print(sharpe_report([-1,1,3], 0))
         '''), solution=None,
         replacements={'monthly_rf = None  # TODO_RF':'monthly_rf = 100 * ((1 + annual_effective_pct / 100) ** (1 / 12) - 1)', 'excess = None  # TODO_EXCESS':'excess = [value - monthly_rf for value in returns_pct]', 'ratio = None  # TODO_RATIO':'ratio = math.sqrt(12) * mean(excess) / stdev(excess)'},
         example=code('''
            from statistics import mean, stdev
            import math
            excess = [-1,1,3]  # Monthly percentage-point excess, risk-free0%.
            print("Mean excess:", mean(excess), "Sample SD:", stdev(excess))
            print("Annualised Sharpe, independent-month assumption:", math.sqrt(12)*mean(excess)/stdev(excess))
            print("Zero excess variance means undefined, not a zero Sharpe.")
         '''),
         cases=[case('Declared sample ratio', 'sharpe_report', [[-1,1,3],0], {'defined':1,'sharpe':12**.5/2,'monthly_rf':0}, 'Mean1 / sample SD2; multiply by sqrt12.'),
                case('Effective annual conversion', 'sharpe_report', [[-1,1,3],12], {'defined':1,'sharpe':12**.5*(1-100*(1.12**(1/12)-1))/2,'monthly_rf':100*(1.12**(1/12)-1)}, 'Convert before monthly subtraction; do not divide12 by12.'),
                case('Non-binary constant', 'sharpe_report', [[.3]*12,0], {'defined':0,'sharpe':0,'monthly_rf':0}, 'All equal observations have exactly zero variance; report undefined.')])
]
