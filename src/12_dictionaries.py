'''
Dictionaries:
- use key/value pairs
- changable
- NO duplicate keys
- use {}, similar to JSON
'''

d1 = {
    'name': 'Hans',
    'age': '32',
    'city': 'Berlin'
}

print(d1)  # {'name': 'Hans', 'age': '32', 'city': 'Berlin'}
print(d1['name'])  # 'Hans'
print(len(d1))  # 3

# looping through dictionary

for key in d1:  # list keys
    print(key)
'''
name
age
city
'''

for key in d1.keys():  # list keys
    print(key)
'''
name
age
city
'''

for key in d1:  # list values
    print(d1[key])
'''
Hans
32
Berlin
'''

for key_val_tuple in d1.items():  # list (key, value) as tuples
    print(key_val_tuple)
'''
('name', 'Hans')
('age', '32')
('city', 'Berlin')
'''

for key, val in d1.items():  # list separated keys and values
    print(key, val)
'''
name Hans
age 32
city Berlin
'''
