# Conditions

Branch execution with `if`, `elif`, and `else` based on a boolean expression.

## If / elif / else

Only the first branch whose condition is true runs. `else` catches everything else.

```python
if 1 > 2:
    print('1 is greater than 2')
elif 1 == 2:
    print('1 equals 2')
else:
    print('1 is less than 2')
```

!!! tip "Indentation matters"
    Branches are defined by indentation, not braces. Keep each block at a consistent indent level.

## Indentation rules

Indent 4 spaces after a colon to open a block, dedent to close it. Be consistent — mixing tabs and spaces raises an error.

```python
if True:
    print('indented block runs')  # 4 spaces
print('dedented, always runs')
```
