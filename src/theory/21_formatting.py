# f-string (Python 3.6+)
print(f"{3/2:.2f}") # 1.50
print(f"{3/2:.3f}") # 1.500

# format()
name = 'Alice'
age = 30
print('My name is {} and I am {} years old.'.format(name, age))
# My name is Alice and I am 30 years old.

print('My name is {1} and I am {0} years old.'.format(age, name))
# My name is Alice and I am 30 years old.
