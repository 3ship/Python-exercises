'''def start():
    number = int(input("Give me a whole number: "))
    numberspace = list(range(2,number))
    divisors = []
    for x in numberspace:
        if number % x == 0:
            divisors.append(x)
    if divisors != []:
        print(number, "is NOT a prime number!", number, "can be divided by:", divisors)
        start()
    else:
        print(number, "IS a prime number!")
        start()

start()'''

#### With two functions:

def start():
    number = int(input("Give me a whole number: "))
    numberspace = list(range(3,int(number / 2)))
    divisors = []
    control(number, numberspace, divisors)
    if divisors != []:
        print(number, "is NOT a prime number!", number, "can be divided by:", divisors)
        start()
    else:
        print(number, "IS a prime number!")
        start()
        
def control(num, numspc, div):
    for x in numspc:
        if num % x == 0:
            div.append(x)

start()