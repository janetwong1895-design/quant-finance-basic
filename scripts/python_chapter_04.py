"""Self-contained optional Chapter 4 exercise definitions (Python 3.8+)."""
from textwrap import dedent


def code(s):
    return dedent(s).strip() + '\n'


def case(label, function, args, expected, hint):
    return dict(label=label, function=function, args=args, expected=expected, hint=hint)


EXERCISES = [
    dict(id='ch4-summary', chapter=4, kind='Guided practice', minutes=15,
         title='Summarise a tiny return sample', concept='Chapter 4 · observed frequency, centre and sample spread',
         objective='Calculate observed loss frequency, arithmetic mean, median and sample SD; explain their units and limits.',
         prediction='For [-2, 0, 2]%, predict mean, median, loss frequency and sample standard deviation before running.',
         instructions='Complete the four dictionary values. Use the standard-library statistics functions already imported. Inputs are percentage-unit returns, not decimals. A loss is strictly below zero; return its frequency on the 0–1 scale. Sample SD uses n−1 and is in percentage points. At least two finite observations are required. No external packages.',
         syntax='A dictionary maps quoted keys to values. statistics.mean, median and stdev accept lists. sum(value < 0 for value in returns_pct) counts True conditions. len returns the number of observations. Do not use pstdev: it uses n, not n−1.',
         hints=['Use mean(returns_pct), median(returns_pct) and stdev(returns_pct) for the three summaries.', 'Count strictly negative observations and divide by len(returns_pct); zero belongs to the complement.'],
         reflection='Explain why standard deviation uses percentage points, why zero is not a loss, and why this tiny invented sample does not establish future probabilities.',
         starter=code('''
            import math
            from statistics import mean, median, stdev

            def describe(returns_pct):
                if len(returns_pct) < 2 or not all(math.isfinite(x) for x in returns_pct):
                    raise ValueError("Supply at least two finite observations.")
                return {
                    "mean": None,  # TODO_MEAN
                    "median": None,  # TODO_MEDIAN
                    "sample_sd": None,  # TODO_SD
                    "loss_frequency": None,  # TODO_LOSS
                }

            if __name__ == "__main__":
                print(describe([-3, -1, 0, 1, 2, 7]))
         '''), solution=None,
         replacements={'None,  # TODO_MEAN':'mean(returns_pct),', 'None,  # TODO_MEDIAN':'median(returns_pct),', 'None,  # TODO_SD':'stdev(returns_pct),', 'None,  # TODO_LOSS':'sum(x < 0 for x in returns_pct) / len(returns_pct),'},
         example=code('''
            from statistics import mean, median, stdev
            values = [-2, 0, 2]  # Hypothetical monthly returns in percentage units.
            print("Mean (%):", mean(values))  # 0
            print("Median (%):", median(values))  # 0
            print("Sample SD (percentage points):", stdev(values))  # 2
            print("Observed loss frequency:", sum(x < 0 for x in values) / len(values))
         '''),
         cases=[case('Zero is not a loss', 'describe', [[-2, 0, 2]], {'mean':0,'median':0,'sample_sd':2,'loss_frequency':1/3}, 'Use n−1 and count only values below zero.'),
                case('Transfer sample', 'describe', [[-4, 0, 4, 8]], {'mean':2,'median':2,'sample_sd':(80/3)**.5,'loss_frequency':.25}, 'Use all observations and return numeric dictionary values.'),
                case('Constant series', 'describe', [[3, 3, 3]], {'mean':3,'median':3,'sample_sd':0,'loss_frequency':0}, 'A constant sample has zero spread, not missing data.')]),
    dict(id='ch4-quantile', chapter=4, kind='Guided practice', minutes=15,
         title='Declare the quantile convention', concept='Chapter 4 · sorted linear interpolation',
         objective='Implement inclusive quantiles using h=(n−1)p and explain differences from other conventions.',
         prediction='For [0, 10, 20, 40]%, predict the 25th and 75th percentiles under h=(n−1)p.',
         instructions='Complete the interpolation expression. The starter sorts the data and finds the lower and upper neighbours. p is a fraction between zero and one, so .25 means the 25th percentile. For p=1 both neighbours are the final observation. Keep full precision; round only printed output.',
         syntax='sorted creates a sorted copy. int(h) truncates a nonnegative position to its lower integer. Python list indices start at zero. The fraction h-lower is how far to move from the lower value toward the upper value.',
         hints=['Interpolate as lower_value + fraction × (upper_value − lower_value).', 'Use ordered[lower] + (h - lower) * (ordered[upper] - ordered[lower]).'],
         reflection='State the sorting rule, zero-based position and interpolation convention. Explain why a different software default can give a different small-sample quantile.',
         starter=code('''
            import math

            def inclusive_quantile(values, p):
                if not values or not all(math.isfinite(x) for x in values) or not 0 <= p <= 1:
                    raise ValueError("Use finite values and p between zero and one.")
                ordered = sorted(values)
                h = (len(ordered) - 1) * p
                lower = int(h)
                upper = min(lower + 1, len(ordered) - 1)
                return None  # TODO_INTERPOLATE

            if __name__ == "__main__":
                print("25th percentile (%):", inclusive_quantile([0, 10, 20, 40], .25))
         '''), solution=None,
         replacements={'return None  # TODO_INTERPOLATE':'return ordered[lower] + (h - lower) * (ordered[upper] - ordered[lower])'},
         example=code('''
            ordered = [0, 10, 20, 40]
            h = (len(ordered) - 1) * .75  # 2.25
            lower = int(h)  # 2: value 20
            fraction = h - lower  # .25
            result = ordered[lower] + fraction * (ordered[lower + 1] - ordered[lower])
            print("75th percentile (%):", result)  # 25
         '''),
         cases=[case('Interpolation', 'inclusive_quantile', [[0,10,20,40], .25],7.5,'Interpolate .75 of the distance from 0 to 10.'),
                case('Unsorted input', 'inclusive_quantile', [[20,0,8,4], .75],11,'Sort before finding position 2.25.'),
                case('Upper endpoint', 'inclusive_quantile', [[3,-2,9], 1],9,'The 100th percentile is the maximum.'),
                case('Median transfer', 'inclusive_quantile', [[-3,-1,0,1,2,7], .5],.5,'Interpolate between zero-based indices 2 and 3.')]),
    dict(id='ch4-correlation', chapter=4, kind='Transfer challenge', minutes=15,
         title='Preserve the date pairs', concept='Chapter 4 · Pearson correlation and undefined cases',
         objective='Implement Pearson correlation for aligned monthly rows; detect zero variance and reject causal overclaims.',
         prediction='What correlation do you expect when x=[-1,0,1] and y=[-2,0,2]? What if y is constant?',
         instructions='Complete covariance numerator and denominator calculations. Each row must already hold same-date asset returns; the starter rejects duplicate dates. Verify alignment in the source data before creating rows. Undefined correlation is reported as {"defined": 0, "r": 0}; this explicit flag means the numeric placeholder is not a correlation estimate. Do not interpret it as zero association. Defined cases use {"defined": 1, "r": value}. No statistics.correlation dependency, so this works on Python 3.8.',
         syntax='Each row is [date, x, y]. List comprehensions extract aligned values. zip pairs deviations without sorting. sum accumulates products; math.sqrt takes a square root. The defined flag is numeric to work with the shared exercise checker.',
         hints=['The numerator is sum((a - mx) * (b - my) for a, b in zip(x, y)).', 'The denominator is math.sqrt(xx * yy); when either squared-deviation sum is zero, use the explicit undefined flag supplied in the starter.'],
         reflection='Explain why row alignment matters, why zero variance makes r undefined, and why a nonzero sample association proves neither causation nor future stability.',
         starter=code('''
            import math

            def paired_report(rows):
                if len(rows) < 2 or len({r[0] for r in rows}) != len(rows):
                    raise ValueError("Supply at least two unique aligned date rows.")
                x = [r[1] for r in rows]
                y = [r[2] for r in rows]
                if not all(math.isfinite(v) for v in x + y):
                    raise ValueError("Returns must be finite.")
                if all(v == x[0] for v in x) or all(v == y[0] for v in y):
                    return {"defined": 0, "r": 0}  # Check identical observations before floating-point centring.
                mx, my = sum(x) / len(x), sum(y) / len(y)
                xx = sum((v - mx) ** 2 for v in x)
                yy = sum((v - my) ** 2 for v in y)
                if xx == 0 or yy == 0:
                    return {"defined": 0, "r": 0}  # Undefined: do not interpret placeholder as an r.
                numerator = None  # TODO_NUMERATOR
                denominator = None  # TODO_DENOMINATOR
                return {"defined": 1, "r": numerator / denominator}

            if __name__ == "__main__":
                print(paired_report([["Jan", -1, -2], ["Feb", 0, 0], ["Mar", 1, 2]]))
         '''), solution=None,
         replacements={'numerator = None  # TODO_NUMERATOR':'numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))', 'denominator = None  # TODO_DENOMINATOR':'denominator = math.sqrt(xx * yy)'},
         example=code('''
            import math
            x, y = [-1, 0, 1], [-2, 0, 2]  # Same three dates, not sorted independently.
            cross_products = 2 + 0 + 2
            print("Correlation:", cross_products / math.sqrt(2 * 8))  # 1
            print("An association in these pairs is not a causal explanation or forecast.")
         '''),
         cases=[case('Positive aligned line', 'paired_report', [[['Jan',-1,-2],['Feb',0,0],['Mar',1,2]]],{'defined':1,'r':1},'Sum paired deviation products.'),
                case('Negative association', 'paired_report', [[['Jan',-1,2],['Feb',0,0],['Mar',1,-2]]],{'defined':1,'r':-1},'Keep original pairs and signs.'),
                case('Undefined constant series', 'paired_report', [[['Jan',1,3],['Feb',2,3],['Mar',3,3]]],{'defined':0,'r':0},'The flag marks an undefined value; the placeholder is not a correlation.'),
                case('Undefined decimal constant', 'paired_report', [[[str(i), .3, i] for i in range(12)]],{'defined':0,'r':0},'Identical decimal observations have zero variance even when arithmetic rounding leaves a tiny residual.'),
                case('Zero linear association', 'paired_report', [[['Jan',-1,1],['Feb',0,-2],['Mar',1,1]]],{'defined':1,'r':0},'Zero linear correlation can coexist with a nonlinear pattern.')])
]
