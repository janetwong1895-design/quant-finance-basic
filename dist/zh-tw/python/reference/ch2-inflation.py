def real_return(nominal_pct, inflation_pct):
    return ((1 + nominal_pct / 100) / (1 + inflation_pct / 100) - 1) * 100

def buying_power(nominal_balance, inflation_pct, years):
    return nominal_balance / (1 + inflation_pct / 100) ** years

if __name__ == "__main__":
    print("Real return (%):", real_return(3, 5))
    print("Buying power (£):", round(buying_power(1030, 5, 1), 2))
