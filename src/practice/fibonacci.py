# https://en.wikipedia.org/wiki/Fibonacci_sequence

a, b = 0, 1
print(a)
print(b)
for num in range(1, 10):
    c = a + b
    print(c)
    a = b
    b = c


def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        i = 2
        while True:
            c = a + b
            i += 1
            if i == n:
                return c
            else:
                a = b
                b = c


print(nth_fib(10))  # 34
