import math

def sensitivity_report(rows):
    if len(rows) < 2 or len({r[0] for r in rows}) != len(rows):
        raise ValueError("Use two or more unique same-date rows.")
    portfolio, market = [r[1] for r in rows], [r[2] for r in rows]
    if not all(math.isfinite(x) for x in portfolio + market):
        raise ValueError("Use finite same-frequency returns.")
    mp, mm = sum(portfolio)/len(rows), sum(market)/len(rows)
    pp = 0 if all(x == portfolio[0] for x in portfolio) else sum((x-mp)**2 for x in portfolio)
    bb = 0 if all(x == market[0] for x in market) else sum((x-mm)**2 for x in market)
    if bb == 0:
        return {"beta_defined":0,"beta":0,"correlation_defined":0,"correlation":0}
    cross = sum((p-mp)*(m-mm) for p,m in zip(portfolio,market))
    beta = cross / bb
    if pp == 0:
        return {"beta_defined":1,"beta":beta,"correlation_defined":0,"correlation":0}
    correlation = cross / math.sqrt(pp*bb)
    return {"beta_defined":1,"beta":beta,"correlation_defined":1,"correlation":correlation}

if __name__ == "__main__":
    print(sensitivity_report([["Jan",-2,-1],["Feb",0,0],["Mar",2,1]]))
