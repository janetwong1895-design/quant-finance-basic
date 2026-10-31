import math
from statistics import mean, median, stdev

def describe(returns_pct):
    if len(returns_pct) < 2 or not all(math.isfinite(x) for x in returns_pct):
        raise ValueError("Supply at least two finite observations.")
    return {
        "mean": mean(returns_pct),
        "median": median(returns_pct),
        "sample_sd": stdev(returns_pct),
        "loss_frequency": sum(x < 0 for x in returns_pct) / len(returns_pct),
    }

if __name__ == "__main__":
    print(describe([-3, -1, 0, 1, 2, 7]))
