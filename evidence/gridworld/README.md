# GridWorld finite-domain evidence

This directory contains a **byte-preserved copy of the archived GridWorld enumeration data** and its 12-cell reaggregation.

| File | Contents |
| --- | --- |
| [`identifiability_enumeration.csv`](identifiability_enumeration.csv) | **16,368** aggregation rows, 24 state comparisons per row |
| [`table2_reaggregated.csv`](table2_reaggregated.csv) | Unresolved comparison counts for 3 hypothesis pairs × 4 observation contracts |

**Research-record SHA-256 of the original enumeration CSV:**

`d7346f6a307e4b711738ac45cc81df517490005edae39595a50d3e4e84eb3f48`

The CSV uses CRLF line endings. The repository preserves those original bytes using a [Git attributes rule](../../.gitattributes).

## Verification

~~~bash
python tools/verify_gridworld_enumeration.py
python -m unittest discover -s tests -p test_gridworld_evidence.py -v
~~~

Run the commands from the repository root with Python 3.11+. The [verifier](../../tools/verify_gridworld_enumeration.py) checks the CSV hash, schema, internal consistency, finite experiment design, and all 12 comparison counts. GitHub Actions repeats these checks automatically.

**Scientific limitation:** This verifies a saved data artifact; it does **not** regenerate simulator trajectories. Canonical simulator source is not included here. See [reproducibility](../../docs/REPRODUCIBILITY.md).
