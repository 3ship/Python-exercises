import random

randomNumber1 = random.randrange(1, 100)
randomNumber2 = random.randrange(1, 100)

multiRand = randomNumber1 * randomNumber2

result = "The random number is {}"
result2 = "The rather small number is {}"

if multiRand > 5000:
	print(result.format(multiRand))
elif multiRand > 2000:
	print(result2.format(multiRand))
else:
	print("The number was smaller than 2000!")


x = 18 % 12

print(x)