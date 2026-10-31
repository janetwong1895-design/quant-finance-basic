import math

def trial_summary(values):
    if not values or not all(math.isfinite(x) for x in values):
        raise ValueError("Use a nonempty complete list of finite trial returns in %.")
    losses = sum(x < 0 for x in values)
    average = sum(values) / len(values)
    return {"trials": len(values), "losses": losses, "mean_pct": average, "best_pct": max(values)}

if __name__ == "__main__":
    print(trial_summary([-4, 0, 6, -2]))
