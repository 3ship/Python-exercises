from random import choice as rc

charSample = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+,-./:;<=>?@^_~"

def generator(n):
    password = []
    while len(password) < n:
        password.append(rc(charSample))
    password = "".join(password)
    print(password)

query = int(input("How many digits should your password have? "))
generator(query)