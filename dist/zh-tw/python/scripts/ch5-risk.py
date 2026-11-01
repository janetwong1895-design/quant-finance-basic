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
