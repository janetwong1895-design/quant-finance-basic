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
