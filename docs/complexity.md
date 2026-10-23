# Complexity & Patterns

How to reason about how fast and how memory-hungry code is, which built-in structure fits which job, and a handful of problem-solving patterns that recur everywhere.

## Big-O in one minute

**Big-O notation** describes how the cost of an operation *grows* with the input size `n`, ignoring constant factors. It is about shape, not stopwatch time.

| Class | Name | Example |
| --- | --- | --- |
| O(1) | constant | list index, dict lookup |
| O(log n) | logarithmic | binary search |
| O(n) | linear | scanning a list, `sum()` |
| O(n log n) | linearithmic | sorting |
| O(n²) | quadratic | comparing every pair (nested loops) |
| O(2ⁿ) | exponential | naive recursive Fibonacci |

Two refinements: **amortized** cost averages out occasional expensive steps (`list.append` is O(1) amortized: the array sometimes grows and copies, but rarely), and **average vs worst case** can differ (a dict is O(1) on average, O(n) if every key collides).

## Cost of built-in operations

| Structure | Fast: O(1) | Slow: O(n) |
| --- | --- | --- |
| `list` | index, `append()`, `pop()` (end) | `in`, `insert(0, x)`, `pop(0)`, `remove()`, `index()` |
| `dict` | get, set, delete, `in` (by key) | search by *value* |
| `set` | `add`, `discard`, `in` | — |
| `deque` | append/pop at *both* ends | index into the middle |
| `str` | index, `len()` | concatenation (a new string each time), `in`, `replace()` |

Why dicts and sets are O(1): they are **hash tables**. `hash(key)` selects a slot directly, so no scanning is needed ([hashability](mutable-immutable.md#hashability-what-can-be-a-key)). Lists are dynamic arrays: jumping to an index is instant, but shifting elements to insert at the front is not.

!!! tip "The cheapest optimisation"
    Replacing `x in some_list` with `x in some_set` inside a loop turns an O(n²) program into an O(n) one. Choose the data structure before micro-optimising code.

## Sorting and searching

`sorted()` and `list.sort()` use **Timsort**: O(n log n) worst case, close to O(n) on nearly sorted data, and *stable* (equal items keep their original order, so you can sort by several keys in turn). Searching a **sorted** list with the `bisect` module is O(log n). `heapq` gives the smallest items of a collection in O(log n) per push or pop.

## Time vs space

Faster code often spends more memory (caches, lookup tables), and lazy code ([generators](generators.md)) trades repeatability for memory. State both costs when you analyse an approach. Fibonacci below needs O(1) extra space with a loop but O(n) with memoization.

## Patterns worth recognising

These small problems (Fibonacci, primes, palindromes, word counts) are classic because each teaches a reusable idea.

### 1. Iterate instead of recursing; cache overlapping work

The naive recursion `fib(n) = fib(n-1) + fib(n-2)` recomputes the same values over and over: O(2ⁿ) calls. Two fixes:

- **memoization**: remember results (`functools.cache`), reducing it to O(n);
- **iteration**: keep only the last two values and update both at once, O(n) time and O(1) space.

```python
def nth_fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b    # tuple assignment updates both together
    return a
```

Python caps recursion depth (see [Functions](functions.md#recursion)), another reason to prefer loops for long chains.

### 2. Stop early with a bound

To test whether `n` is prime you only need to try divisors up to √n: divisors come in pairs `(d, n/d)`, and one of each pair is ≤ √n. That cuts O(n) work to O(√n). Use `math.isqrt(n)`, the *exact* integer square root, rather than `int(n ** 0.5)`, which goes through inexact floating-point.

### 3. Normalise, then compare

For palindromes, anagrams, duplicate detection and similar problems, first convert both sides to a **canonical form** (lower-case, strip punctuation, sort letters), then compare. Most of the bugs live in the normalisation step, so keep it a small separate function. See also [Unicode normalization](unicode.md#len-counts-code-points-not-what-you-see).

### 4. Count with a hash table

Counting frequencies, grouping, and finding duplicates all become a single O(n) pass with a dict, `Counter`, or `defaultdict` ([Collections](collections.md)), instead of an O(n²) pair of loops. Tokenise with a regular expression rather than `split()` when punctuation must not stick to words.

### 5. Separate logic from input/output

A function that takes data (or an open file object) and *returns* a result can be reused and tested with in-memory input. A function that reads a hard-coded path and prints cannot. Keep the computation pure, and let a thin outer layer do the reading and printing ([Testing](testing.md)).

### 6. Be safe by default

For anything destructive, like renaming or deleting files, plan first and act second: build the list of changes, offer a **dry run**, skip items already processed so running twice is harmless (*idempotence*), and make the safe behaviour the default argument.

!!! tip "Measure, don't guess"
    Reasoning with Big-O tells you what *scales*. Profile (`timeit`, `cProfile`, and from 3.15 the `profiling.sampling` profiler) to find what is actually slow before you optimise.
