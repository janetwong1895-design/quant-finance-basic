def summarise(principal, growth_pct, inflation_pct, years, future_payment):
    nominal = principal * (1 + growth_pct / 100) ** years
    real = nominal / (1 + inflation_pct / 100) ** years
    payment_pv = future_payment / (1 + growth_pct / 100) ** years
    return {"nominal": nominal, "real": real, "payment_pv": payment_pv}

if __name__ == "__main__":
    for inflation in [3, 6]:
        result = summarise(1000, 5, inflation, 10, 2000)
        print("Inflation scenario (%):", inflation)
        for label, amount in result.items():
            print(label, "(pounds):", round(amount, 2))
