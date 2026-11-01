import math
def derivative_report(terminal,strike,premium):
    if not all(math.isfinite(x) and x >= 0 for x in [terminal,strike,premium]):
        raise ValueError("Use nonnegative finite amounts.")
    payoff = max(terminal-strike,0)
    return {"forward":terminal-strike,
            "call":payoff,"profit":payoff-premium}
if __name__ == "__main__":
    print(derivative_report(104,100,6))
