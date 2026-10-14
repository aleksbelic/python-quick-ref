# While Loop

Repeats a block as long as a condition is `True`. Use it when you don't know the number of iterations upfront.

## Basic while loop

Increment a counter each iteration. `break` exits the loop, `continue` skips to the next iteration.

```python
i = 1
while i <= 100:
    if i > 10:
        break
    if i == 6:
        i += 1
        continue
    if i % 2 == 0:
        print(i)
    i += 1
```

## While-else

The `else` block runs when the loop finishes normally — i.e. the condition becomes `False` without hitting `break`.

```python
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('x is no longer less than 3')
```

!!! tip "Avoid infinite loops"
    Always update the loop variable inside the body. If the condition never becomes `False` and there is no `break`, the loop runs forever.
