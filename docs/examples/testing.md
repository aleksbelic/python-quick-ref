# Testing

Test the [examples](fibonacci.md) with [pytest](https://pytest.org): save each block below as `test_example.py` and run it from the project root:

```bash
python -m pip install pytest
pytest
```

pytest finds files named `test_*.py` and runs every function named `test_*`. A test passes when it finishes without an exception; a failing `assert` shows both sides of the comparison.

## Fibonacci tests

Parametrized cases for known values, plus invalid inputs that must raise `ValueError`.

```python
import pytest


def nth_fib(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (7, 8),
    ],
)
def test_nth_fib(n, expected):
    assert nth_fib(n) == expected


@pytest.mark.parametrize("invalid_input", [3.14, "100", 0, -1])
def test_nth_fib_rejects_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        nth_fib(invalid_input)
```

## Palindrome tests

Palindromes (including mixed case, punctuation, and empty string), non-palindromes, and a case proving non-alphanumeric characters are ignored.

```python
import pytest


def is_palindrome(word: str) -> bool:
    cleaned = "".join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]


@pytest.mark.parametrize(
    "word",
    [
        "racecar",
        "RaceCar",
        "A man, a plan, a canal: Panama!",
        "12321",
        "",
        "Ana voli Milovana",
    ],
)
def test_palindromes(word):
    assert is_palindrome(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "python",
        "racecars",
        "12345",
        "hello world",
    ],
)
def test_non_palindromes(word):
    assert is_palindrome(word) is False


def test_non_alphanumeric_characters_are_ignored():
    assert is_palindrome("!@#r a c e c a r#$%") is True
```

## Prime number tests

Known primes, known non-primes (including `1`, `0`, and negatives), and invalid inputs.

```python
import pytest


def is_prime_number(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    if num <= 1:
        return False

    # if a divisor exists, one of them must be <= sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


@pytest.mark.parametrize("num", [2, 3, 17, 29])
def test_primes(num):
    assert is_prime_number(num) is True


@pytest.mark.parametrize("num", [1, 0, -5, 16, 25])
def test_non_primes(num):
    assert is_prime_number(num) is False


@pytest.mark.parametrize("invalid_input", [3.14, "100"])
def test_is_prime_number_rejects_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        is_prime_number(invalid_input)
```

## Word counter tests

Plain assertions on the returned `Counter`.

```python
import re
from collections import Counter


def count_words(text: str) -> Counter[str]:
    words = re.findall(r"[a-z0-9']+", text.lower())
    return Counter(words)


def test_counts_words_ignoring_case_and_punctuation():
    counts = count_words("The cat and the hat. THE END!")
    assert counts["the"] == 3
    assert counts["cat"] == 1


def test_most_common_returns_top_words():
    counts = count_words("a b b c c c")
    assert counts.most_common(2) == [("c", 3), ("b", 2)]


def test_empty_text_has_no_words():
    assert count_words("") == {}
```

## CSV summary tests

`io.StringIO` stands in for a file, and `pytest.approx` compares floats safely.

```python
import csv
from io import StringIO
from statistics import mean
from typing import TextIO

import pytest


def summarize_ages(file: TextIO) -> dict[str, float]:
    ages = [int(row["age"]) for row in csv.DictReader(file)]
    if not ages:
        raise ValueError("No rows to summarize")

    return {
        "count": len(ages),
        "min": min(ages),
        "max": max(ages),
        "mean": mean(ages),
    }


CSV_TEXT = """name,email,age
Anna,anna@example.com,30
Ben,ben@example.com,22
Cleo,cleo@example.com,28
"""


def test_summarize_ages():
    summary = summarize_ages(StringIO(CSV_TEXT))
    assert summary == {"count": 3, "min": 22, "max": 30, "mean": pytest.approx(26.67, abs=0.01)}


def test_header_only_file_raises():
    with pytest.raises(ValueError):
        summarize_ages(StringIO("name,email,age\n"))
```

## File renamer tests

pytest's built-in `tmp_path` fixture gives every test its own empty temporary folder, so tests never touch real files.

```python
from pathlib import Path


def add_prefix(folder: Path, prefix: str, dry_run: bool = True) -> list[tuple[Path, Path]]:
    renames = [
        (path, path.with_name(prefix + path.name))
        for path in sorted(folder.iterdir())
        if path.is_file() and not path.name.startswith(prefix)
    ]
    if not dry_run:
        for old, new in renames:
            old.rename(new)
    return renames


def make_files(folder, *names):
    for name in names:
        (folder / name).write_text("")


def test_dry_run_changes_nothing(tmp_path):
    make_files(tmp_path, "a.txt", "b.txt")

    renames = add_prefix(tmp_path, "2026_")

    assert [new.name for _, new in renames] == ["2026_a.txt", "2026_b.txt"]
    assert sorted(p.name for p in tmp_path.iterdir()) == ["a.txt", "b.txt"]


def test_real_run_renames_files(tmp_path):
    make_files(tmp_path, "a.txt", "b.txt")

    add_prefix(tmp_path, "2026_", dry_run=False)

    assert sorted(p.name for p in tmp_path.iterdir()) == ["2026_a.txt", "2026_b.txt"]


def test_already_prefixed_files_and_folders_are_skipped(tmp_path):
    make_files(tmp_path, "2026_a.txt", "b.txt")
    (tmp_path / "subfolder").mkdir()

    renames = add_prefix(tmp_path, "2026_")

    assert [old.name for old, _ in renames] == ["b.txt"]
```

!!! tip "parametrize over copy-paste"
    `@pytest.mark.parametrize` runs one test function against many inputs — one place to extend coverage instead of a new function per case. Use `pytest.raises` to assert that invalid input fails loudly.

## Useful pytest options

```bash
pytest -q                 # quiet output
pytest -x                 # stop at the first failure
pytest -k palindrome      # run tests whose name contains "palindrome"
pytest test_module.py::test_name   # one specific test
pytest -vv                # verbose, full diffs
```

## How this site stays honest

Every example on these pages is self-contained — paste a block into a file and run it. Automated snippet checking in CI is planned but not wired up yet; until then, verify by running the code yourself before pushing.
