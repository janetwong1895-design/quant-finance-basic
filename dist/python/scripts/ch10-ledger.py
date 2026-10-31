def evaluate_block(cost_bps):
    if not 0 <= cost_bps <= 100:
        raise ValueError("Use cost0–100bps.")
    opens = [100,103,105,101,97,94,96,99,102,98,95,97,94,92,96,99]
    closes = [price + [1,-1,2,-2][i % 4] for i, price in enumerate(opens)]
    c = cost_bps / 10000
    wealth, previous, turnover_sum = 1000.0, 0, 0
    for t in range(2, len(opens) - 2):
        position = None  # TODO_SIGNAL
        turnover = abs(position - previous)
        wealth = None  # TODO_WEALTH
        turnover_sum += turnover
        previous = position
    wealth *= 1 - previous * c  # final liquidation, if invested
    benchmark = 1000 * (1-c) * opens[-1] / opens[3] * (1-c)
    return {"final": wealth, "benchmark": benchmark, "return_pct": (wealth/1000-1)*100, "traded_fraction": turnover_sum + previous}

if __name__ == "__main__":
    print("10bps:", evaluate_block(10))
    print("30bps:", evaluate_block(30))
