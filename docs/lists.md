# Lists

Ordered, changeable collections using `[]`. Allow duplicates and mixed data types.

## Creating and accessing

Index from `0` (negative indexes count from the end), use `len()` for the size.

```python
fruits = ['apple', 'banana', 'orange',
          'banana', 'orange']  # can have duplicates
print(fruits)
print(fruits[2])  # orange
print(fruits[-1])  # orange
print(len(fruits))  # 5

mix = ['apple', 1, 'orange', 234]  # can have diff data types
print(mix)  # ['apple', 1, 'orange', 234]
```

## Slicing

`[start:stop:step]` returns a new list; `stop` is excluded.

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])  # [1, 2, 3]
print(nums[:2])  # [0, 1]
print(nums[-2:])  # [4, 5]
print(nums[::2])  # [0, 2, 4]
print(nums[::-1])  # [5, 4, 3, 2, 1, 0]
```

## Adding items

`append()` adds one element to the end, `insert()` adds at an index, `extend()` adds all elements of another iterable.

```python
my_list = ['a', 'b', 'c', 'd', 'e']
my_list.append('f')
print(my_list)  # ['a', 'b', 'c', 'd', 'e', 'f']

my_list.insert(0, 'z')
print(my_list)  # ['z', 'a', 'b', 'c', 'd', 'e', 'f']

my_list.extend(['x', 'y'])
print(my_list)  # ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'x', 'y']
```

## Removing items

`remove()` deletes by value, `pop()` and `del` delete by index.

```python
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

my_list.remove('c')  # removes the first matching element
print(my_list)  # ['a', 'b', 'd', 'e', 'f']

my_list.pop(3)  # removes the element at index 3 (which is 'e')
print(my_list)  # ['a', 'b', 'd', 'f']

del my_list[1]  # removes the element at index 1 (which is 'b')
print(my_list)  # ['a', 'd', 'f']
```

!!! tip "pop vs del"
    `pop()` returns the removed element (and defaults to the last one); `del` removes by index or slice and returns nothing.

## Searching and counting

```python
letters = ['a', 'b', 'c', 'b']
print('b' in letters)  # True
print(letters.index('b'))  # 1, first position
print(letters.count('b'))  # 2

nums = [3, 1, 2]
print(min(nums), max(nums), sum(nums))  # 1 3 6
```

## Sorting and reversing

`sorted()` returns a new list; `.sort()` sorts in place and returns `None`. Both accept `key` and `reverse`.

```python
nums = [3, 1, 2]
print(sorted(nums))  # [1, 2, 3]
print(sorted(nums, reverse=True))  # [3, 2, 1]

words = ['pear', 'fig', 'banana']
print(sorted(words, key=len))  # ['fig', 'pear', 'banana']

nums.sort()
print(nums)  # [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
```

!!! warning "Gotcha: `.sort()` returns `None`"
    `nums = nums.sort()` leaves `nums` as `None`. Use `sorted(nums)` when you want the sorted list as a value.

## Unpacking

Assign list items to names; `*` collects the rest.

```python
first, second, *rest = [1, 2, 3, 4, 5]
print(first, second, rest)  # 1 2 [3, 4, 5]
```

## References and copies

Assignment binds a second name to the same list; it does not copy it. Use `.copy()` (or a slice `[:]`) for an independent list.

```python
original = ['a', 'd', 'f']
alias = original  # same list, two names
del alias[0]
print(alias)  # ['d', 'f']
print(original)  # ['d', 'f']

l1 = [1, 2, 3]
l2 = l1.copy()  # independent copy
l1.pop()
print(l1)  # [1, 2]
print(l2)  # [1, 2, 3]
```

!!! warning "Gotcha: `.copy()` is shallow"
    A shallow copy shares nested lists. Use `copy.deepcopy()` for lists of lists. See [Mutable vs Immutable](mutable-immutable.md).

## Identity vs equality

`==` compares content, `is` compares object identity.

```python
l1 = [1, 2, 3]
l2 = l1  # by reference: when l1 changes - l2 also changes
l3 = l2.copy()  # copy: when l3 changes - l2 does not change
print(l1 == l2)  # True, same content
print(l1 is l2)  # True, same object
print(l2 == l3)  # True, same content
print(l2 is l3)  # False, different objects
```

!!! warning "Gotcha: repeating a list of lists"
    `*` repeats *references*, so `[[0] * 3] * 3` is three names for one inner list.

    ```python
    grid = [[0] * 3] * 3
    grid[0][0] = 1
    print(grid)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

    grid = [[0] * 3 for _ in range(3)]  # three separate rows
    ```

## How lists work

A list is a dynamic array of references. Indexing and `append()` are fast; inserting or removing near the front, and searching with `in`, must walk the list. See [Complexity](complexity.md).

## Joining items

`join()` concatenates string elements with a separator.

```python
my_list = ['a', 'b', 'c']
print('-'.join(my_list))  # a-b-c
```

!!! tip "Building lists"
    To build a list from another one, see [Comprehensions](comprehensions.md).
