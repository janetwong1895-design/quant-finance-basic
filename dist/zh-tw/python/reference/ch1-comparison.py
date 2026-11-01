def ending_value(start, return_pct, fee_twd):
    # TODO: replace the next line with a calculation and return its result.
    return start * (1 + return_pct / 100) - fee_twd

if __name__ == "__main__":
    print("Baseline after fee (NT$):", ending_value(1000, 4.8, 5))
    print("Alternative after fee (NT$):", ending_value(1000, 3.0, 5))
