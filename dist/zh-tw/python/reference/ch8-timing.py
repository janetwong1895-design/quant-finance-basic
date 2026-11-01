import math
def target(closes,t):
    if not isinstance(t,int) or t < 2 or t >= len(closes):
        raise ValueError("Need3known closes ending at t.")
    observed=closes[t-2:t+1]
    if not all(math.isfinite(x) and x > 0 for x in observed):
        raise ValueError("Use finite positive observed prices.")
    average=sum(observed)/3
    return int(closes[t] > average)
if __name__ == "__main__":
    print(target([100,101,102,1],2))
