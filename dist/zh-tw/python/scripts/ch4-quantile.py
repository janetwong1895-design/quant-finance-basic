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
