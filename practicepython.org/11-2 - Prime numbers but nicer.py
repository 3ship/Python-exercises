def start(number, mode):
    if mode == 'quit':
        exit()
    try:
        number = int(number)
    except ValueError:
        repeat_program()
    if mode == 'short':
        print(short_check(number))
        repeat_program()
    if mode == 'long':
        divisors = long_check(number)
        if divisors != []:
            print(number, 'is NOT a prime number!\n')
            show_calcs(divisors)
            repeat_program()
        else:
            print(number, 'IS a prime number!\n')
            repeat_program()

def short_check(num):
    if num & 1 == 0:
        return 'Even numbers can\'t be primes.\n'
    d = 3
    while d * d <= num:
        if num % d == 0:
            return f'{num} is NOT a prime number! It\'s divisible by {d}\n'
        d += 2
    return f'{num} IS a Prime number!\n'

def long_check(num):
    div = []
    for x in range(3, num, 2):
        if num % x == 0:
            div.append(x)
    return div

def show_calcs(div):
    calcs = 'Possible calculations: '
    calclist = []
    head, tail = 0, -1
    while len(calclist) < len(div):
        calcs = calcs + str(div[head]) + ' * ' + str(div[tail]) + ', '
        calclist.append(div[0])
        calclist.append(div[-1])
        head += 1
        tail -= 1
    print(calcs[:-2] + '\n')
    
def repeat_program():
    query1 = input('Enter a whole number: ')
    if query1 == 'quit':
        exit()
    query2 = input('\nChoose \'long\' or \'short\' mode.\nLong mode will show '
                    'all possible calculations if your number is not a prime, '
                    'but it struggles with numbers longer than 9 digits: ')
    start(query1, query2)

if __name__=='__main__':
    print('Check if a number is a prime.\n'
      'Type \'quit\' to exit the program.')
    repeat_program()