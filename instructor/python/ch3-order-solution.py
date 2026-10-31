import csv
import io

def ordered_returns(rows):
    ordered = sorted(rows, key=lambda row: row[0])
    returns = []
    for earlier, later in zip(ordered, ordered[1:]):
        result = (later[1] / earlier[1] - 1) * 100
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
    csv_text = "date,adjusted\n2025-01-08,52.02\n2025-01-02,50\n2025-01-07,51\n"
    print("Interval price returns (%):", csv_returns(csv_text))
