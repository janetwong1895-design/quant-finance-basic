# Chapter 8 data and execution contract

Original authored synthetic data, 31 October 2026; no market feed or real corporate actions. Dates are ordered hypothetical sessions, including weekends intentionally. Repository MIT licence. Prices GBP/unit, finite positive unadjusted synthetic values with no splits, distributions, default or other corporate actions.

`date`: unique chronological ISO session date. `open`: available at that session open. `close`: available after that session close.

Development Jan2–17,2025. Exposed transfer Feb3–12,2025. Neither establishes market profitability or a secure holdout. All data are inspectable. No tuning, parameter optimisation or selective trial deletion.

Frozen rule: trailing3-close mean including t. Strict close[t]>mean chooses target1;else0. After-close signal t executes open[t+1], earns open[t+1]→open[t+2]. Warmup first3closes; no partial final interval. `backtest(data,{costBps=10,initial=1000,window=3})` validates unique ordered dates, positive prices, window3 only and cost0–100bps. Returns rows and final wealth/benchmark, decimal total returns, final-exit costs, initial/cost/window metadata. Exported DEVELOPMENT_DATA=DATA; EVALUATION_DATA=TRANSFER_DATA; EVALUATION_ID='qf-synthetic-feb2025-v1' is only an exposed teaching label. Chapter9 uses its own disclosed evaluation case.

Rows: signalDate,entryDate,exitDate,close,average,position,previousPosition,turnover=abs(position−previous),grossReturn=nextopen/entryopen−1,costRate=(costBps/10000)*turnover,startWealth,endWealth,benchmarkStart,benchmarkEnd. Returns are decimal, wealth GBP. Initial previous weight0. Wealth multiplies fee factor first, then1+position*grossReturn. Final liquidate last position with fee factor1−c*lastWeight. Thus ledger last row is before final liquidation. Benchmark same initial1000,firsteligibleopen to samefinalopen,entry and finalexit fees at same c; no intermediate trades. Eligible development opens Jan5→Jan17; transfer Feb6→Feb12. Zero cash return,no leverage,shorts,interest,dividends,tax,default or additional spread/impact/slippage. Fixed0/1weights mean no intermediate-weight drift.

Every cost sensitivity retained. Future-price perturbations must not alter earlier positions. Higher fees cannot improve final wealth with unchanged path. These tests detect specific errors, not every possible implementation defect.
