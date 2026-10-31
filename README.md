# Quantitative Finance Foundations

A proposed 30-hour beginner course, with the first two chapters implemented as self-paced, browser-based learning experiences.

| Chapter | Content | Status |
| --- | --- | --- |
| [1 · Start with a good question](dist/index.html) | Markets, instruments, benchmarks, an allocation lab and a research card | Interactive prototype |
| [2 · Make the numbers comparable](dist/chapter-02/index.html) | Total returns, compounding/CAGR, present value, bond cash flows and purchasing power | Interactive prototype |
| 3–10 | Data, statistics, risk, portfolios, simulation, backtesting, research reliability and capstone | Course proposal |

Each implemented chapter has worked examples, guided practice, independent self-checks, targeted feedback, revisions, local progress and a text/paper alternative. Suggested chapter time is three hours, including activities and assessment. Learner timings and educational effectiveness have not yet been validated.

## Run locally

Use Python 3 to serve the static learner site:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Open [Chapter 1](http://127.0.0.1:8765/) or [Chapter 2](http://127.0.0.1:8765/chapter-02/). JavaScript modules require HTTP(S); double-clicking `index.html` is not a supported way to launch the interactive route. Learners visiting a hosted copy need no installation.

The core chapters have no runtime npm dependencies, external fonts, remote calculation APIs or required market-data accounts. The optional Python workspace downloads pinned Pyodide from jsDelivr on first execution; the downloadable scripts run locally without third-party Python packages. Text/paper alternatives are available at `dist/chapter-guide.html` and `dist/chapter-02/guide.html`.

## Verify and regenerate

Developer checks require Node.js 24 or later. No `npm install` is needed.

```sh
npm test
npm run build:guide
npm run build:python
npm run test:python
```

The tests cover both chapters, including financial arithmetic, input validation, critical assessment criteria, saved-state recovery and completion invalidation. The Chapter 2 text route is generated from the same lesson and assessment definitions as the interactive route.

## Optional Python consolidation

Open [Python practice](dist/python/index.html) from the chapter links. Eight activities offer prediction, a real Python editor, changed-input checks, hints, references and self-reviewed reflection. A [complete text/setup guide](dist/python/guide.html) and [downloadable learner pack](dist/python/learner-pack.zip) support local Python. See [the design and future chapter mapping](docs/python-practice.md).

Allow an additional 40 minutes for Chapter 1, 65 minutes for Chapter 2 and 10–15 minutes for first setup, beyond the proposed 30-hour core. These estimates are unvalidated. Python progress is separate from core completion. Chapters 3–10 remain proposed.

## Course materials

- [Full 30-hour course proposal](course-proposal.md)
- [Course brief and assumptions](course-brief.md)
- [Production record](production-record.md)
- [Chapter 1 design notes](docs/chapter-01.md)
- [Chapter 2 design notes](docs/chapter-02.md)
- [Instructor materials and answer guidance](instructor/)
- [Independent reviews and verification records](review/)

Only `dist/` should be served to learners. Instructor and review materials are separate documentation; this public repository makes them available to anyone reading the source. Client-side correctness data are also visible by design. These are formative learning activities, not secure examinations or accredited credentials.

## Data, privacy and limitations

All core examples use original hypothetical data with stated assumptions. No live execution, broker keys or learner uploads are required. Returns and positive model outcomes do not establish investment suitability or future performance.

Answers and progress stay in the learner's browser using separate chapter storage keys. Reset removes the selected chapter's saved work; exports are local records, with no import or account synchronisation. The lesson app has no analytics, although a hosting provider may keep access logs.

The package has undergone automated checks, browser walkthroughs and independent agent reviews. Real-learner pilots, full screen-reader verification, validated completion timings and commercial-release checks remain outstanding. Review records describe the precise scope and remaining limits. Agent review does not establish accessibility conformance or learning effectiveness.

The original prototype's hosting configuration, deployment archives and machine-specific authentication settings are intentionally absent. To host this repository, serve `dist/` from any static web server and configure the destination separately. Source review hashes refer to the inspected development snapshots; machine-local documentation paths have been normalised for this repository.

## License

The repository's existing [MIT license](LICENSE) is retained. External reference sites and readings keep their own rights and terms; links do not grant redistribution rights to their materials.
