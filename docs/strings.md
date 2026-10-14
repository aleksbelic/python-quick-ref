# Strings

Strings hold text. Quote them with single, double, or triple quotes. Single and double quotes are equivalent. Triple quotes span multiple lines.

```python
str1 = 'this string is using single quotes'
str2 = "this string is using double quotes"

str3 = '''
this
can also be
a multi-line
string when attached to a
variable.
'''
```

## Indexing, slicing and length

Index from `0` with `[]`; negative indexes count from the end. A slice `[start:stop:step]` excludes `stop`. `len()` returns the character count.

```python
s = 'abcdef'
print(s[1])     # b
print(s[-1])    # f
print(len(s))   # 6

print(s[1:4])   # bcd
print(s[:2])    # ab
print(s[::2])   # ace
print(s[::-1])  # fedcba, reversed
```

## Concatenation and repetition

Join with `+`, repeat with `*`, or pass multiple values to `print()` separated by commas (joined with spaces).

```python
str1 = 'Here\'s'
str2 = 'Johnny'
print(str1 + ' ' + str2)  # Here's Johnny

print('This', 'can', 'be', 'a', 'sentence')  # This can be a sentence

print('Hello' * 3)  # HelloHelloHello
```

## Searching strings

`split()`, `find()`, `count()`, `startswith()`, and `in` locate or break apart text.

```python
print('a-b-c'.split('-')) # ['a', 'b', 'c']

print('abc'.find('c'))                 # 2
print('abc'.find('C'))                 # -1, not found
print('banana'.count('an'))            # 2

print('word' in 'This is a word')      # True
print('report.csv'.endswith('.csv'))   # True
print('report.csv'.startswith('rep'))  # True
```

## Transforming strings

Methods like `upper()`, `strip()`, and `replace()` return a new string.

```python
print('abc'.capitalize())         # Abc
print('abc'.upper())              # ABC
print('ABC'.lower())              # abc
print('abc'.replace('b', 'X'))    # aXc
print('  padded  '.strip())       # padded
print('-'.join(['a', 'b', 'c']))  # a-b-c
```

## Checking content

```python
print('123'.isdigit())     # True
print('abc'.isalpha())     # True
print('abc123'.isalnum())  # True
print('   '.isspace())     # True
```

## Escapes and raw strings

A backslash starts an escape sequence such as `\n` (newline) or `\t` (tab). Common ones: `\\` backslash, `\'` and `\"` quotes, `\n` newline, `\r` carriage return, `\t` tab, `\b` backspace, `\xhh` and `\uhhhh` Unicode by code point. A raw string (`r'...'`) keeps backslashes as they are — handy for Windows paths and [regular expressions](regexp.md).

```python
print('line1\nline2')   # two lines
print('It\'s')          # It's
print('backslash: \\')  # backslash: \
print(r'C:\new\table')  # C:\new\table
```

## Immutability

Strings cannot be changed in place — every change creates a new object.

```python
x = 'abc'
print(x[1])  # b

try:
    x[1] = 'w'
except TypeError as error:
    print(error)  # 'str' object does not support item assignment
```

!!! tip "Build a new string instead"
    To "edit" a string, build a new one with slicing, `replace()`, or `'+'.join(...)`. For building a string in a loop, collect the pieces in a list and `join()` them once.

!!! tip "Formatting values into text"
    Use [f-strings](formatting.md) rather than concatenation when mixing text and values.
