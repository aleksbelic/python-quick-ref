# Iterators

The protocol behind every `for` loop, comprehension, and unpacking: what an *iterable* is, what an *iterator* is, and how they differ.

## Iterable vs iterator

- An **iterable** is anything you can loop over: it can produce an iterator on request. Lists, strings, tuples, dicts, sets, files, and `range` are iterables.
- An **iterator** is the object that actually produces the values one at a time and remembers its position. It is *used up* once exhausted.

Two built-in functions connect them: `iter(iterable)` returns an iterator, and `next(iterator)` returns the next value or raises `StopIteration` when there are no more.

```python
letters = ['a', 'b']
it = iter(letters)       # the list is the iterable, `it` the iterator
print(next(it))          # a
print(next(it))          # b
# next(it)               # StopIteration
```

## What a `for` loop does

```python
for item in collection:
    print(item)
```

is roughly shorthand for:

```python
iterator = iter(collection)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)
```

Everything that consumes an iterable uses the same protocol: `list(x)`, `sum(x)`, `sorted(x)`, `' '.join(x)`, `*x` unpacking, `in`, `zip`, and comprehensions.

## The two protocol methods

| Method | Called by | Must return |
| --- | --- | --- |
| `__iter__(self)` | `iter(obj)` | an iterator |
| `__next__(self)` | `next(obj)` | the next value, or raise `StopIteration` |

An iterator implements both, with `__iter__` returning `self`, so iterators are themselves iterable. A container usually implements only `__iter__`, returning a fresh iterator each time, which is why you can loop over a list as often as you like.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print(list(Countdown(3)))  # [3, 2, 1]
```

A [generator function](generators.md) is the short way to write the same thing: Python builds the iterator class for you.

## Iterators are single-use

An iterator keeps its position, so a second pass finds it empty. A container produces a new iterator each time and does not have this problem.

```python
it = iter([1, 2, 3])
print(sum(it))  # 6
print(sum(it))  # 0, already exhausted
```

## Lazy evaluation

Many built-ins return iterators rather than lists, computing items only when asked: `map`, `filter`, `zip`, `enumerate`, `reversed`, and generator expressions. This keeps memory flat for large or endless data, but means you must wrap them in `list()` when you want to see or reuse the results.

`range` is a slight exception: it is a lazy **sequence** (you can index it and take `len()`), and each loop gets a fresh iterator.

Dictionary **views** (`d.keys()`, `d.values()`, `d.items()`) are iterable and reflect later changes to the dict.

## `itertools`: building blocks

The standard `itertools` module provides fast, memory-friendly iterator tools. A tour of the names worth knowing:

| Tool | What it does |
| --- | --- |
| `count()`, `cycle()`, `repeat()` | endless iterators |
| `islice(it, n)` | slice any iterator (indexing does not work on iterators) |
| `chain(a, b)` | one iterator over several |
| `zip_longest(a, b)` | like `zip`, padding the shorter input |
| `groupby(it, key)` | group *consecutive* items with the same key (sort first) |
| `product`, `permutations`, `combinations` | combinatorics |
| `accumulate(it)` | running totals |
| `batched(it, n)` | chunks of size `n` (3.12+) |

## `iter()` with a sentinel

`iter(callable, sentinel)` calls a function repeatedly until it returns the sentinel value. Reading a file in fixed-size blocks until an empty result is the classic use.

!!! tip "Iterable or iterator?"
    Ask: "can I loop over it twice?" Yes → it is a container (iterable). No → it is an iterator, so store its items in a list first if you need them again.
