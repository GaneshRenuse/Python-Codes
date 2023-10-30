import random


def my_random(d):
    return random.randrange(10**(d-1), 10**d)


print(my_random(6))
