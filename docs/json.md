# JSON

Convert Python data to and from JSON text with the built-in `json` module.

## Python to JSON string

`json.dumps()` ("dump string") turns dicts, lists, strings, numbers, booleans, and `None` into JSON text.

```python
import json

user = {'name': 'Ana', 'age': 30, 'tags': ['a', 'b'], 'active': True, 'manager': None}

text = json.dumps(user)
print(text)  # {"name": "Ana", "age": 30, "tags": ["a", "b"], "active": true, "manager": null}

print(json.dumps(user, indent=2, sort_keys=True))
```

## JSON string to Python

`json.loads()` ("load string") parses JSON text back into Python objects.

```python
data = json.loads('{"name": "Ana", "scores": [90, 85], "active": false}')
print(data['name'])  # Ana
print(data['scores'][0])  # 90
print(data['active'])  # False
```

## Reading and writing files

`json.dump()` and `json.load()` (no `s`) work with open files.

```python
with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(user, file, indent=2)

with open('user.json', encoding='utf-8') as file:
    loaded = json.load(file)

print(loaded == user)  # True
```

## Type mapping

| Python | JSON |
| --- | --- |
| `dict` | object |
| `list`, `tuple` | array |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

## Invalid JSON

Parsing bad input raises `json.JSONDecodeError` (a subclass of `ValueError`).

```python
try:
    json.loads("{'single': 'quotes'}")
except json.JSONDecodeError as error:
    print('Invalid JSON:', error.msg)  # Invalid JSON: Expecting property name enclosed in double quotes
```

## Non-serializable values

Types such as `datetime`, `set`, or custom objects are rejected. Pass `default=` to convert them.

```python
from datetime import date

try:
    json.dumps({'when': date(2026, 1, 15)})
except TypeError as error:
    print(error)  # Object of type date is not JSON serializable

print(json.dumps({'when': date(2026, 1, 15)}, default=str))  # {"when": "2026-01-15"}
```

!!! warning "Gotcha: JSON keys are always strings"
    `json.dumps({1: 'a'})` produces `{"1": "a"}`, so the integer key comes back as the string `"1"`. Tuples come back as lists.

!!! tip "Pretty-print any JSON"
    From the terminal: `python -m json.tool file.json`.
