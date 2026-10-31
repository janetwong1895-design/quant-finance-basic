# Chapter 6: original hypothetical data dictionary

- `month`: unique chronological month label, January–June2025. Invented examples, not historical market data.
- `a_return_pct`: A monthly simple total return in percentage units; 5 means5%, not.05. Distributions are included.
- `b_return_pct`: B monthly simple total return on the same dates and basis; B is the second asset.
- `market_return_pct`: same-date illustrative benchmark monthly simple total return in percentage units.

All observations are finite, no months are missing, and no external flows, fees, taxes or transaction costs are included. Initial wealth 100 is a hypothetical currency-unit value, not a price. No market-data licence or API key is needed: original teaching data are released with this repository. Keep dates aligned; do not sort each return series independently.

`comparison-examples.csv` holds the same two deterministic prepared runs as the text guide. Interactive JSON exports retain run inputs, predictions and timestamps. Interactive CSV exports contain every retained run: `run`, `input`, `month` (zero means initial), `value1`, `value2`, `detail`. Here input is target/initial A percentage, value1 is constant-mix wealth, value2 is buy-and-hold wealth, detail is ending buy-and-hold A fraction. No costs are included.

A changed input generates another retained deterministic run; there is no random generator or seed. Compare matched dates only. Export is a record, not an import or synchronisation mechanism.
