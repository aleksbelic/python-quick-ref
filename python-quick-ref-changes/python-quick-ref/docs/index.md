# Python Quick Reference

Short lessons — one topic per page, grouped by theme. The focus is on *understanding*: what each feature is, why Python works that way, and which traps to avoid. Short snippets illustrate the ideas; the expected output is shown in comments, so you can follow along without running anything.

## How to use this site

- **Learning from scratch?** Read the sections top to bottom: Setup → Basics → Data Structures → Control Flow → Functions & OOP → I/O & Modules → Going Further.
- **Looking something up?** Use the search box, or jump straight to the [Cheat Sheet](cheatsheet.md).
- **Want to see it all together?** [Complexity & Patterns](complexity.md) shows how classic small problems (Fibonacci, primes, palindromes, word counts) turn into reusable ideas.

Look out for the callouts: **tip** boxes add a useful habit, **gotcha** boxes warn about a classic trap. Notes like "3.10+" mark features that need a newer Python.

## Setup

- [Python Installation](setup/python-installation.md) — installing Python 3.11+
- [Virtual Env](setup/virtual-env.md) — isolated environments and pip basics
- [Tooling](setup/tooling.md) — uv, pyproject.toml, ruff, type checkers

## Basics

- [How Python Works](how-python-works.md) — interpreter, bytecode, names and objects, namespaces
- [Syntax Basics](syntax.md) — comments, docstrings, indentation, `pass`
- [Variables](variables.md) — assignment, naming, constants
- [Data Types](data-types.md) — the core built-in types
- [Numbers](numbers.md) — integers, floats, rounding, precision, bitwise operators
- [Casting](casting.md) — converting between types
- [Operators](operators.md) — arithmetic, comparison, logical, membership
- [Conditions](conditions.md) — `if` / `elif` / `else`, truthiness, `match`

## Data Structures

- [Strings](strings.md) — indexing, slicing, searching, transforming
- [Text & Encoding](unicode.md) — Unicode, `str` vs `bytes`, UTF-8
- [Lists](lists.md) — ordered, changeable sequences
- [Tuples](tuples.md) — ordered, immutable sequences
- [Sets](sets.md) — unique unordered items
- [Dictionaries](dictionaries.md) — key–value mappings
- [Comprehensions](comprehensions.md) — building collections in one expression
- [Collections](collections.md) — `Counter`, `defaultdict`, `deque`, `namedtuple`
- [Mutable vs Immutable](mutable-immutable.md) — references, copies, hashability
- [Complexity & Patterns](complexity.md) — Big-O, cost of operations, classic problem-solving ideas

## Control Flow

- [Loops](loops.md) — `for`, `while`, `range`, `enumerate`, `zip`
- [Iterators](iterators.md) — the protocol behind every `for` loop
- [Try–Except](try-except.md) — handling and raising errors
- [Context Managers](context-managers.md) — `with` and guaranteed clean-up

## Functions & OOP

- [Functions](functions.md) — arguments, scope, lambdas
- [Scope & Closures](scope-closures.md) — LEGB, `global`, `nonlocal`, late binding
- [Generators](generators.md) — lazy sequences with `yield`
- [Decorators](decorators.md) — wrapping functions
- [Classes](classes.md) — attributes, methods, inheritance, properties
- [OOP Concepts](oop-concepts.md) — encapsulation, composition, MRO, abstract classes, enums
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

## Going Further

- [Concurrency](concurrency.md) — threads, processes, `asyncio`, the GIL
- [Testing](testing.md) — kinds of tests, fixtures, mocks, design for testability
- [What's New (3.10–3.15)](modern-python.md) — features by release

## Cheat Sheet

- [Cheat Sheet](cheatsheet.md) — built-ins, methods, format specs, exceptions, precedence, complexity, version notes
