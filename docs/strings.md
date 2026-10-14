# Strings

Strings hold text. Quote them with single, double, or triple quotes.

## Creating strings

Single and double quotes are equivalent. Triple quotes span multiple lines.

```python
s1 = 'this string is using single quotes'
s2 = "this string is using double quotes"

s3 = '''
this
can also be
a multi-line
string when attached to a
variable.
'''
print(s3)
```

## Indexing and length

Index from `0` with `[]`; `len()` returns the character count.

```python
s4 = 'abc'
print(s4[1])  # 'b
print(len(s4))  # 3
```

## Concatenation

Join with `+`, or pass multiple values to `print()` separated by commas (joined with spaces).

```python
# concat using plus sign:
str1 = 'Here\'s'
str2 = 'Johnny'
print(str1 + ' ' + str2)
# Here's Johnny

# concat with comma:
print('This', 'can', 'be', 'a', 'sentence')
# This can be a sentence
```

## Searching strings

`split()`, `find()`, and `in` locate or break apart text.

```python
# split
print('a-b-c'.split('-'))
# ['a', 'b', 'c']

# find
print('abc'.find('c'))  # 2
print('abc'.find('C'))  # -1

# in
print('word' in 'This is a word')  # True
```

## Transforming strings

Methods like `capitalize()`, `upper()`, and `replace()` return a new string.

```python
# capitalize
print('abc'.capitalize())  # 'Abc'

# upper
print('abc'.upper())  # 'ABC'

# replace
print('abc'.replace('b', 'X'))  # 'aXc'
```

## Immutability

Strings cannot be changed in place — every change creates a new object.

```python
# Strings are immutable = whenever we change them - we end up with new object in memory
x = 'abc'
print(x[1])  # 'b'
x[1] = 'w'  # TypeError: 'str' object does not support item assignment
```

!!! tip "Build a new string instead"
    To "edit" a string, build a new one with slicing, `replace()`, or `'+'.join(...)`.
