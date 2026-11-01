import math

def holding_end(start, entry_open, exit_open, cost_bps):
    if not all(math.isfinite(x) for x in [start, entry_open, exit_open, cost_bps]) or min(start, entry_open, exit_open) <= 0 or not 0 <= cost_bps <= 100:
        raise ValueError("Use positive finite wealth/prices and cost 0–100bps.")
    return None  # TODO_END

if __name__ == "__main__":
    print(holding_end(1000, 101, 97, 10))
