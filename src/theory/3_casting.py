x = str(123)  # 123 -> '123'

y = '78'
# print (1 + y) # ERROR
print(1 + int(y))  # 79

z = 3.456
print(int(z))  # 3

my_num = 2
print(float(my_num))  # 2.0

my_bool = "True"
print(type(my_bool))  # <class 'str'>
print(type(bool(my_bool)))  # <class 'bool'>
