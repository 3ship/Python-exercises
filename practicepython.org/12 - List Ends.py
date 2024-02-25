"""Write a program that takes a list of numbers and makes a new list of
only the first and last elements of the given list. For practice, write
this code inside a function."""

import random

query = int(input("How many random numbers? "))

def start(inp):
    # Get a list of ten random numbers:
    numberlist = []
    for i in range(inp):
        num = random.randint(0,100)
        # We don't want duplicates
        while num not in numberlist:
            numberlist.append(num)
    print(numberlist[0], "and", numberlist[-1])

start(query)