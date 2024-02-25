"""Create a program that asks the user for a number and then prints out a list
of all the divisors of that number."""

# Original:

choose = int(input("Pick a number: "))
div_list = []

for x in range(1, choose):
    divisor = choose / x
    if divisor % 1 == 0 and divisor != choose:
        div_list.append(int(divisor))
print(str(choose) + " can be divided by the following numbers: " + str(div_list) + " ... and of course by itself and 1.")


# Alternative:

choose = int(input("Pick a number: "))
div_list = []

for x in range(2,choose-1):
    if choose % x == 0:
        div_list.append(int(x))
print(str(choose) + " can be divided by the following numbers: " + str(div_list) + " ... and of course by itself and 1.")