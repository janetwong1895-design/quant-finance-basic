def summarise(principal, growth_pct, inflation_pct, years, future_payment):
    nominal = None  # TODO: compound the principal.
    real = None  # TODO: express nominal balance in starting-year pounds.
    payment_pv = None  # TODO: discount the separate future payment.
    return {"nominal": nominal, "real": real, "payment_pv": payment_pv}

if __name__ == "__main__":
    for inflation in [3, 6]:
        result = summarise(1000, 5, inflation, 10, 2000)
        print("Inflation scenario (%):", inflation)
        for label, amount in result.items():
            print(label, "(pounds):", round(amount, 2))
