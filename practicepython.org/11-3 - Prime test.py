def primeChecker(n):
    if n & 1 == 0:
        return 'Even numbers can\'t be primes.'
    d = 3
    test = []
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return 'Prime'

print(primeChecker(2683564477777))