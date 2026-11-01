def present_value(payments, rate_pct):
    total = 0
    for year, amount in payments:
        discounted = None  # TODO: discount this payment using its year.
        total += discounted
    return total

if __name__ == "__main__":
    bond = [(1, 20), (2, 1020)]
    print("Present value (£):", round(present_value(bond, 5), 2))
