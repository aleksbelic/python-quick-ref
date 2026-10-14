# For Loop

Iterates over iterable objects — strings, lists, tuples, sets, dictionaries, or `range()`.

## Iterating a string

Looping over a string yields one character at a time.

```python
for x in 'abc':
    print(x)
```

## Iterating a list

Same syntax works for lists.

```python
friends = ['Lucky', 'Joey', 'Chandler']
for f in friends:
    print('Hi', f)
```

## For-else

The `else` block runs after the loop completes without `break`.

```python
for x in 'abc':
    print(x)
else:
    print('finished!')
```

## Iterating a range

`range(3)` yields `0`, `1`, `2` — useful when you need an index counter.

```python
for num in range(3):
    print(num)
```

!!! tip "for vs while"
    Prefer `for` when iterating a known sequence. Use `while` when looping until a condition changes.
