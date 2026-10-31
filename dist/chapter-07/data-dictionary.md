# Chapter 7 data contract

All data are original synthetic teaching examples, authored 31 October 2026. No company prices or market feed; reuse under repository MIT licence.

- terminal: terminal underlying price, GBP per one unit.
- forward: long forward payoff terminal minus strike100; no initial premium, collateral or financing.
- call: max(terminal−100,0), GBP per unit; excludes premium.
- profit: call payoff minus supplied premium6, GBP per unit. Undiscounted convention; excludes financing, tax, fees, dividends and default. This is not an option-price estimate.
- simulation CSV: seed whole1–999999; spread5/10/20 percent;100paths each3periods; r1–r3 in percentage units. Price starts100. Each period independently selects equally probable −spread,0,+spread using explicit unsigned32-bit LCG z=(1664525z+1013904223)mod2^32,u=z/2^32,direction=floor(3u)−1. Draws continue in path/period order. No calendar frequency or annualisation.

The model bounds losses and assumes stationary independent returns. More paths do not validate these assumptions. Seed42 first directions down,down,zero: terminal81 at spread10;64 at spread20. Python reproduces the explicit generator using modulo, not a library default RNG. Browser all-run CSV is unrounded. Paper guide supplies both100-path tables.
