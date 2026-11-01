import math
def net_wealth(opens,positions,cost_bps,initial=1000):
    if len(opens) != len(positions)+1 or not positions or any(w not in (0,1) for w in positions):
        raise ValueError("One0/1weight per open-to-open interval.")
    if not all(math.isfinite(x) and x > 0 for x in opens) or not 0 <= cost_bps <= 100:
        raise ValueError("Positive finite opens,costs0-100bps.")
    c=cost_bps/10000
    wealth,previous=initial,0
    for i,weight in enumerate(positions):
        turnover=None # TODO_TURNOVER
        interval_return=opens[i+1]/opens[i]-1
        wealth=None # TODO_INTERVAL
        previous=weight
    return None # TODO_EXIT
if __name__ == "__main__":
    print(net_wealth([100,100],[1],10))
