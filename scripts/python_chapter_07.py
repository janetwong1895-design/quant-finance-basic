"""Optional Chapter7 standard-library Python practice, Python3.8+."""
from textwrap import dedent

def code(s): return dedent(s).strip()+'\n'
def case(label,function,args,expected,hint): return dict(label=label,function=function,args=args,expected=expected,hint=hint)
EXERCISES=[dict(id='ch7-payoffs',chapter=7,kind='Guided practice',minutes=15,title='Keep premium out of payoff',concept='Chapter7 · terminal payoff versus undiscounted profit',objective='Calculate long-forward payoff, call payoff and call profit per unit.',prediction='K=100,premium6,terminal104: predict forward payoff,call payoff and call profit.',instructions='Complete the three values. Prices,premium and output are pounds per unit. No financing,discounting,fees,taxes,early exercise or default. Premium is supplied,not priced. A long forward has no initial premium in this example.',syntax='max(a,0) floors a negative payoff at zero. Dictionary keys label different quantities. Subtract premium once for profit.',hints=['Forward payoff is terminal-strike,without a zero floor.','Call payoff is max(terminal-strike,0);profit subtracts premium from that payoff.'],reflection='Explain why a call can be in the money yet make a loss,and why negative long-forward payoffs are possible.',starter=code('''
 import math
 def derivative_report(terminal,strike,premium):
     if not all(math.isfinite(x) and x >= 0 for x in [terminal,strike,premium]):
         raise ValueError("Use nonnegative finite amounts.")
     payoff = None # TODO_CALL
     return {"forward":None, # TODO_FORWARD
             "call":payoff,"profit":None} # TODO_PROFIT
 if __name__ == "__main__":
     print(derivative_report(104,100,6))
'''),solution=None,replacements={'None # TODO_CALL':'max(terminal-strike,0)','None, # TODO_FORWARD':'terminal-strike,','None} # TODO_PROFIT':'payoff-premium}'},example=code('''
 terminal,strike,premium=104,100,6
 payoff=max(terminal-strike,0)
 print("Forward payoff:",terminal-strike)
 print("Call payoff:",payoff)
 print("Undiscounted call profit:",payoff-premium)
'''),cases=[case('Above strike but loss','derivative_report',[104,100,6],{'forward':4,'call':4,'profit':-2},'Premium belongs in profit,not payoff.'),case('Below strike','derivative_report',[70,80,5],{'forward':-10,'call':0,'profit':-5},'The forward obligation can lose;call payoff is floored.'),case('Break-even','derivative_report',[85,80,5],{'forward':5,'call':5,'profit':0},'Call break-even is strike plus premium,without financing.')]),
 dict(id='ch7-path',chapter=7,kind='Transfer challenge',minutes=15,title='Reproduce a conditional price path',concept='Chapter7 · compounding and fixed-generator simulation',objective='Compound supplied discrete returns;repeat a declared seeded generator.',prediction='For100 and [+10,0,-10]%,predict terminal price. Does a wider spread raise every terminal outcome?',instructions='Complete the multiplication. The supplied fixed LCG produces the same up/zero/down indices as the browser;do not use random.Random and expect identical paths. The function returns one terminal price from three draws. Seed1–999999,spread5/10/20. Three independent,equally likely bounded returns are a teaching assumption,not a market forecast.',syntax='Python integers do not overflow;use modulo2**32 explicitly. z//(2**32//3) is not exactly the specified mapping;use int((z/2**32)*3)-1. Multiplication updates the current wealth.',hints=['The period return is direction*spread in percentage units.','Multiply price by1+direction*spread/100 each period.'],reflection='Explain seed reproducibility,compound growth,and two model risks that more paths cannot fix.',starter=code('''
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
'''),solution=None,replacements={'None # TODO_GROW':'price*(1+direction*spread/100)'},example=code('''
 price=100
 for return_pct in [10,0,-10]:
     price *= 1+return_pct/100
 print("Conditional terminal price:",price) #99
 print("This invented path is not a forecast.")
'''),cases=[case('Browser seed42','terminal_price',[42,10],81,'The first directions are down,down,zero.'),case('Spread-only sensitivity','terminal_price',[42,20],64,'Keep draws fixed;compound two-20% returns.'),case('Different seed','terminal_price',[1,5],95,'Seed1 draws down,zero,zero.')])]
