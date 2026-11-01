def present_value(payments, rate_pct):
    total = 0
    for year, amount in payments:
        discounted = amount / (1 + rate_pct / 100) ** year
        total += discounted
    return total

if __name__ == "__main__":
    bond = [(1, 20), (2, 1020)]
    print("Present value (NT$):", round(present_value(bond, 5), 2))
