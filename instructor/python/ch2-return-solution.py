def total_return(start, end, distribution):
    # TODO: return the total return in percentage units.
    return (end - start + distribution) / start * 100

if __name__ == "__main__":
    print("Total return (%):", total_return(80, 76, 2))
