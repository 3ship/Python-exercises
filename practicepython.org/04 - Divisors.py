# Original:

choose = int(input("Pick a number: "))
list = []

for x in range(1, choose):
    divider = choose / x
    if divider % 1 == 0 and divider != choose:
        list.append(int(divider))
print(str(choose) + " can be divided by the following numbers: " + str(list) + " ... and of course by itself and 1.")


# Alternative:

choose = int(input("Pick a number: "))
list = []

for x in range(2,choose-1):
    if choose % x == 0:
        list.append(int(x))
print(str(choose) + " can be divided by the following numbers: " + str(list) + " ... and of course by itself and 1.")