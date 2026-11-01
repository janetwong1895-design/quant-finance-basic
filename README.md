# Quantitative Finance Foundations

A beginner course with ten self-paced chapters, an estimated30-hour core and English / Taiwan Traditional Chinese editions.

## Choose your edition

| Entry | English | 繁體中文（臺灣） |
| --- | --- | --- |
| Course introduction and interactive preview | [Landing page](dist/learn/index.html) | [課程介紹頁](dist/zh-tw/learn/index.html) |
| Ten-chapter course map | [Course map](dist/course/index.html) | [完整課程地圖](dist/zh-tw/course/index.html) |
| Python setup and full text route | [Python guide](dist/python/guide.html) | [Python 指南](dist/zh-tw/python/guide.html) |
| Concept graphics | [Visual guides](dist/visuals/index.html) | [概念圖解](dist/zh-tw/visuals/index.html) |

- Taiwan edition: hypothetical monetary examples are denominated in New Taiwan dollars (TWD / NT$), with zh-TW number formatting (1,234.56). This is a teaching-context adaptation, not an FX conversion; underlying numerical relationships remain consistent.

Hosted entry points: [English introduction](https://quant-finance-foundations-chapter-one.dreamy-shore-0573.chatgpt.site/learn/) and [繁體中文介紹頁](https://quant-finance-foundations-chapter-one.dreamy-shore-0573.chatgpt.site/zh-tw/learn/). The existing site's private audience is preserved; these pages do not add public enrolment, lead collection or payment.


| Chapter | Content | Status |
| --- | --- | --- |
| [1 · Start with a good question](dist/index.html) | Markets, instruments, benchmarks, an allocation lab and a research card | Self-paced learning |
| [2 · Make the numbers comparable](dist/chapter-02/index.html) | Total returns, compounding/CAGR, present value, bond cash flows and purchasing power | Self-paced learning |
| [3 · Trust the table](dist/chapter-03/index.html) | CSV inspection, dates, duplicates, missing prices, split adjustments and a cleaning audit | Self-paced learning |
| [4 · Describe the evidence](dist/chapter-04/index.html) | Probability, mean/median, sample spread, quantiles, correlation and resampling | Self-paced learning |
| [5 · Risk and performance](dist/chapter-05/index.html) | Volatility, drawdown and a defined Sharpe ratio | Self-paced learning |
| [6 · Portfolio diversification](dist/chapter-06/index.html) | Weights, concentration, rebalancing, correlation and beta | Self-paced learning |
| [7 · Simulation and payoffs](dist/chapter-07/index.html) | Seeded scenarios, forwards and calls after premium | Self-paced learning |
| [8 · A transparent backtest](dist/chapter-08/index.html) | Signal timing, execution, costs and matching benchmark | Self-paced learning |
| [9 · Research reliability](dist/chapter-09/index.html) | Bias audit, complete trial logs and a frozen plan | Self-paced learning |
| [10 · Capstone and communication](dist/chapter-10/index.html) | Reproduce evidence, draft and revise a research memo | Self-paced learning |

Start with the [complete course map](dist/course/index.html). All ten chapters provide formative self-learning: completion does not certify research quality or award a credential.

Each chapter has worked examples, guided practice, independent self-checks, targeted feedback, revisions, local progress and a text/paper alternative. Suggested chapter time is three hours, including activities and assessment. Learner timings and educational effectiveness have not yet been validated.

## Run locally

Use Python 3 to serve the static learner site:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Open the [English introduction](http://127.0.0.1:8765/learn/), [繁體中文介紹頁](http://127.0.0.1:8765/zh-tw/learn/), [Chapter 1](http://127.0.0.1:8765/), [Chapter 2](http://127.0.0.1:8765/chapter-02/), [Chapter 3](http://127.0.0.1:8765/chapter-03/) or the [ten-chapter course map](http://127.0.0.1:8765/course/). JavaScript modules require HTTP(S); double-clicking `index.html` is not a supported way to launch the interactive route. Learners visiting a hosted copy need no installation.

The core chapters have no runtime npm dependencies, external fonts, remote calculation APIs or required market-data accounts. The optional Python workspace downloads pinned Pyodide from jsDelivr on first execution; the downloadable scripts run locally without third-party Python packages. Text/paper alternatives are available at `dist/chapter-guide.html` and each later chapter’s `guide.html`.

## Verify and regenerate

Developer checks require Node.js 24 or later. No `npm install` is needed.

```sh
npm run build:all
npm test
npm run test:python
```

The tests cover the implemented chapters, including financial arithmetic, input validation, critical assessment criteria, saved-state recovery and completion invalidation. The Chapter 2–10 text routes are generated from the same lesson and assessment definitions as their interactive routes.

## Optional Python consolidation

Open [Python practice](dist/python/index.html) from the chapter links. Chapter-linked activities offer prediction, a real Python editor, changed-input checks, hints, references and self-reviewed reflection. A [complete text/setup guide](dist/python/guide.html) and [downloadable learner pack](dist/python/learner-pack.zip) support local Python. See [the design and future chapter mapping](docs/python-practice.md).

Allow an additional 40 minutes for Chapter 1, 65 minutes for Chapter 2 and 10–15 minutes for first setup, beyond the proposed 30-hour core. These estimates are unvalidated. Python progress is separate from core completion. Chapters 3–4 add an estimated 50 and 45 minutes of data and statistics scripts; Chapters 5–10 add risk, portfolios, simulation, backtesting, reliability and capstone scripts; their additional study time is shown per activity.

## Course materials

- [Full 30-hour course proposal](course-proposal.md)
- [Course brief and assumptions](course-brief.md)
- [Production record](production-record.md)
- [Chapter 1 design notes](docs/chapter-01.md)
- [Chapter 2 design notes](docs/chapter-02.md)
- [Chapter 3 design notes](docs/chapter-03.md)
- [Chapter 4 design notes](docs/chapter-04.md)
- [Remaining chapter design notes](docs/)
- [Full prototype manifest and outcome map](docs/prototype-manifest.md)
- [Instructor materials and answer guidance](instructor/)
- [Independent reviews and verification records](review/)

Only `dist/` should be served to learners. Instructor and review materials are separate documentation; this public repository makes them available to anyone reading the source. Client-side correctness data are also visible by design. These are formative learning activities, not secure examinations or accredited credentials.

## Data, privacy and limitations

All core examples use original hypothetical data with stated assumptions. No live execution, broker keys or learner uploads are required. Returns and positive model outcomes do not establish investment suitability or future performance.

Answers and progress stay in the learner's browser using separate chapter storage keys. Reset removes the selected chapter's saved work; exports are local records, with no import or account synchronisation. The lesson app has no analytics, although a hosting provider may keep access logs.

The package has undergone automated checks, browser walkthroughs and independent agent reviews. Real-learner pilots, full screen-reader verification, validated completion timings and commercial-release checks remain outstanding. Review records describe the precise scope and remaining limits. Agent review does not establish accessibility conformance or learning effectiveness.

The original hosting configuration, deployment archives and machine-specific authentication settings are intentionally absent. To host this repository, serve `dist/` from any static web server and configure the destination separately. Source review hashes refer to the inspected development snapshots; machine-local documentation paths have been normalised for this repository.

## Validation evidence

The automated suite covers financial calculations, state and feedback mechanics, graphics, locale contracts and both downloadable Python packs. Current counts and scoped checks are recorded with each release. Independent review and observed browser workflows are recorded in [the release evidence](review/chapters-05-10/verification.md). Human learner timing, full assistive-technology compatibility and educational effectiveness remain unvalidated.

## License

The repository's existing [MIT license](LICENSE) is retained. External reference sites and readings keep their own rights and terms; links do not grant redistribution rights to their materials.
