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

s4 = 'abc'
print(s4[1])  # 'b
print(len(s4))  # 3

# concat using plus sign:
str1 = 'Here\'s'
str2 = 'Johnny'
print(str1 + ' ' + str2)
# Here's Johnny

# concat with comma:
print('This', 'can', 'be', 'a', 'sentence')
# This can be a sentence

# split
print('a-b-c'.split('-'))
# ['a', 'b', 'c']

# find
print('abc'.find('c'))  # 2
print('abc'.find('C'))  # -1

# in
print('word' in 'This is a word')  # True

# capitalize
print('abc'.capitalize())  # 'Abc'

# upper
print('abc'.upper())  # 'ABC'

# replace
print('abc'.replace('b', 'X'))  # 'aXc'

# Strings are immutable = whenever we change them - we end up with new object in memory
x = 'abc'
print(x[1])  # 'b'
x[1] = 'w'  # TypeError: 'str' object does not support item assignment
