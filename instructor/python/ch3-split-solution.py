def split_report(earlier_raw, later_raw, split_factor):
    earlier_adjusted = earlier_raw / split_factor
    raw_return = (later_raw / earlier_raw - 1) * 100
    adjusted_return = (later_raw / earlier_adjusted - 1) * 100
    return dict(earlier_adjusted=earlier_adjusted,
                raw_return=raw_return, adjusted_return=adjusted_return)

if __name__ == "__main__":
    print(split_report(100, 51, 2))
