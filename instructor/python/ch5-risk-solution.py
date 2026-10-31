import math
from statistics import stdev

def risk_summary(returns_pct):
    if len(returns_pct) < 2 or not all(math.isfinite(x) and x > -100 for x in returns_pct):
        raise ValueError("Use at least two finite monthly returns above -100%.")
    monthly_sd = stdev(returns_pct)
    value, peak, largest_loss = 100.0, 100.0, 0.0
    for monthly_return in returns_pct:
        value *= 1 + monthly_return / 100
        peak = max(peak, value)
        loss = 100 * (1 - value / peak)
        largest_loss = max(largest_loss, loss)
    return {"monthly_sd": monthly_sd,
            "annualised_sd": monthly_sd * math.sqrt(12),
            "maximum_drawdown": largest_loss, "ending_wealth": value}

if __name__ == "__main__":
    print(risk_summary([-20, 25]))
