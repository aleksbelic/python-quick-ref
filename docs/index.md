# Python Quick Reference

Short lessons — one topic per page, grouped by theme. Snippets are short enough to try yourself — paste one into a file and run it.

## How to use this site

- **Learning from scratch?** Read the sections top to bottom: Setup → Basics → Data Structures → Control Flow → Functions & OOP → I/O & Modules.
- **Looking something up?** Use the search box, or jump straight to the [Cheat Sheet](cheatsheet.md).
- **Want to see it all together?** The [Examples](examples/fibonacci.md) combine several chapters into small, tested programs.

Look out for the callouts: **tip** boxes add a useful habit, **gotcha** boxes warn about a classic trap. Notes like "3.10+" mark features that need a newer Python.

## Setup

- [Python Installation](setup/python-installation.md) — installing Python 3.11+
- [Virtual Env](setup/virtual-env.md) — isolated environments and pip basics
- [Tooling](setup/tooling.md) — uv, pyproject.toml, ruff, type checkers

## Basics

- [Syntax Basics](syntax.md) — comments, docstrings, indentation, `pass`
- [Variables](variables.md) — assignment, naming, constants
- [Data Types](data-types.md) — the core built-in types
- [Casting](casting.md) — converting between types
- [Operators](operators.md) — arithmetic, comparison, logical, membership
- [Conditions](conditions.md) — `if` / `elif` / `else`, truthiness, `match`

## Data Structures

- [Strings](strings.md) — indexing, slicing, searching, transforming
- [Lists](lists.md) — ordered, changeable sequences
- [Tuples](tuples.md) — ordered, immutable sequences
- [Sets](sets.md) — unique unordered items
- [Dictionaries](dictionaries.md) — key–value mappings
- [Comprehensions](comprehensions.md) — building collections in one expression
- [Collections](collections.md) — `Counter`, `defaultdict`, `deque`, `namedtuple`
- [Mutable vs Immutable](mutable-immutable.md) — references, copies, what can change in place

## Control Flow

- [Loops](loops.md) — `for`, `while`, `range`, `enumerate`, `zip`
- [Try–Except](try-except.md) — handling and raising errors

## Functions & OOP

- [Functions](functions.md) — arguments, scope, lambdas
- [Generators](generators.md) — lazy sequences with `yield`
- [Decorators](decorators.md) — wrapping functions
- [Classes](classes.md) — attributes, methods, inheritance, properties
- [Dunders](dunders.md) — double-underscore methods
- [Dataclasses](dataclasses.md) — less boilerplate for data holders
- [Type Hints](type-hints.md) — annotating code for humans and checkers

## I/O & Modules

- [Input & Output](input.md) — `input()`, `print()`, stderr
- [Formatting](formatting.md) — f-strings and `format()`
- [Files & Paths](files.md) — `open()` and `pathlib`
- [CSV](csv.md) — reading and writing CSV files
- [JSON](json.md) — `json.dumps`, `json.loads`, files
- [Dates & Times](datetime.md) — `datetime`, `timedelta`, time zones
- [RegExp](regexp.md) — searching and replacing with `re`
- [Imports & Packages](imports.md) — modules, packages, import styles
- [Scripts & CLI](scripts.md) — `__main__`, `argparse`, exit codes
- [Logging](logging.md) — levels, handlers, loggers

## Cheat Sheet

- [Cheat Sheet](cheatsheet.md) — built-ins, string/list/dict/set methods, format specs, exceptions

## Examples

- [Fibonacci](examples/fibonacci.md) — n-th Fibonacci number
- [Palindrome](examples/palindrome.md) — palindrome check
- [Prime Number](examples/prime-number.md) — primality test
- [Word Counter](examples/word-counter.md) — word frequencies with `Counter`
- [CSV Summary](examples/csv-summary.md) — statistics from a CSV column
- [File Renamer](examples/file-renamer.md) — safe batch renaming with `pathlib`
- [Testing](examples/testing.md) — testing the examples with pytest
