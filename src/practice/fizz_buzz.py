'''
Players take turns to count incrementally, replacing any number divisible by three with the word "fizz",
and any number divisible by five with the word "buzz", and any number divisible by both 3 and 5 with
the word "fizzbuzz".
https: // en.wikipedia.org/wiki/Fizz_buzz

'''

for num in range(1, 31):
    if num % 15 == 0:
        print(num, 'fizzbuzz')
    elif num % 5 == 0:
        print(num, 'buzz')
    elif num % 3 == 0:
        print(num, 'fizz')
