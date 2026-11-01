def future_value(principal, rate_pct, years):
    raise NotImplementedError("TODO: compound the annual growth factor.")

def cagr(start, end, years):
    raise NotImplementedError("TODO: find the equivalent annual percentage rate.")

if __name__ == "__main__":
    print("Future value (£):", future_value(500, 8, 2))
    print("CAGR (%):", cagr(1000, 1331, 3))
