# CSV Summary

Summarize a numeric column of a [CSV](../csv.md) file: count, minimum, maximum, and mean.

```python
import csv
from statistics import mean
from typing import TextIO


def summarize_ages(file: TextIO) -> dict[str, float]:
    """Return count, min, max and mean of the `age` column of a CSV file."""
    ages = [int(row["age"]) for row in csv.DictReader(file)]
    if not ages:
        raise ValueError("No rows to summarize")

    return {
        "count": len(ages),
        "min": min(ages),
        "max": max(ages),
        "mean": mean(ages),
    }
```

The function takes an open file, so it works with real files *and* in-memory text:

```python
from io import StringIO

csv_text = """name,email,age
Anna,anna@example.com,30
Ben,ben@example.com,22
Cleo,cleo@example.com,28
"""

print(summarize_ages(StringIO(csv_text)))
# {'count': 3, 'min': 22, 'max': 30, 'mean': 26.666666666666668}

with open('./data/user-data-with-header.csv', newline='', encoding='utf-8') as file:
    print(summarize_ages(file)['mean'])  # 26.666666666666668
```

!!! note "Needs the CSV file"
    The `StringIO` part above runs as-is, but the last two lines read `./data/user-data-with-header.csv` (see [CSV](../csv.md)), which isn't in the repo.

!!! tip "Accept a file object, not a path"
    Taking a `TextIO` instead of a filename makes the function trivial to test — pass a `StringIO` — and reusable for data that doesn't live on disk.
