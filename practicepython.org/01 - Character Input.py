name = input("What's your name? ")
age = int(input("How old are you? "))
result = 2023 - age + 100

print(f"Hey, {name}! You will turn 100 in the year {result}!")

#Extended:

name = input("What's your name? ")
age = int(input("How old are you? "))
number = int(input("Give me a number from 1 to 10: "))
result = 2023 - age + 100

if number > 10 or number < 1:
    print("Number was not in the range from 1 to 10! Try again!")
else:
    while number > 0:
        print(f"Hey, {name}! You will turn 100 in the year {result}!")
        number -= 1