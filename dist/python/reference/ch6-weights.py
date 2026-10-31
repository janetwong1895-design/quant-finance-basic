import math

def policy_report(rows, w_a):
    if not rows or not 0 <= w_a <= 1 or not all(math.isfinite(v) and v > -100 for row in rows for v in row):
        raise ValueError("Use aligned finite return pairs above -100%, and A weight0-1.")
    mix, a_value, b_value = 100.0, 100*w_a, 100*(1-w_a)
    first_return = None
    for a_return, b_return in rows:
        weighted = w_a*a_return + (1-w_a)*b_return
        if first_return is None:
            first_return = weighted
        mix *= 1 + weighted/100
        a_value *= 1 + a_return/100
        b_value *= 1 + b_return/100
    return {"first_return": first_return, "constant_mix": mix,
            "buy_hold": a_value+b_value, "ending_a_weight": a_value/(a_value+b_value)}

if __name__ == "__main__":
    print(policy_report([[20,0],[-20,0]], .5))
