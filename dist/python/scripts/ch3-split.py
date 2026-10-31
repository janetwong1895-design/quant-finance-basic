def split_report(earlier_raw, later_raw, split_factor):
    earlier_adjusted = None  # TODO: use the post-split share basis.
    raw_return = None  # TODO: raw interval percentage change.
    adjusted_return = None  # TODO: split-consistent interval percentage return.
    return dict(earlier_adjusted=earlier_adjusted,
                raw_return=raw_return, adjusted_return=adjusted_return)

if __name__ == "__main__":
    print(split_report(100, 51, 2))
