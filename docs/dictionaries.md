# Dictionaries

Changeable key/value collections using `{}`. Keys must be unique and hashable, similar to JSON objects. Dicts keep insertion order.

## Creating and accessing

Look up values by key; `len()` counts entries.

```python
d1 = {
    'name': 'Hans',
    'age': '32',
    'city': 'Berlin'
}

print(d1)  # {'name': 'Hans', 'age': '32', 'city': 'Berlin'}
print(d1['name'])  # Hans
print(len(d1))  # 3

d2 = dict(name='Hans', age='32')  # alternative constructor
print(d2)  # {'name': 'Hans', 'age': '32'}
```

## Safe lookups with get()

`d['missing']` raises `KeyError`. `get()` returns `None` (or a default you choose).

```python
print(d1.get('city'))  # Berlin
print(d1.get('country'))  # None
print(d1.get('country', 'unknown'))  # unknown
print('city' in d1)  # True, membership checks keys
```

## Adding, changing and removing

```python
d1['country'] = 'Germany'  # add
d1['age'] = '33'  # change
print(d1)  # {'name': 'Hans', 'age': '33', 'city': 'Berlin', 'country': 'Germany'}

removed = d1.pop('country')  # remove and return
print(removed)  # Germany

del d1['age']  # remove
print(d1)  # {'name': 'Hans', 'city': 'Berlin'}
```

## Merging

`update()` merges in place; `|` (3.9+) creates a new dict. The right-hand side wins on duplicate keys.

```python
defaults = {'theme': 'light', 'lang': 'en'}
user = {'theme': 'dark'}

print(defaults | user)  # {'theme': 'dark', 'lang': 'en'}

defaults.update(user)
print(defaults)  # {'theme': 'dark', 'lang': 'en'}
```

## Looping through keys

Iterating the dict directly yields keys; `.keys()` is equivalent.

```python
d1 = {'name': 'Hans', 'age': '32', 'city': 'Berlin'}

for key in d1:
    print(key)
# name
# age
# city
```

## Looping through values

Use `.values()` to get just the values.

```python
for value in d1.values():
    print(value)
# Hans
# 32
# Berlin
```

## Looping through items

`.items()` yields `(key, value)` tuples, unpackable into two variables.

```python
for key, val in d1.items():
    print(key, val)
# name Hans
# age 32
# city Berlin
```

!!! tip "Prefer .items() for both"
    When you need keys and values, loop `for key, val in d.items()` instead of indexing inside the loop.

!!! warning "Gotcha: don't change a dict while looping over it"
    Adding or removing keys during iteration raises `RuntimeError`. Loop over a copy — `for key in list(d):` — or build a new dict with a [comprehension](comprehensions.md).
