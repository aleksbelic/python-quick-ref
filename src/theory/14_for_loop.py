# iterates over list, tuple, set, dictionary or string (iterable objects)

for x in 'abc':
    print(x)

'''
a
b
c
'''

friends = ['Lucky', 'Joey', 'Chandler']
for f in friends:
    print('Hi', f)

'''
Hi Lucky
Hi Joey
Hi Chandler
'''

# FOR loop with ELSE:
for x in 'abc':
    print(x)
else:
    print('finished!')

'''
a
b
c
finished!
'''

for num in range(3):
    print(num)

'''
0
1
2
'''