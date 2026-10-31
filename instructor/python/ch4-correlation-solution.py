import math

def paired_report(rows):
    if len(rows) < 2 or len({r[0] for r in rows}) != len(rows):
        raise ValueError("Supply at least two unique aligned date rows.")
    x = [r[1] for r in rows]
    y = [r[2] for r in rows]
    if not all(math.isfinite(v) for v in x + y):
        raise ValueError("Returns must be finite.")
    mx, my = sum(x) / len(x), sum(y) / len(y)
    xx = sum((v - mx) ** 2 for v in x)
    yy = sum((v - my) ** 2 for v in y)
    if xx == 0 or yy == 0:
        return {"defined": 0, "r": 0}  # Undefined: do not interpret placeholder as an r.
    numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denominator = math.sqrt(xx * yy)
    return {"defined": 1, "r": numerator / denominator}

if __name__ == "__main__":
    print(paired_report([["Jan", -1, -2], ["Feb", 0, 0], ["Mar", 1, 2]]))
