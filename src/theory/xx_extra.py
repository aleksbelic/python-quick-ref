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
x = 1
y = 2
print(f'Sum of {x} and {y} is {x + y}')  # Sum of 1 and 2 is 3

# RAISE
# raise TODO


# OBJECT ID
l1 = [1, 2, 3]
l2 = l1  # by reference, no copy
print(id(l1) == id(l2))  # True
l3 = l2.copy()  # copy, no reference
print(id(l2) == id(l3))  # False

import sys

sys.exit(0)  # stop program execution (quit() is REPL-only, use sys.exit() in scripts)
