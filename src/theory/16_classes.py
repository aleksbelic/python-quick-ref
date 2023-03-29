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
