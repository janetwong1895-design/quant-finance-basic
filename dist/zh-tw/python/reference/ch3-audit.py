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
            conflicts += len(prices)
        else:
            retained += 1
            duplicates += len(prices) - 1
    return dict(retained=retained, missing=missing,
                conflicts=conflicts, duplicates=duplicates)

if __name__ == "__main__":
    rows = [["2025-01-02", 50], ["2025-01-03", 51],
            ["2025-01-03", 51.5], ["2025-01-06", None],
            ["2025-01-07", 51], ["2025-01-08", 52.02],
            ["2025-01-08", 52.02]]
    print(audit_counts(rows))
