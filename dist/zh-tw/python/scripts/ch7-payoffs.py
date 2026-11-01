import math
def derivative_report(terminal,strike,premium):
    if not all(math.isfinite(x) and x >= 0 for x in [terminal,strike,premium]):
        raise ValueError("Use nonnegative finite amounts.")
    payoff = None # TODO_CALL
    return {"forward":None, # TODO_FORWARD
            "call":payoff,"profit":None} # TODO_PROFIT
if __name__ == "__main__":
    print(derivative_report(104,100,6))
