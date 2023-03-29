# https://en.wikipedia.org/wiki/Fibonacci_sequence

a, b = 0, 1
print(a)
print(b)
for num in range(1, 10):
    c = a + b
    print(c)
    a = b
    b = c
