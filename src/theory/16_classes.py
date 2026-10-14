class Point1():
    x = 5
    y = 10


p1 = Point1()
print(p1.x)  # 5


class Point2():
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y


p2 = Point2(7, 11)
print(p2.y)  # 11


print(p1.__class__)
# <class '__main__.Point1'>

print(type(p1))
# <class '__main__.Point1'>

print(type(p1).__name__)
# Point1

print(p1.__class__.__name__)
# Point1