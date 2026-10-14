# Comprehensions

A compact way to build a list, dict, or set from another iterable in a single expression.

## List comprehension

`[expression for item in iterable]` — the loop and the `append()` in one line.

```python
squares = [n ** 2 for n in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# the same with a regular loop
squares = []
for n in range(5):
    squares.append(n ** 2)
```

## Filtering with if

Add `if condition` at the end to keep only some items.

```python
evens = [n for n in range(10) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

words = ['apple', 'fig', 'banana']
long_words = [w.upper() for w in words if len(w) > 3]
print(long_words)  # ['APPLE', 'BANANA']
```

## Conditional values

An `if`/`else` *before* the `for` chooses the value instead of filtering.

```python
labels = ['even' if n % 2 == 0 else 'odd' for n in range(4)]
print(labels)  # ['even', 'odd', 'even', 'odd']
```

## Nested loops

Read the `for` clauses left to right, exactly like nested loops.

```python
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)  # [(0, 0), (0, 1), (1, 0), (1, 1)]

matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```

## Dict and set comprehensions

```python
lengths = {w: len(w) for w in ['apple', 'fig']}
print(lengths)  # {'apple': 5, 'fig': 3}

unique_lengths = {len(w) for w in ['apple', 'pear', 'fig', 'plum']}
print(sorted(unique_lengths))  # [3, 4, 5]

# invert a dict
inverted = {value: key for key, value in lengths.items()}
print(inverted)  # {5: 'apple', 3: 'fig'}
```

## Generator expressions

Use parentheses to produce items lazily instead of building a list. Ideal as the only argument of `sum()`, `any()`, `all()`, `max()`.

```python
total = sum(n ** 2 for n in range(1000))
print(total)  # 332833500

print(any(n > 990 for n in range(1000)))  # True
```

See [Generators](generators.md) for details.

!!! tip "When not to use a comprehension"
    If it needs more than one `for` plus a condition, or has side effects such as `print()`, use a regular loop. Readability beats cleverness.
