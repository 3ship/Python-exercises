import random

# Length of the list doesn't matter, because user doesn't see the full list.
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

# This would be more concise with random.sample