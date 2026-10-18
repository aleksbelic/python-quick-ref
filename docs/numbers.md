# Numbers

How Python represents integers and floating-point numbers, why `0.1 + 0.2` is not `0.3`, and which tool to reach for instead.

## Integers

`int` has **arbitrary precision**: it grows as large as memory allows, so there is no overflow. Python integers are exact, which is why they are also the right type for money held in the smallest unit (cents).

```python
print(2 ** 100)  # 1267650600228229401496703205376
```

`bool` is a subclass of `int`: `True == 1`, `False == 0`, and `True + True` is `2`.

!!! note "Guard against huge digit strings"
    Converting a *string* of more than 4300 digits to an `int` (or back) raises `ValueError` by default, a protection against denial-of-service input. The limit is adjustable (`sys.set_int_max_str_digits`), but think twice before lifting it for untrusted data.

## Floating-point numbers

A `float` is a 64-bit **IEEE 754 binary** number: 1 sign bit, 11 exponent bits, 52 fraction bits, giving roughly 15–17 significant decimal digits. Two consequences follow.

**Most decimals are approximations.** Just as `1/3` has no finite decimal expansion, `0.1` has no finite *binary* expansion, so the stored value is the closest representable one.

```python
print(0.1 + 0.2)           # 0.30000000000000004
print(0.1 + 0.2 == 0.3)    # False
```

**Precision is relative.** Floats are dense near zero and sparse for large values. Above 2**53, not every integer can be represented, and adding a small number to a large one may do nothing.

Compare floats with a tolerance:

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### Special values

`float('inf')`, `float('-inf')` and `float('nan')` ("not a number") exist. `nan` is not equal to anything, **including itself**, so test for it with `math.isnan(x)`.

```python
nan = float('nan')
print(nan == nan)  # False
```

## Exact alternatives

| Type | Use it for | Notes |
| --- | --- | --- |
| `decimal.Decimal` | money, anything that must match decimal rules | build from strings: `Decimal('0.1')`, not `Decimal(0.1)` |
| `fractions.Fraction` | exact rational arithmetic | `Fraction(1, 3) + Fraction(1, 6)` is `Fraction(1, 2)` |
| `int` in smaller units | prices, durations | store cents or milliseconds, format on output |

These are slower than `float`, so use them when exactness matters more than speed.

## Division, floor, and modulo

`/` is true division and always returns a `float`. `//` is **floor** division: it rounds toward negative infinity, not toward zero. `%` is defined so that `a == (a // b) * b + a % b`.

```python
print(-7 // 2)       # -4, not -3
print(-7 % 2)        # 1
print(divmod(-7, 2)) # (-4, 1)
print(int(-3.5))     # -3, int() truncates toward zero
```

Because the result of `%` takes the sign of the divisor, `n % 2` is always `0` or `1` in Python, even for negative `n`.

## Rounding

`round()` uses **round half to even** ("banker's rounding"): ties go to the nearest even digit, which avoids a systematic upward bias when summing many rounded values.

```python
print(round(0.5), round(1.5), round(2.5))  # 0 2 2
print(round(2.675, 2))                       # 2.67
```

The second result surprises people: `2.675` is stored as slightly *less* than 2.675, so it rounds down. If you need "round half up" decimal behaviour, use `Decimal` with an explicit rounding mode. For whole-number rounding in a fixed direction use `math.floor()` and `math.ceil()`.

## Bitwise operators

Integers are also bit patterns. Bitwise operators act on each bit of the two's-complement representation.

| Operator | Meaning | Example |
| --- | --- | --- |
| `a & b` | AND | `5 & 3` is `1` |
| `a | b` | OR | `5 | 3` is `7` |
| `a ^ b` | XOR (exactly one) | `5 ^ 3` is `6` |
| `~a` | NOT (`-a - 1`) | `~5` is `-6` |
| `a << n` | shift left (× 2**n) | `1 << 3` is `8` |
| `a >> n` | shift right (// 2**n) | `16 >> 2` is `4` |

Typical uses are flags and permissions (`mode & READ`), compact sets of options, and low-level protocols.

## The `math` module

`math` collects the common numeric helpers: `sqrt`, `isqrt` (exact integer square root), `floor`, `ceil`, `gcd`, `pow`, `log`, `sin`/`cos`, `pi`, `inf`, `isclose`, `isnan`. The built-ins `abs`, `round`, `min`, `max`, `sum`, `pow`, and `divmod` need no import. For statistics, see the `statistics` module; for arrays of numbers at scale, third-party NumPy.

!!! tip "Pick the right number type"
    Counting things → `int`. Measuring things (physics, averages) → `float`, compared with `isclose`. Money or exact decimal rules → `Decimal` or integer cents.
