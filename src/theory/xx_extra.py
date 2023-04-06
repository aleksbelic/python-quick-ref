a, b, c = 1, 2, 3

if 3 > 6:
    pass  # do nothing

print('Hello' * 3)
# HelloHelloHello

for num in range(1, 3):  # upper limit is not included
    print(num)
'''
1
2
'''

# F-STRINGS (Formatted string literals, since Python 3.6.)
a = 1
b = 2
print(f'Sum of {a} and {b} is {a + b}')  # Sum of 1 and 2 is 3

# RAISE
# raise TODO


# OBJECT ID
l1 = [1, 2, 3]
l2 = l1  # by reference, no copy
print(id(l1) == id(l2))  # True
l3 = l2.copy()  # copy, no reference
print(id(l2) == id(l3))  # False

quit()  # stop program execution
