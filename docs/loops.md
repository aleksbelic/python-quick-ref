# Loops

Repeat a block of code. Use `for` to iterate over a known sequence and `while` to repeat until a condition changes.

## For loop

Iterates over any iterable object — strings, lists, tuples, sets, dictionaries, or `range()`.

```python
for x in 'abc':
    print(x)  # a, b, c

friends = ['Lucky', 'Joey', 'Chandler']
for f in friends:
    print('Hi', f)
```

## range()

`range(stop)`, `range(start, stop)` and `range(start, stop, step)` count up to — but not including — `stop`.

```python
for num in range(3):
    print(num)  # 0, 1, 2

for num in range(1, 3):  # upper limit is not included
    print(num)  # 1, 2

for num in range(10, 0, -3):
    print(num)  # 10, 7, 4, 1
```

## enumerate() and zip()

`enumerate()` gives you the index as well. `zip()` walks several iterables in parallel and stops at the shortest.

```python
names = ['Ana', 'Ben', 'Cleo']

for index, name in enumerate(names, start=1):
    print(index, name)  # 1 Ana, 2 Ben, 3 Cleo

ages = [30, 22, 28]
for name, age in zip(names, ages):
    print(f'{name} is {age}')
```

!!! tip "Don't use `range(len(x))`"
    `for i in range(len(items))` is almost always better written as `for item in items` or `for i, item in enumerate(items)`.

## While loop

Repeats a block as long as a condition is `True`. Use it when you don't know the number of iterations upfront.

```python
i = 1
while i <= 100:
    if i > 10:
        break
    if i == 6:
        i += 1
        continue
    if i % 2 == 0:
        print(i)  # 2, 4, 8, 10
    i += 1
```

`break` exits the loop, `continue` skips to the next iteration.

## Loop until valid

A `while True` loop with `break` is the standard way to retry until something works.

```python
attempts = ['abc', '', '42']  # pretend these come from input()
for text in attempts:
    if text.isdigit():
        print('Got a number:', text)
        break
    print('Not a number, try again')
```

## Loop-else

The `else` block of a `for` or `while` runs when the loop finishes *without* hitting `break`.

```python
for x in 'abc':
    print(x)
else:
    print('finished!')

x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('x is no longer less than 3')

for n in [1, 2, 3]:
    if n == 5:
        break
else:
    print('5 not found')  # typical use: search loops
```

!!! tip "for vs while"
    Prefer `for` when iterating a known sequence. Use `while` when looping until a condition changes.

!!! warning "Gotcha: infinite loops and mutating while iterating"
    Always update the loop variable inside a `while` body. And don't add or remove items of a list while you loop over it — iterate over a copy (`for x in items[:]`) or build a new list with a [comprehension](comprehensions.md).
