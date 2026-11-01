import math

def portfolio_return(weights, returns_pct):
    if len(weights) != 3 or len(returns_pct) != 3:
        raise ValueError("Supply three matching assets.")
    if any(w < 0 or w > 100 for w in weights):
        raise ValueError("Each weight must be between 0 and 100.")
    if not math.isclose(sum(weights), 100):
        raise ValueError("Weights must add to 100%.")
    total = 0
    for weight, asset_return in zip(weights, returns_pct):
        contribution = weight / 100 * asset_return
        total += contribution
    return total

if __name__ == "__main__":
    stress = [1, -5, -20]  # Cash, bonds, shares: synthetic annual returns (%).
    print("Baseline stress return (%):", portfolio_return([20, 40, 40], stress))
    print("Alternative stress return (%):", portfolio_return([50, 40, 10], stress))
