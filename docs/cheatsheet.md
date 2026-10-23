# Cheat Sheet

Dense lookup tables. Follow the links for explanations and examples.

## Built-in functions

| Function | Purpose |
| --- | --- |
| `len(x)` | number of items |
| `sum(x)`, `min(x)`, `max(x)` | aggregate numbers |
| `sorted(x, key=, reverse=)` | new sorted list |
| `reversed(x)` | iterator over `x` backwards |
| `enumerate(x, start=0)` | `(index, item)` pairs |
| `zip(a, b)` | parallel iteration |
| `range(start, stop, step)` | integer sequence |
| `any(x)`, `all(x)` | is any / every item truthy |
| `map(f, x)`, `filter(f, x)` | lazy transform / filter |
| `abs(n)`, `round(n, d)`, `divmod(a, b)` | numeric helpers |
| `isinstance(x, T)`, `type(x)` | inspect types |
| `iter(x)`, `next(it, default)` | get an iterator / advance it ([Iterators](iterators.md)) |
| `ord(c)`, `chr(n)` | character ↔ code point ([Text & Encoding](unicode.md)) |
| `id(x)`, `hash(x)` | identity / hash value |
| `getattr(o, name, default)`, `hasattr(o, name)` | dynamic attribute access |
| `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()` | construct / convert |
| `open()`, `print()`, `input()` | I/O |
| `help(x)`, `dir(x)` | explore objects in the REPL |

## String methods

See [Strings](strings.md).

| Method | Result |
| --- | --- |
| `s.upper()`, `s.lower()`, `s.capitalize()`, `s.title()` | change case |
| `s.strip()`, `s.lstrip()`, `s.rstrip()` | trim whitespace (or given characters) |
| `s.split(sep)`, `sep.join(items)` | break apart / join |
| `s.replace(old, new)` | substitute |
| `s.find(x)`, `s.index(x)`, `s.count(x)` | locate / count (`find` gives `-1`, `index` raises) |
| `s.startswith(x)`, `s.endswith(x)` | prefix / suffix test |
| `s.isdigit()`, `s.isalpha()`, `s.isalnum()` | content tests |
| `s.zfill(n)`, `s.center(n)`, `s.ljust(n)`, `s.rjust(n)` | padding |

## List methods

See [Lists](lists.md).

| Method | Effect |
| --- | --- |
| `l.append(x)` | add to the end |
| `l.insert(i, x)` | add at index |
| `l.extend(it)` | add all items of `it` |
| `l.remove(x)` | delete first `x` |
| `l.pop(i=-1)` | delete and return item |
| `l.index(x)`, `l.count(x)` | position / occurrences |
| `l.sort(key=, reverse=)` | sort in place (returns `None`) |
| `l.reverse()` | reverse in place |
| `l.copy()`, `l.clear()` | shallow copy / empty it |

## Dict methods

See [Dictionaries](dictionaries.md).

| Method | Effect |
| --- | --- |
| `d[k]`, `d.get(k, default)` | lookup (`[]` raises `KeyError`) |
| `d[k] = v` | add or change |
| `d.pop(k, default)`, `del d[k]` | remove |
| `d.setdefault(k, default)` | get, inserting `default` if missing |
| `d.update(other)`, `d | other` | merge |
| `d.keys()`, `d.values()`, `d.items()` | views for looping |
| `k in d` | key membership |

## Set operations

See [Sets](sets.md).

| Expression | Meaning |
| --- | --- |
| `a | b` | union |
| `a & b` | intersection |
| `a - b` | in `a` but not in `b` |
| `a ^ b` | in exactly one |
| `a <= b` | `a` is a subset of `b` |
| `s.add(x)`, `s.discard(x)`, `s.remove(x)` | add / remove (`remove` raises if missing) |

## Format specs

Used in [f-strings](formatting.md): `f'{value:spec}'`.

| Spec | Example | Result |
| --- | --- | --- |
| `.2f` | `f'{3.14159:.2f}'` | `3.14` |
| `,` | `f'{1234567:,}'` | `1,234,567` |
| `.1%` | `f'{0.256:.1%}'` | `25.6%` |
| `05d` | `f'{42:05d}'` | `00042` |
| `>8` | `f'{"hi":>8}'` | `      hi` |
| `<8` | `f'{"hi":<8}'` | `hi      ` |
| `^8` | `f'{"hi":^8}'` | `   hi   ` |
| `x`, `b`, `o` | `f'{255:x}'` | `ff` |
| `=` | `f'{x=}'` | `x=5` |

## Common exceptions

See [Try–Except](try-except.md).

| Exception | Typical cause |
| --- | --- |
| `ValueError` | right type, wrong value |
| `TypeError` | wrong type for an operation |
| `KeyError` / `IndexError` | missing key / index out of range |
| `AttributeError` | attribute does not exist |
| `FileNotFoundError` | path does not exist |
| `ZeroDivisionError` | division by zero |
| `ImportError` | module or name can't be imported |
| `StopIteration` | iterator is exhausted |
| `RecursionError` | recursion went too deep |
| `UnicodeDecodeError` | bytes don't match the encoding ([Text & Encoding](unicode.md)) |
| `UnboundLocalError` | local name used before assignment ([Scope](scope-closures.md)) |

## Operator precedence (high → low)

`**`, unary `-x ~x`, `* / // %`, `+ -`, `<< >>`, `&`, `^`, `|`, comparisons / `in` / `is`, `not`, `and`, `or`, `lambda`, conditional expression, `:=`. Full table: [Operators](operators.md#operator-precedence).

## Scope lookup (LEGB)

**L**ocal → **E**nclosing function → **G**lobal (module) → **B**uilt-in. `global x` and `nonlocal x` let a function rebind an outer name. See [Scope & Closures](scope-closures.md).

## Complexity at a glance

| Operation | Cost |
| --- | --- |
| `list[i]`, `dict[k]`, `x in set` | O(1) |
| `list.append(x)` | O(1) amortized |
| `x in list`, `list.insert(0, x)`, `list.pop(0)` | O(n) |
| `sorted(x)` | O(n log n) |

See [Complexity & Patterns](complexity.md).

## Truthy and falsy

Falsy: `False`, `None`, `0`, `0.0`, `''`, `[]`, `()`, `{}`, `set()`. Everything else is truthy. See [Conditions](conditions.md#truthy-and-falsy-values).

## Python version notes

| Feature | Since |
| --- | --- |
| f-strings | 3.6 |
| walrus operator `:=` | 3.8 |
| `f'{x=}'` debugging | 3.8 |
| `list[int]`, `dict | dict` | 3.9 |
| `match` statement, `X | Y` types | 3.10 |
| `dataclass(slots=True)` | 3.10 |
| `ExceptionGroup`, `except*`, `tomllib`, `Self` | 3.11 |
| `type` alias statement, `def f[T]()`, `itertools.batched` | 3.12 |
| free-threaded build (experimental), new REPL | 3.13 |
| t-strings, lazy annotations, `except A, B:` | 3.14 |
| `lazy import`, `frozendict`, `sentinel`, UTF-8 default, `[*x for x in xs]` | 3.15 |

More detail in [What's New](modern-python.md).
