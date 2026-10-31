"""Optional Chapter 6 exercises; standard-library Python 3.8+ only."""
from textwrap import dedent

def code(s):
    return dedent(s).strip() + '\n'

def case(label, function, args, expected, hint):
    return dict(label=label, function=function, args=args, expected=expected, hint=hint)

EXERCISES = [
    dict(id='ch6-weights', chapter=6, kind='Guided practice', minutes=20,
         title='Compare a policy with drift', concept='Chapter 6 · weighted return, constant mix and buy-and-hold',
         objective='Implement two cost-free policies on aligned monthly return pairs and distinguish ending wealth from target weights.',
         prediction='A has [+20,-20]% and B [0,0]%; start50/50. Predict constant-mix and buy-and-hold ending wealth from100.',
         instructions='Complete the weighted return, constant-mix update and separate sleeve updates. Input rows already pair same-date A/B total returns; verify alignment before constructing them. w_a is a starting/target fraction0–1; B gets1-w_a. Constant mix resets before each following month; buy-and-hold keeps units unchanged. No costs, taxes, flows or borrowing. A better result in one path is not a recommendation.',
         syntax='for a_return, b_return in rows unpacks each paired observation. A sleeve is the currency value invested in one asset. *= compounds a sleeve. Return a dictionary of numeric values.',
         hints=['weighted = w_a * a_return + (1 - w_a) * b_return.', 'Grow mix by1+weighted/100; grow each initial sleeve by its own monthly return.'],
         reflection='Explain why the buy-and-hold A weight drifts, when constant-mix resets and why omitted costs or another path can reverse the comparison.',
         starter=code('''
            import math

            def policy_report(rows, w_a):
                if not rows or not 0 <= w_a <= 1 or not all(math.isfinite(v) and v > -100 for row in rows for v in row):
                    raise ValueError("Use aligned finite return pairs above -100%, and A weight0-1.")
                mix, a_value, b_value = 100.0, 100*w_a, 100*(1-w_a)
                first_return = None
                for a_return, b_return in rows:
                    weighted = None  # TODO_WEIGHTED
                    if first_return is None:
                        first_return = weighted
                    mix *= None  # TODO_MIX
                    a_value *= None  # TODO_A
                    b_value *= None  # TODO_B
                return {"first_return": first_return, "constant_mix": mix,
                        "buy_hold": a_value+b_value, "ending_a_weight": a_value/(a_value+b_value)}

            if __name__ == "__main__":
                print(policy_report([[20,0],[-20,0]], .5))
         '''), solution=None,
         replacements={'weighted = None  # TODO_WEIGHTED':'weighted = w_a*a_return + (1-w_a)*b_return', 'mix *= None  # TODO_MIX':'mix *= 1 + weighted/100', 'a_value *= None  # TODO_A':'a_value *= 1 + a_return/100', 'b_value *= None  # TODO_B':'b_value *= 1 + b_return/100'},
         example=code('''
            w_a = .6
            first_return = w_a*10 + (1-w_a)*(-5)
            print("Weighted return (%):", first_return)  # 4
            print("Ending wealth:", 100*(1+first_return/100))  # 104
            print("Drifted A weight:", 60*1.1/(60*1.1+40*.95))
            print("Resetting target weights before the next month is a different policy.")
         '''),
         cases=[case('Reversal path', 'policy_report', [[[20,0],[-20,0]],.5], {'first_return':10,'constant_mix':99,'buy_hold':98,'ending_a_weight':48/98}, 'Buy-hold sleeves48 and50; constant mix110 then99.'),
                case('Trending counterexample', 'policy_report', [[[20,0],[20,0]],.5], {'first_return':10,'constant_mix':121,'buy_hold':122,'ending_a_weight':72/122}, 'The trending path reverses the winner; no universal policy advantage.'),
                case('New allocation', 'policy_report', [[[10,-5],[-10,5]],.8], {'first_return':7,'constant_mix':99.51,'buy_hold':99.15,'ending_a_weight':79.2/99.15}, 'Use .8/.2, not fixed .5/.5. Keep the original pairs.')]),
    dict(id='ch6-beta', chapter=6, kind='Transfer challenge', minutes=15,
         title='Keep sensitivity paired', concept='Chapter 6 · sample beta and Pearson correlation',
         objective='Calculate beta against benchmark variance, report undefined cases and distinguish slope from correlation.',
         prediction='For benchmark[-1,0,1]% and portfolio[-2,0,2]%, predict beta and correlation. Which changes if portfolio scale doubles?',
         instructions='Rows are [date, portfolio, benchmark] using aligned monthly simple total returns, without subtracting a risk-free series. Complete cross-product, beta and correlation expressions. Sample n-1 cancels in the ratio. Defined flags distinguish numeric zero from an undefined placeholder. A constant benchmark makes beta and correlation undefined; a constant portfolio with varying benchmark has beta0 and undefined correlation. This is a fitted sample slope with intercept, not a future promise.',
         syntax='List comprehensions select each aligned column. zip pairs deviations. math.sqrt makes the correlation denominator. defined flags are numeric for the public formative checker; a placeholder value with flag0 is not an estimate.',
         hints=['cross=sum((p-mp)*(m-mm) for p,m in zip(portfolio,market)).', 'Beta uses cross/market_squared_sum; correlation uses cross/sqrt(portfolio_squared_sum*market_squared_sum).'],
         reflection='Distinguish beta scale from correlation, preserve date pairs and explain the two different zero-variance cases and predictive limits.',
         starter=code('''
            import math

            def sensitivity_report(rows):
                if len(rows) < 2 or len({r[0] for r in rows}) != len(rows):
                    raise ValueError("Use two or more unique same-date rows.")
                portfolio, market = [r[1] for r in rows], [r[2] for r in rows]
                if not all(math.isfinite(x) for x in portfolio + market):
                    raise ValueError("Use finite same-frequency returns.")
                mp, mm = sum(portfolio)/len(rows), sum(market)/len(rows)
                pp = 0 if all(x == portfolio[0] for x in portfolio) else sum((x-mp)**2 for x in portfolio)
                bb = 0 if all(x == market[0] for x in market) else sum((x-mm)**2 for x in market)
                if bb == 0:
                    return {"beta_defined":0,"beta":0,"correlation_defined":0,"correlation":0}
                cross = None  # TODO_CROSS
                beta = None  # TODO_BETA
                if pp == 0:
                    return {"beta_defined":1,"beta":beta,"correlation_defined":0,"correlation":0}
                correlation = None  # TODO_CORRELATION
                return {"beta_defined":1,"beta":beta,"correlation_defined":1,"correlation":correlation}

            if __name__ == "__main__":
                print(sensitivity_report([["Jan",-2,-1],["Feb",0,0],["Mar",2,1]]))
         '''), solution=None,
         replacements={'cross = None  # TODO_CROSS':'cross = sum((p-mp)*(m-mm) for p,m in zip(portfolio,market))', 'beta = None  # TODO_BETA':'beta = cross / bb', 'correlation = None  # TODO_CORRELATION':'correlation = cross / math.sqrt(pp*bb)'},
         example=code('''
            import math
            cross, portfolio_ss, benchmark_ss = 4, 8, 2
            print("Sample beta:", cross/benchmark_ss)  # 2
            print("Sample Pearson correlation:", cross/math.sqrt(portfolio_ss*benchmark_ss))  # 1
            print("The n-1 covariance/variance factors cancel; beta is a sample slope, not a guaranteed next return.")
         '''),
         cases=[case('Scale versus association', 'sensitivity_report', [[['Jan',-2,-1],['Feb',0,0],['Mar',2,1]]], {'beta_defined':1,'beta':2,'correlation_defined':1,'correlation':1}, 'Beta2, correlation1. Use benchmark variance in the beta denominator.'),
                case('Negative slope transfer', 'sensitivity_report', [[['Jan',1,-2],['Feb',0,0],['Mar',-1,2]]], {'beta_defined':1,'beta':-.5,'correlation_defined':1,'correlation':-1}, 'Preserve signs and date pairs.'),
                case('Constant benchmark', 'sensitivity_report', [[['Jan',1,.3],['Feb',2,.3],['Mar',3,.3]]], {'beta_defined':0,'beta':0,'correlation_defined':0,'correlation':0}, 'All identical benchmark values mean exactly zero variance.'),
                case('Constant portfolio', 'sensitivity_report', [[['Jan',.3,-1],['Feb',.3,0],['Mar',.3,1]]], {'beta_defined':1,'beta':0,'correlation_defined':0,'correlation':0}, 'Beta0 is defined with varying benchmark; correlation is undefined.')])
]
