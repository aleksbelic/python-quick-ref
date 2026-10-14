# Regular Expressions

Match and transform text patterns with the `re` module. Write patterns as raw strings (`r'...'`) so backslashes reach `re` unchanged.

## search()

Returns a `Match` object for the first match anywhere in the string, or `None`.

```python
import re

matches = re.search(r'^The.*Spain$', 'The rain in Spain')
print(matches)
# <re.Match object; span=(0, 17), match='The rain in Spain'>

if matches is not None:
    print(matches[0])  # The rain in Spain
```

## match() vs search() vs fullmatch()

`match()` only matches at the start of the string, `search()` anywhere, `fullmatch()` requires the entire string to match.

```python
print(bool(re.match(r'rain', 'The rain')))  # False, "The rain" doesn't start with rain
print(bool(re.search(r'rain', 'The rain')))  # True
print(bool(re.fullmatch(r'\d+', '12345')))  # True
print(bool(re.fullmatch(r'\d+', '123a')))  # False
```

## findall()

Returns a list of every non-overlapping match.

```python
print(re.findall(r'\d+', 'a1 b22 c333'))  # ['1', '22', '333']
print(re.findall(r'[A-Z]\w+', 'Ana met Ben in Paris'))  # ['Ana', 'Ben', 'Paris']
```

## sub()

Replaces matches with a string. `\s` matches any whitespace.

```python
text = 'The rain in Spain'

print(re.sub('Spain', 'Italy', text))  # The rain in Italy
print(re.sub(r'\s', '-', text))  # The-rain-in-Spain
```

## Groups

Parentheses capture parts of a match. Named groups `(?P<name>...)` make the result self-documenting.

```python
m = re.search(r'(\d{4})-(\d{2})-(\d{2})', 'Released on 2026-01-15.')
print(m.groups())  # ('2026', '01', '15')

m = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})', 'Released on 2026-01-15.')
print(m['year'], m['month'])  # 2026 01
```

## Flags and compile()

Pass `re.IGNORECASE` (or `re.I`) to ignore case. `re.compile()` pre-builds a pattern you reuse.

```python
print(re.findall(r'spain', 'Spain, SPAIN, spain', flags=re.IGNORECASE))
# ['Spain', 'SPAIN', 'spain']

email = re.compile(r'[\w.]+@[\w.]+\.\w+')
print(bool(email.fullmatch('ana@example.com')))  # True
```

## Common pattern pieces

| Pattern | Matches |
| --- | --- |
| `.` | any character except newline |
| `\d` `\w` `\s` | digit, word character, whitespace |
| `\D` `\W` `\S` | the opposites |
| `*` `+` `?` | 0 or more, 1 or more, 0 or 1 |
| `{3}` `{2,4}` | exactly 3, between 2 and 4 |
| `^` `$` | start, end of string |
| `[abc]` `[^abc]` | one of a, b, c / anything but |
| `a|b` | a or b |
| `(...)` | capture group |

!!! tip "Guard the Match"
    `re.search()` returns `None` when nothing matches. Always check for `None` before indexing the result.

!!! tip "Don't parse everything with regex"
    Regexes are great for quick text extraction, but use proper parsers for HTML, JSON, or CSV.
