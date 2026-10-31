def timing_audit(rows):
    if any(len(row) != 2 or not all(isinstance(v, int) for v in row) for row in rows):
        raise ValueError("Use [available_day, execution_day] integer pairs.")
    invalid = None  # TODO_INVALID
    return {"total": len(rows), "invalid": invalid, "valid": len(rows) - invalid}

if __name__ == "__main__":
    print(timing_audit([[1, 2], [3, 2], [4, 4]]))
