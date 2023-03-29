i = 1
while i <= 100:
    if i > 10:
        break
    if i == 6:
        i += 1
        continue
    if i % 2 == 0:
        print(i)
    i += 1

'''
2
4
8
10
'''

# WHILE loop with ELSE:

x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('x is no longer less than 3')

'''
1
2
x is no longer less than 3
'''
