"""Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. If the number is a multiple of
4, print out a different message."""

def question():
    query = int(input("Give me a number, and I'll check, if it's even or odd: "))

    if query % 4 == 0:
        print("Even and divisible by 4")
    elif query % 2 == 0:
        print("Even")
    else:
        print("Odd")
    question()
    
question()

"""Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that to
the user. If not, print a different appropriate message."""

start = input("Odd/Even [1] or Division [2] ? ")

if start == "1":
    query = int(input("Give me a number, and I'll check, if it's even or odd: "))
    if query % 4 == 0:
        print("Even and divisible by 4")
    elif query % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif start == "2":
    num = int(input("Give me a number to divide: "))
    check = int(input("Give me a number to divide by: "))
    result = num / check
    if result % 1 == 0:
        print("Whole number")
    else:
        print("Not a whole number")
