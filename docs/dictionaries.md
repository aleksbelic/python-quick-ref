# Dictionaries

Changeable key/value collections using `{}`. Keys must be unique, similar to JSON objects.

## Creating and accessing

Look up values by key; `len()` counts entries.

```python
d1 = {
    'name': 'Hans',
    'age': '32',
    'city': 'Berlin'
}

print(d1)  # {'name': 'Hans', 'age': '32', 'city': 'Berlin'}
print(d1['name'])  # 'Hans'
print(len(d1))  # 3
```

## Looping through keys

Iterating the dict directly yields keys; `.keys()` is equivalent.

```python
for key in d1:  # list keys
    print(key)
'''
name
age
city
'''
```

```python
for key in d1.keys():  # list keys
    print(key)
'''
name
age
city
'''
```

## Looping through values

Index each key to get its value.

```python
for key in d1:  # list values
    print(d1[key])
'''
Hans
32
Berlin
'''
```

## Looping through items

`.items()` yields `(key, value)` tuples, unpackable into two variables.

```python
for key_val_tuple in d1.items():  # list (key, value) as tuples
    print(key_val_tuple)
'''
('name', 'Hans')
('age', '32')
('city', 'Berlin')
'''
```

```python
for key, val in d1.items():  # list separated keys and values
    print(key, val)
'''
name Hans
age 32
city Berlin
'''
```

!!! tip "Prefer .items() for both"
    When you need keys and values, loop `for key, val in d.items()` instead of indexing inside the loop.
