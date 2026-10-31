def terminal_price(seed,spread):
    if not isinstance(seed,int) or not 1 <= seed <= 999999 or spread not in (5,10,20):
        raise ValueError("Use the declared seed and spread bounds.")
    z,price=seed,100.0
    for _ in range(3):
        z=(1664525*z+1013904223) % 2**32
        direction=int((z/2**32)*3)-1
        price = None # TODO_GROW
    return price
if __name__ == "__main__":
    print(terminal_price(42,10))
