import random


# d is the no of digits, or let's say length of the generated number.
def my_random(d):
    return random.randrange(10**(d-1), 10**d)


# print to test the output
print(my_random(6))
