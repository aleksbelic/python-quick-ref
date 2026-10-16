# Generators

A generator produces values one at a time, on demand, instead of building a whole collection in memory. Generators are the easiest way to write an *iterator* — read [Iterators](iterators.md) first if "iterable" and "iterator" feel blurry.

## yield

A function containing `yield` returns a generator. Each `next()` call runs the function until the next `yield`, then pauses.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1


gen = countdown(3)
print(next(gen))  # 3
print(next(gen))  # 2
print(next(gen))  # 1
```

When the function ends, the generator raises `StopIteration` — a `for` loop handles that for you.

```python
for n in countdown(3):
    print(n)  # 3, 2, 1

print(list(countdown(3)))  # [3, 2, 1]
```

## Lazy and infinite sequences

Because nothing is computed up front, a generator can be infinite. Take only what you need with `itertools.islice`.

```python
from itertools import islice


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(islice(fibonacci(), 10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Generators are single-use

Once exhausted, a generator is empty. Create a new one to iterate again.

```python
squares = (n ** 2 for n in range(3))
print(list(squares))  # [0, 1, 4]
print(list(squares))  # []
```

## yield from

Delegate to another iterable.

```python
def chain(*iterables):
    for iterable in iterables:
        yield from iterable


print(list(chain([1, 2], 'ab')))  # [1, 2, 'a', 'b']
```

## Processing big files

Reading a file line by line is itself lazy, so a generator pipeline keeps memory flat even for huge inputs.

```python
def non_empty_lines(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield line


print(list(non_empty_lines(['a\n', '\n', 'b\n'])))  # ['a', 'b']
```

## Two-way generators

A generator can also *receive* values with `.send()`, be stopped early with `.close()`, and hand back a final result through `return` (carried in `StopIteration.value`). These are the building blocks that older asynchronous code was based on; today you will rarely write them by hand, but they explain why `yield` is an expression.

!!! tip "Generator or list?"
    Use a generator when you iterate once, or the data is large or infinite. Use a list when you need `len()`, indexing, or several passes.
