# Testing

Why and how to test: the kinds of tests, what makes a good one, the vocabulary of fixtures and mocks, and how to write code that is easy to test. Concepts first; the tool shown is `pytest`, but the ideas apply to any framework.

## Why test

Tests are executable specifications. They tell you when a change breaks something, document what the code is supposed to do, and make refactoring safe. A bug that is caught by a test costs minutes; one caught in production costs far more.

## Kinds of tests

| Kind | Checks | Speed | Typical count |
| --- | --- | --- | --- |
| **Unit** | one function or class in isolation | milliseconds | many |
| **Integration** | several parts working together (code + database, code + files) | slower | some |
| **End-to-end** | the whole program as a user would use it | slowest | few |

This is the **test pyramid**: a wide base of fast unit tests, a thinner layer of integration tests, and a few end-to-end tests on top. Inverting it gives a slow, fragile suite.

## Anatomy of a test

A good test has three phases, **Arrange – Act – Assert**:

1. **Arrange**: set up inputs and objects.
2. **Act**: call the code under test, once.
3. **Assert**: check the outcome.

```python
def test_discount_applies_to_total():
    cart = Cart(prices=[10, 20])          # arrange
    total = cart.total(discount=0.1)      # act
    assert total == 27                    # assert
```

A test **passes** if it finishes without an exception; a failing `assert` reports both sides. In `pytest` any function named `test_*` in a file named `test_*.py` is collected and run automatically.

### Properties of good tests

- **Independent**: no test depends on another's side effects or run order.
- **Deterministic**: same result every run. Beware of the clock, randomness, and the network.
- **Fast**: otherwise nobody runs them.
- **Readable**: the name says what behaviour is expected (`test_empty_cart_total_is_zero`).
- **Focused**: one reason to fail.

## What to test

Write cases for the **normal path**, the **boundaries** (0, 1, empty, maximum), **invalid input** (the right exception is raised, see [Try–Except](try-except.md)), and every **bug you fix** (a *regression test* so it cannot come back). Floating-point results should be compared with a tolerance (`pytest.approx`, `math.isclose`; see [Numbers](numbers.md)).

## Fixtures and parametrization

- A **fixture** is reusable setup (and tear-down) that tests request by name: a temporary folder, a prepared object, a database connection. They keep arrange steps out of the tests.
- **Parametrization** runs one test body against many input/expected pairs, so adding a case is one line instead of a new function.

```python
import pytest


@pytest.mark.parametrize('n, expected', [(0, False), (1, False), (2, True), (9, False)])
def test_is_prime(n, expected):
    assert is_prime(n) is expected
```

## Test doubles: stubs, fakes, mocks

Code often depends on something slow, random, or external. A **test double** stands in for it:

| Double | Role |
| --- | --- |
| **Stub** | returns canned answers |
| **Fake** | a simple working replacement (in-memory database) |
| **Mock** | records how it was called so you can assert on interactions |

`unittest.mock` and pytest's `monkeypatch` provide them. Use doubles at the *edges* (network, clock, filesystem), not between your own small functions; over-mocking makes tests that pass while the real code is broken.

## Design for testability

Code is easy to test when it is made of **small functions that take their inputs as arguments and return results**, instead of reading global state or hard-coded paths and printing. For example, a function that accepts an open file object (or just a list of rows) can be tested with an in-memory `io.StringIO`; one that opens `'data/users.csv'` itself cannot. See [pattern 5 in Complexity & Patterns](complexity.md#5-separate-logic-from-inputoutput). Dependencies passed in from outside ("dependency injection") are what make doubles easy to swap in.

## Process and tools

- **TDD** (test-driven development): *red* (write a failing test), *green* (make it pass with the simplest code), *refactor* (clean up while the tests protect you).
- **Coverage** measures which lines the tests executed. It can show what is *untested* but not whether the tests are *good*: 100% coverage with weak assertions proves little.
- **Property-based testing** (the Hypothesis library) generates many random inputs and checks that a *property* always holds ("reversing a list twice gives the original"), finding edge cases you would not think of.
- **doctest** runs examples embedded in docstrings; **unittest** is the standard-library framework (class-based); **pytest** is the de-facto standard, with plain `assert` and fixtures.

!!! tip "Test behaviour, not implementation"
    Assert on what a function promises (its result and visible effects), not on how it gets there. Then you can rewrite the internals freely and the tests keep passing.
