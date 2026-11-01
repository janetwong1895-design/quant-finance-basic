# Hypothetical amounts; no deposits, withdrawals, fees or tax.
def percentage_change(start, end):
    return (end - start) / start * 100

if __name__ == "__main__":
    starting_value = 200
    ending_value = 210  # Try 190, predict, then run again.
    result = percentage_change(starting_value, ending_value)
    print("Percentage change:", result, "%")
