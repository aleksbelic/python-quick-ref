# Lists

Ordered, changeable collections using `[]`. Allow duplicates and mixed data types.

## Creating and accessing

Index from `0`, use `len()` for the size.

```python
fruits = ['apple', 'banana', 'orange',
          'banana', 'orange']  # can have duplicates
print(fruits)
print(fruits[2])  # orange
print(len(fruits))  # 5

mix = ['apple', 1, 'orange', 234]  # can have diff data types
print(mix)  # ['apple', 1, 'orange', 234]
```

## Adding items

`append()` adds one element to the end.

```python
my_list = ['a', 'b', 'c', 'd', 'e']
my_list.append('f')
print(my_list)  # ['a', 'b', 'c', 'd', 'e', 'f']
```

## Removing items

`remove()` deletes by value, `pop()` and `del` delete by index.

```python
my_list.remove('c')  # removes the first matching element from the list
print(my_list)  # ['a', 'b', 'd', 'e', 'f']
```

```python
my_list.pop(3)  # removes the element at index 3 (which is 'e') from the list
print(my_list)  # ['a', 'b', 'd', 'f']
```

```python
del my_list[1]  # removes the element at index 1 (which is 'b') from the list
print(my_list)  # ['a', 'd', 'f']
```

!!! tip "pop vs del"
    `pop()` returns the removed element; `del` removes by index or slice and returns nothing.

## References and copies

Assignment copies the reference, not the data. Use `.copy()` for an independent list.

```python
my_list2 = my_list  # pass by reference, because it is not a basic data type
del my_list2[0]
print(my_list2)  # ['d', 'f']
print(my_list)  # ['d', 'f']
```

```python
l1 = [1, 2, 3]
l2 = l1.copy()  # no reference
l1.pop()
print(l1)  # [1, 2]
print(l2)  # [1, 2, 3]
```

## Identity vs equality

`==` compares content, `is` compares object identity.

```python
l1 = [1, 2, 3]
l2 = l1  # by reference: when l1 changes - l2 also changes
l3 = l2.copy()  # copy: when l3 changes - l2 does not change
print(l1 == l2)  # True, same content
print(l1 is l2)  # True, same object
print(id(l1) == id(l2))  # True (same as above)
print(l2 == l3)  # True, same content
print(l2 is l3)  # False, different objects
print(id(l2) == id(l3))  # False (same as above)
```

## Joining items

`join()` concatenates string elements with a separator.

```python
my_list = ['a', 'b', 'c']
print('-'.join(my_list))  # a-b-c
```
