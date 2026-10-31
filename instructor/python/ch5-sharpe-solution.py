import math
from statistics import mean, stdev

def sharpe_report(returns_pct, annual_effective_pct):
    if len(returns_pct) < 2 or not all(math.isfinite(x) for x in returns_pct):
        raise ValueError("Supply two or more finite monthly returns.")
    if not math.isfinite(annual_effective_pct) or annual_effective_pct <= -100:
        raise ValueError("Annual effective rate must exceed -100%.")
    monthly_rf = 100 * ((1 + annual_effective_pct / 100) ** (1 / 12) - 1)
    excess = [value - monthly_rf for value in returns_pct]
    if all(x == excess[0] for x in excess):
        return {"defined": 0, "sharpe": 0, "monthly_rf": monthly_rf}
    ratio = math.sqrt(12) * mean(excess) / stdev(excess)
    return {"defined": 1, "sharpe": ratio, "monthly_rf": monthly_rf}

if __name__ == "__main__":
    print(sharpe_report([-1,1,3], 0))
