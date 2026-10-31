"""Optional Chapter 3 Python exercises; consumed by build-python-practice.py."""
import textwrap


def code(text):
    return textwrap.dedent(text).strip() + "\n"


def case(label, function, args, expected, hint):
    return dict(label=label, function=function, args=args, expected=expected, hint=hint)


EXERCISES = [
    dict(id="ch3-order", chapter=3, kind="Guided practice", minutes=15,
         title="Sort before taking a return", concept="Chapter 3 · chronological observations",
         objective="Sort ISO-date observations and calculate adjacent interval price returns.",
         prediction="The input arrives as 8 January £52.02, 2 January £50, 7 January £51. Predict the first chronological interval return.",
         instructions="Complete both TODO expressions. The supplied csv_returns wrapper reads CSV with csv.DictReader, converts price strings using float, and passes [ISO date, split-adjusted price] rows to your function. Inputs here have unique valid dates and positive prices; the next activity handles quality defects. Return a dictionary of the first and last interval percentages and cumulative percentage, not rounded strings. At least two observations are supplied. The first observation has no return. Gaps remain observed intervals, not daily returns.",
         syntax="csv.DictReader returns dictionary fields as strings; float converts price strings to numbers. io.StringIO makes CSV text readable like a file. sorted(rows, key=...) returns a new list. lambda row: row[0] selects its ISO date as a sorting key. zip pairs the earlier rows with ordered[1:], the list starting at its second item. append adds a result to a list.",
         hints=["Fixed-width ISO dates sort in chronological order. Use key=lambda row: row[0].", "For each earlier/later pair use (later[1] / earlier[1] - 1) * 100."],
         reflection="Name the actual date intervals. Explain why file order and a daily label would be misleading, and why the first observation has no return.",
         starter=code('''
            import csv
            import io

            def ordered_returns(rows):
                ordered = None  # TODO: sort a copy by ISO date.
                returns = []
                for earlier, later in zip(ordered, ordered[1:]):
                    result = None  # TODO: interval return in percentage units.
                    returns.append(result)
                total = 1
                for result in returns:
                    total *= 1 + result / 100
                return dict(first=returns[0], last=returns[-1], cumulative=(total - 1) * 100)

            def csv_returns(csv_text):
                reader = csv.DictReader(io.StringIO(csv_text))
                rows = [[row["date"], float(row["adjusted"])] for row in reader]
                return ordered_returns(rows)

            if __name__ == "__main__":
                csv_text = "date,adjusted\\n2025-01-08,52.02\\n2025-01-02,50\\n2025-01-07,51\\n"
                print("Interval price returns (%):", csv_returns(csv_text))
         '''),
         replacements={"ordered = None  # TODO: sort a copy by ISO date.": "ordered = sorted(rows, key=lambda row: row[0])",
                       "result = None  # TODO: interval return in percentage units.": "result = (later[1] / earlier[1] - 1) * 100"},
         example=code('''
            # ISO strings, not ambiguous day/month strings.
            rows = [["2025-03-06", 84], ["2025-03-01", 80]]
            ordered = sorted(rows, key=lambda row: row[0])
            print("From", ordered[0][0], "to", ordered[1][0])
            print("Interval return (%):", (ordered[1][1] / ordered[0][1] - 1) * 100)  # 5
         '''),
         cases=[case("Shuffled split-consistent file", "csv_returns", ["date,adjusted\n2025-01-08,52.02\n2025-01-02,50\n2025-01-07,51\n"], dict(first=2, last=2, cumulative=4.04), "Sort dates, not prices or original row order."),
                case("A falling interval", "csv_returns", ["date,adjusted\n2025-02-05,95\n2025-02-01,100\n"], dict(first=-5, last=-5, cumulative=-5), "The older price is the denominator."),
                case("Already ordered with a gap", "csv_returns", ["date,adjusted\n2025-03-01,80\n2025-03-04,84\n2025-03-09,84\n"], dict(first=5, last=0, cumulative=5), "Do not insert zero-return observations for absent dates.")]),
    dict(id="ch3-audit", chapter=3, kind="Guided practice", minutes=20,
         title="Count every cleaning decision", concept="Chapter 3 · transparent quality audit",
         objective="Implement a conservative missing/duplicate/conflict policy and report audit counts.",
         prediction="Five rows contain one exact duplicate and two different prices on one date. How many rows will remain after exact deduplication and conflict quarantine?",
         instructions="Rows contain [date, price] on one consistently adjusted basis. Valid ISO dates are supplied. Complete the counting and retention TODOs; the grouping logic is provided. Return a dictionary with retained, missing, conflicts and duplicates. Counts describe original removed rows, except duplicates counts redundant exact copies. If a date has multiple distinct valid prices, quarantine every row on that date. Unknown prices are excluded first. No filling occurs.",
         syntax="A dictionary maps keys to values. set removes identical values. len counts items. continue skips to the next loop item. The supplied groups.setdefault(date, []).append(price) collects valid prices for each date. None means unknown here.",
         hints=["Each None price increments missing, then continue prevents adding it to groups.", "If a date has conflicting distinct prices, all len(prices) rows count as conflicts. Otherwise retain one and count len(prices) - 1 redundant copies."],
         reflection="Explain the unit of each audit count, the retained observation count and why quarantining conflict does not recover the true price.",
         starter=code('''
            def audit_counts(rows):
                groups = {}
                missing = 0
                for date, price in rows:
                    if price is None:
                        missing += 1
                        continue
                    groups.setdefault(date, []).append(price)
                retained = conflicts = duplicates = 0
                for date, prices in groups.items():
                    if len(set(prices)) > 1:
                        conflicts += None  # TODO: number of original rows quarantined.
                    else:
                        retained += None  # TODO: how many observations survive this date?
                        duplicates += None  # TODO: redundant identical copies.
                return dict(retained=retained, missing=missing,
                            conflicts=conflicts, duplicates=duplicates)

            if __name__ == "__main__":
                rows = [["2025-01-02", 50], ["2025-01-03", 51],
                        ["2025-01-03", 51.5], ["2025-01-06", None],
                        ["2025-01-07", 51], ["2025-01-08", 52.02],
                        ["2025-01-08", 52.02]]
                print(audit_counts(rows))
         '''),
         replacements={"conflicts += None  # TODO: number of original rows quarantined.": "conflicts += len(prices)",
                       "retained += None  # TODO: how many observations survive this date?": "retained += 1",
                       "duplicates += None  # TODO: redundant identical copies.": "duplicates += len(prices) - 1"},
         example=code('''
            # Worked exact duplicate: both date and price agree.
            prices_for_one_date = [50, 50, 50]
            distinct_values = set(prices_for_one_date)
            print("Distinct values:", len(distinct_values))  # 1
            print("Retained:", 1)
            print("Redundant copies:", len(prices_for_one_date) - 1)  # 2
            print("A conflicting date needs source investigation, not averaging.")
         '''),
         cases=[case("Mixed audit", "audit_counts", [[["2025-01-02", 50], ["2025-01-03", 51], ["2025-01-03", 51.5], ["2025-01-06", None], ["2025-01-07", 51], ["2025-01-08", 52.02], ["2025-01-08", 52.02]]], dict(retained=3, missing=1, conflicts=2, duplicates=1), "Classify every original row exactly once as retained or removed."),
                case("Changed conflict case", "audit_counts", [[["2025-02-01", 80], ["2025-02-01", 80], ["2025-02-02", 81], ["2025-02-02", 82], ["2025-02-03", 84]]], dict(retained=2, missing=0, conflicts=2, duplicates=1), "Conflicting values are both quarantined; one exact copy is retained."),
                case("Only missing observations", "audit_counts", [[["2025-03-01", None], ["2025-03-02", None]]], dict(retained=0, missing=2, conflicts=0, duplicates=0), "Do not turn None into a zero price.")]),
    dict(id="ch3-split", chapter=3, kind="Transfer challenge", minutes=15,
         title="Keep the share basis consistent", concept="Chapter 3 · split-adjusted price returns",
         objective="Adjust an earlier raw price for a verified split, then report raw and adjusted interval returns.",
         prediction="A raw £100 becomes £51 after a two-for-one split. Predict the raw price change and split-consistent price return.",
         instructions="Use split_factor as new shares per old share. The split is independently verified; do not infer it from a price fall. The later price is already post-split. Complete earlier_adjusted and both returns. No dividends, other actions, fees or taxes; this is price return only. Return a dictionary; keep numerical precision.",
         syntax="Divide the older raw price by the split factor to express both prices in new-share units. A dictionary literal uses braces and key: value pairs. Use each function argument so new cases work.",
         hints=["Earlier adjusted price = earlier_raw / split_factor.", "Use later_raw / earlier_raw - 1 for raw, and later_raw / earlier_adjusted - 1 for split-consistent return; multiply each by 100."],
         reflection="Explain the share-count arithmetic and why raw −49% does not prove a 49% wealth loss. State why the result is not dividend-inclusive total return.",
         starter=code('''
            def split_report(earlier_raw, later_raw, split_factor):
                earlier_adjusted = None  # TODO: use the post-split share basis.
                raw_return = None  # TODO: raw interval percentage change.
                adjusted_return = None  # TODO: split-consistent interval percentage return.
                return dict(earlier_adjusted=earlier_adjusted,
                            raw_return=raw_return, adjusted_return=adjusted_return)

            if __name__ == "__main__":
                print(split_report(100, 51, 2))
         '''),
         replacements={"earlier_adjusted = None  # TODO: use the post-split share basis.": "earlier_adjusted = earlier_raw / split_factor",
                       "raw_return = None  # TODO: raw interval percentage change.": "raw_return = (later_raw / earlier_raw - 1) * 100",
                       "adjusted_return = None  # TODO: split-consistent interval percentage return.": "adjusted_return = (later_raw / earlier_adjusted - 1) * 100"},
         example=code('''
            # A pure two-for-one split: one old share -> two new shares.
            old_price = 120
            new_price = 60
            new_shares_per_old = 2
            print("Wealth before:", old_price * 1)
            print("Wealth after:", new_price * new_shares_per_old)
            print("Earlier price in new-share units:", old_price / new_shares_per_old)
         '''),
         cases=[case("Main split case", "split_report", [100, 51, 2], dict(earlier_adjusted=50, raw_return=-49, adjusted_return=2), "Divide the older price by the new-shares-per-old factor."),
                case("Pure split", "split_report", [202, 101, 2], dict(earlier_adjusted=101, raw_return=-50, adjusted_return=0), "A pure split does not change wealth."),
                case("New three-for-one split", "split_report", [90, 31.5, 3], dict(earlier_adjusted=30, raw_return=-65, adjusted_return=5), "Do not hard-code the factor two."),
                case("No split", "split_report", [80, 84, 1], dict(earlier_adjusted=80, raw_return=5, adjusted_return=5), "A factor of one leaves the price basis unchanged.")])
]
