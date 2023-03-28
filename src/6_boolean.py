print(1 > 2)  # False
print(1 == 2)  # False
print(1 < 2)  # True

# bool()
print(bool('Hello'))  # True
print(bool(4))  # True
print(bool(''))  # False
print(bool(0))  # False

# bool() of List, Tuple or Set is always True except it's empty
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

print(bool(None))  # False
print(bool(False))  # False
