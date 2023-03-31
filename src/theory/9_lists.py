'''
Lists:
- changable
- allow duplicates
- use []
- can contain diff data types
'''

fruits = ['apple', 'banana', 'orange',
          'banana', 'orange']  # can have duplicates
print(fruits)
print(fruits[2])  # orange
print(len(fruits))  # 5

mix = ['apple', 1, 'orange', 234]  # can have diff data types
print(mix)  # ['apple', 1, 'orange', 234]

# APPEND

my_list = ['a', 'b', 'c', 'd', 'e']
my_list.append('f')
print(my_list)  # ['a', 'b', 'c', 'd', 'e', 'f']

# REMOVE

my_list.remove('c')  # removes the first matching element from the list
print(my_list)  # ['a', 'b', 'd', 'e', 'f']

# POP

my_list.pop(3)  # removes the element at index 3 (which is 'e') from the list
print(my_list)  # ['a', 'b', 'd', 'f']

# DEL (same as POP)

del my_list[1]  # removes the element at index 1 (which is 'b') from the list
print(my_list)  # ['a', 'd', 'f']

# PASS BY REF

my_list2 = my_list  # pass by reference, because it is not a basic data type
del my_list2[0]
print(my_list2)  # ['d', 'f']
print(my_list)  # ['d', 'f']

# COPY

l1 = [1, 2, 3]
l2 = l1.copy()  # no reference
l1.pop()
print(l1)  # [1, 2]
print(l2)  # [1, 2, 3]
