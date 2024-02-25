"""Write a password generator in Python."""

from random import choice as rc
import string

letterSample = string.printable[0:-6]
print(letterSample)
letterSample = letterSample.replace("\\", "")
letterSample = letterSample.replace("\"", "")
letterSample = letterSample.replace("`", "")
letterSample = letterSample.replace("'", "")

def generator(n):
    password = []
    while len(password) < n:
        password.append(rc(letterSample))
    password = "".join(password)
    print(password)

query = int(input("How many digits should your password have? "))
generator(query)

print(letterSample)