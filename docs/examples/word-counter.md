# Word Counter

Count how often each word appears in a text. Combines [regular expressions](../regexp.md), [Counter](../collections.md#counter), and string methods.

```python
import re
from collections import Counter


def count_words(text: str) -> Counter[str]:
    """Count how often each word appears, ignoring case and punctuation."""
    words = re.findall(r"[a-z0-9']+", text.lower())
    return Counter(words)
```

```python
text = "The cat and the hat. The END!"
counts = count_words(text)

print(counts['the'])          # 3
print(counts.most_common(2))  # [('the', 3), ('cat', 1)]
```

To count the words of a file, read it first with [`Path.read_text()`](../files.md#pathlib):

<!-- no-run -->
```python
from pathlib import Path

print(count_words(Path('book.txt').read_text(encoding='utf-8')).most_common(10))
```

!!! tip "Why `re.findall` instead of `split()`"
    `text.split()` would keep punctuation glued to words (`"hat."` and `"hat"` would count separately). A regex that picks out only word characters avoids that.
