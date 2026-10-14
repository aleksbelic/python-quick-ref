# Input & Output

Talk to the user with `print()` and `input()`. `input()` always returns a string.

## Reading input

Pass a prompt string. What the user types is returned as a string.

```python
name = input('My name is: ')
print('Hello ' + name)
```

!!! tip "input returns str"
    `input()` always returns a string. Convert with `int()` or `float()` when you need a number, e.g. `age = int(input('Age: '))`.

## Validating input

Wrap the conversion in a loop so a typo asks again instead of crashing the program.

```python
while True:
    text = input('Age: ')
    try:
        age = int(text)
    except ValueError:
        print('Please enter a whole number')
        continue
    if age < 0:
        print('Age cannot be negative')
        continue
    break

print(f'You are {age}')
```

## print() options

`print()` accepts several values and a few keyword arguments.

```python
print('a', 'b', 'c')  # a b c
print('a', 'b', 'c', sep='-')  # a-b-c
print('no newline', end='')
print(' ...continued on the same line')
```

## Printing to stderr

Send diagnostics to the error stream so they don't mix with normal output (which may be piped to another program).

```python
import sys

print('Something looks off', file=sys.stderr)
```

## Command-line arguments

For input that comes from the command line rather than the keyboard, see [Scripts & CLI](scripts.md).
