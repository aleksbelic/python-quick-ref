# Scope & Closures

Where a name is visible, how Python finds it, and how an inner function can remember the variables around it.

## The LEGB rule

When Python meets a name, it searches four scopes, innermost first, and uses the first match:

| Letter | Scope | Example |
| --- | --- | --- |
| **L**ocal | the current function | parameters and names assigned in the function |
| **E**nclosing | any outer function | variables of a function that contains this one |
| **G**lobal | the module | names defined at the top of the file |
| **B**uilt-in | the `builtins` module | `len`, `print`, `Exception` |

```python
x = 'global'


def outer():
    x = 'enclosing'

    def inner():
        print(x)  # found in the enclosing scope

    inner()


outer()  # enclosing
```

Scope is decided by *where the code is written* (lexical scope), not by who calls the function.

## Assignment makes a name local

If a function **assigns** to a name anywhere in its body, that name is local for the *whole* function. Reading it before the assignment is an error, even if a global of the same name exists.

```python
counter = 0


def broken():
    counter += 1  # UnboundLocalError: counter is local, but has no value yet


def fixed():
    global counter
    counter += 1
```

`global name` says "this name refers to the module-level one". It works, but shared mutable state makes code harder to test and reason about; prefer parameters and return values.

!!! note "Mutating is not rebinding"
    `items.append(x)` on a global list needs no `global`, because it changes the object and does not assign to the name. Only `items = ...` would rebind.

## Closures

A **closure** is a function that keeps access to variables of the enclosing function even after that function has returned. The inner function remembers the *variables*, not copies of their values at that moment.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count   # rebind the enclosing variable
        count += 1
        return count

    return increment


counter = make_counter()
print(counter(), counter(), counter())  # 1 2 3
```

`nonlocal` is the enclosing-scope counterpart of `global`: it lets the inner function **rebind** an enclosing name. Each call of `make_counter()` creates a separate `count`, so separate counters do not interfere. Closures are the machinery behind [decorators](decorators.md) and factory functions.

## Late binding in loops

Because a closure remembers the *variable*, a function created inside a loop sees the variable's value at **call time**, not at creation time.

```python
functions = [lambda: i for i in range(3)]
print([f() for f in functions])  # [2, 2, 2]

functions = [lambda i=i: i for i in range(3)]  # bind the current value as a default
print([f() for f in functions])  # [0, 1, 2]
```

## Class bodies and comprehensions

- Code in a **class body** runs in its own namespace, but methods do *not* see it as an enclosing scope. Inside a method, reach class attributes through `self` or the class name.
- A **comprehension** has its own scope, so its loop variable does not leak into the surrounding code.
- Names bound by `import`, `def`, `class`, `for`, and `with ... as` follow the same scoping rules as plain assignment.

## Shadowing

An inner scope can reuse a name from an outer one, hiding it. This is legal but a common source of confusion, especially when you shadow a built-in such as `list` or `id` (see [Variables](variables.md#naming)).

!!! tip "Rule of thumb"
    Read freely from outer scopes, but avoid rebinding them. If a function needs to remember state, make that state an argument, an attribute of an object ([Classes](classes.md)), or a closure variable declared with `nonlocal`.
