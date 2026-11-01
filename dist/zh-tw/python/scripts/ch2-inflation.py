def real_return(nominal_pct, inflation_pct):
    raise NotImplementedError("TODO: return the exact real percentage.")

def buying_power(nominal_balance, inflation_pct, years):
    raise NotImplementedError("TODO: return starting-year purchasing power in TWD.")

if __name__ == "__main__":
    print("Real return (%):", real_return(3, 5))
    print("Buying power (NT$):", round(buying_power(1030, 5, 1), 2))
