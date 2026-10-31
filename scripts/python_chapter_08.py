"""Optional Chapter8 standard-library Python3.8 exercises."""
from textwrap import dedent

def code(s): return dedent(s).strip()+'\n'
def case(label,function,args,expected,hint): return dict(label=label,function=function,args=args,expected=expected,hint=hint)
EXERCISES=[dict(id='ch8-timing',chapter=8,kind='Guided practice',minutes=15,title='Separate signal from execution',concept='Chapter8 · trailing3-close signal',objective='Compute a frozen trailing-close target using only information through t.',prediction='Closes100,101,102 imply which target? If a later close changes,should this target change?',instructions='Complete the strict comparison using only closes[t-2:t+1]. Return1 if the signal close is strictly above the mean,otherwise0. This is a target decided after close t,not an execution at that close. Execution would be next open. Do not use future closes.',syntax='slicing excludes the upper bound; t+1 includes close t. int(True) is1 and int(False) is0. Equality belongs to cash.',hints=['Compare closes[t] with the mean of the selected3 values.','Return int(closes[t] > average).'],reflection='Draw signal close→next open execution→following open mark. Explain why modifying future closes must not alter this target.',starter=code('''
 import math
 def target(closes,t):
     if not isinstance(t,int) or t < 2 or t >= len(closes):
         raise ValueError("Need3known closes ending at t.")
     observed=closes[t-2:t+1]
     if not all(math.isfinite(x) and x > 0 for x in observed):
         raise ValueError("Use finite positive observed prices.")
     average=sum(observed)/3
     return None # TODO_SIGNAL
 if __name__ == "__main__":
     print(target([100,101,102,1],2))
'''),solution=None,replacements={'None # TODO_SIGNAL':'int(closes[t] > average)'},example=code('''
 closes=[100,101,102]
 average=sum(closes)/3
 print("Signal target:",int(closes[-1]>average))
 print("Execute at the next open,not this already-observed close.")
'''),cases=[case('Known closes','target',[[100,101,102,1],2],1,'Use only the3closes ending at t.'),case('Future perturbation','target',[[100,101,102,999],2],1,'Changing a future close must not rewrite the past signal.'),case('Tie means cash','target',[[5,5,5],2],0,'Strictly greater,not greater-or-equal.'),case('Falling path','target',[[10,9,8],2],0,'The close is below its trailing mean.')]),
 dict(id='ch8-costs',chapter=8,kind='Transfer challenge',minutes=15,title='Account for the final exit',concept='Chapter8 · turnover fee before return',objective='Reproduce fixed positions net of every fee including liquidation.',prediction='Flat opens,initial1000,target1,cost10bps:predict final wealth after entry and final exit.',instructions='positions[i] is a supplied0/1target held from opens[i] to opens[i+1]. The signal timing that created positions must be audited separately. Complete turnover,fee-before-return growth,and final-exit fee. Costs are bps per traded notional,cash return0%,no leverage/shorting,taxes or additional slippage. Keep the supplied positions fixed;this is not a search for profitable rules.',syntax='abs computes absolute turnover. bps/10000 converts to decimal. A loop enumerates each holding interval. The last target is sold at the final eligible open.',hints=['Turnover=abs(weight-previous).','wealth*(1-c*turnover)*(1+weight*return);after the loop multiply by1-c*previous.'],reflection='Show a one-interval hand-check,explain the final exit and why higher fees cannot improve this fixed path.',starter=code('''
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
'''),solution=None,replacements={'None # TODO_TURNOVER':'abs(weight-previous)','None # TODO_INTERVAL':'wealth*(1-c*turnover)*(1+weight*interval_return)','None # TODO_EXIT':'wealth*(1-c*previous)'},example=code('''
 wealth=1000*(1-.001)*(1+.10)
 print("After entry and interval:",wealth)
 wealth*=1-.001
 print("After final exit:",wealth) #1097.8011
'''),cases=[case('Flat but costs lose','net_wealth',[[100,100],[1],10],998.001,'Entry and final exit both cost.')])]
# Explicit numeric fixtures from independent hand calculations.
EXERCISES[1]['cases']=[case('Flat but costs lose','net_wealth',[[100,100],[1],10],998.001,'Entry and final exit both cost.'),case('Growth then liquidation','net_wealth',[[100,110],[1],10],1097.8011,'Apply fee before growth and liquidate at the end.'),case('Cash then entry','net_wealth',[[100,120,132],[0,1],20],1095.6044,'First interval is cash;second earns10%,with entry/exit20bps=.002.'),case('Exit before next interval','net_wealth',[[100,110,80],[1,0],10],1097.8011,'Cash avoids the second price move but exit costs remain.')]
