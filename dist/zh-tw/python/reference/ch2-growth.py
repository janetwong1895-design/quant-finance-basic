def future_value(principal, rate_pct, years):
    return principal * (1 + rate_pct / 100) ** years

def cagr(start, end, years):
    return ((end / start) ** (1 / years) - 1) * 100

if __name__ == "__main__":
    print("Future value (NT$):", future_value(500, 8, 2))
    print("CAGR (%):", cagr(1000, 1331, 3))
