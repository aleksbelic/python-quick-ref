# How Python Works

A mental model of what happens between typing code and seeing a result. Almost every "weird" Python behaviour in later lessons follows from the ideas on this page.

## From source to execution

Python is both compiled and interpreted. When you run a program, the reference implementation (**CPython**) does two things:

1. **Compile** your source into *bytecode*: a compact, low-level instruction list for a virtual machine. Bytecode of imported modules is cached in `__pycache__/*.pyc` so the next import is faster.
2. **Interpret** that bytecode: the Python virtual machine executes the instructions one by one.

```text
source (.py)  →  bytecode (.pyc)  →  Python virtual machine  →  result
```

"Python" is the language; CPython is just the most common implementation. Others exist (PyPy has a just-in-time compiler, MicroPython targets microcontrollers). CPython also ships an experimental JIT compiler from 3.13 onwards, which was upgraded again in 3.15 — an optimisation, not a change in language behaviour.

## Three ways code runs

| How | What it is |
| --- | --- |
| **REPL** (`python`) | read a statement, run it, print the result of expressions, repeat; ideal for experiments |
| **Script** (`python file.py`) | the file runs top to bottom as the module `__main__` |
| **Module** (`import x`, `python -m x`) | the file runs once and becomes a reusable namespace; see [Imports](imports.md) |

## Names and objects

Everything you handle in Python is an **object**: numbers, strings, functions, classes, modules. Each object has

- an **identity** (where it lives; `id(x)`),
- a **type** (what it is and can do; `type(x)`),
- a **value** (its data; may or may not be changeable).

A **name** is only a label attached to an object. The statement `x = 5` does not put 5 "in" `x`; it makes the name `x` refer to an int object. Assignment never copies an object, it binds a name. This single rule explains aliasing, mutable default arguments, and why functions can modify the lists you pass in — see [Mutable vs Immutable](mutable-immutable.md).

## Typing: dynamic but strong

- **Dynamic**: names have no fixed type; the *object* has one, and it is checked when an operation runs. The same name may later refer to an object of another type.
- **Strong**: Python does not guess between unrelated types. `'1' + 2` is an error rather than `'12'` or `3`.
- **Duck typing**: code cares what an object can *do*, not what class it is. If it has the right methods, it works ("if it walks like a duck..."). See [OOP Concepts](oop-concepts.md#polymorphism-and-duck-typing).

[Type hints](type-hints.md) add optional, tool-checked documentation on top of this; they do not change how the program runs.

## Statements and expressions

An **expression** produces a value (`2 + 3`, `len(x)`, `a if c else b`). A **statement** performs an action (`x = 1`, `if`, `for`, `def`, `import`, `return`). Expressions can appear inside statements, not the other way round (with the walrus operator as a deliberate exception).

`def` and `class` are *executable statements*. When Python reaches a `def`, it creates a function object and binds it to a name, at that moment. That is why default argument values are evaluated once, at definition time ([Functions](functions.md#default-values)), and why a function can only be called after its `def` has run.

## Namespaces

A **namespace** is a mapping from names to objects. Python has several, searched in a fixed order: local → enclosing functions → module (global) → built-ins. Each module, function call, and class body gets its own. Details and consequences: [Scope & Closures](scope-closures.md).

## Memory management

You never free memory by hand. CPython uses **reference counting**: each object counts how many names and containers refer to it, and is discarded when the count reaches zero. A **cycle collector** additionally cleans up objects that refer to each other but are unreachable. Consequences:

- `del x` removes the *name* `x`, not necessarily the object;
- an object stays alive while anything still refers to it (a list in a global, a closure, a cached result);
- resources such as files should be released explicitly, not by waiting for garbage collection — that is what [context managers](context-managers.md) are for.

## The GIL, briefly

In standard CPython, a lock called the **Global Interpreter Lock** lets only one thread execute Python bytecode at a time. It simplifies memory management but shapes how you use threads; see [Concurrency](concurrency.md).

## Python's design principles

`import this` prints "The Zen of Python". Three ideas recur throughout this reference: *readability counts*, *explicit is better than implicit*, and *there should be one obvious way to do it*. When two styles compete, the readable and explicit one is usually the Pythonic one.

!!! tip "Learning order"
    If one thing from this page sticks, make it this: **names refer to objects, and assignment never copies**. Revisit it whenever a bug involves "I changed X but Y changed too".
