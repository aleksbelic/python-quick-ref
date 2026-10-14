# Input

Read user input from the terminal with `input()`. It always returns a string.

## Reading input

Pass a prompt string. What the user types is returned as a string.

```python
name = input('My name is: ')
```

## Using the result

Combine or convert the string as needed.

```python
print('Hello ' + name)
```

!!! tip "input returns str"
    `input()` always returns a string. Convert with `int()` or `float()` when you need a number, e.g. `age = int(input('Age: '))`.
