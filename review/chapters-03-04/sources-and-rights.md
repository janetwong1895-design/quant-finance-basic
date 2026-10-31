# Sources and data rights

Checked 31 October 2026. Original course explanations, hypothetical data tables and teaching scripts are authored for this repository. No market-price dataset or third-party course assessment was copied. Core examples are deterministic; declared pseudorandom seeds apply only to resampling demonstrations, not to data provenance. External readings are optional and retain their own terms.

- Python official CSV documentation: https://docs.python.org/3/library/csv.html — reader/DictReader and explicit dialect/string conversion behaviour.
- Python official date documentation: https://docs.python.org/3/library/datetime.html — date parsing and ISO representation.
- Investor.gov stock split glossary: https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-split — share-count/price adjustment concept.
- Nasdaq provider documentation: https://data.nasdaq.com/databases/SEP/documentation — an example of provider-specific adjustment documentation; not a licence or universal definition. No provider data redistributed.
- NIST measures of scale: https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm — sample variance n−1, standard-deviation units and outlier sensitivity.
- Python official statistics documentation: https://docs.python.org/3/library/statistics.html — descriptive statistics and explicitly different quantile conventions. Course scripts retain Python 3.8+ compatibility; newer convenience APIs are not assumed available.
- NIST Dataplot bootstrap manual: https://www.itl.nist.gov/div898/software/dataplot/refman1/ch2/bootstra.pdf — with-replacement samples of equal size and reproducible seeds. The small course demonstration does not establish a validated future-risk interval.

References inform concepts and implementation; they do not validate this course’s learning effectiveness or investment performance. Current runtime remains pinned to Pyodide 314.0.7; no new CDN package is added. Upstream runtime licensing remains separate from the course repository licence.
