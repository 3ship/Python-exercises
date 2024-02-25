from random import choice as rc
import string

alphanumSample = string.ascii_letters + string.digits
puncSample = string.punctuation[0:-12]
puncSample = puncSample.replace("'", "")

print("Welcome to the Simple Python Password Generator!\n")

def start():
    length = int(input("How many digits do you want your password to have? "))
    characters(length)

def repeat():
    rep = input("Do you want to generate another password? (y/n): ")
    if rep == "n":
        print("Goodbye!")
        exit()
    elif rep == "y":
        start()
    else:
        repeat()

def characters(l):
    charType = int(input("Choose the format: With special characters [1]."
                         " Only letters and numbers [2]: "))
    if charType != 1 and charType != 2:
        characters(l)
    else:
        generator(l, charType)

def generator(l, c):
    password = ""
    if c == 1:
        charSample = alphanumSample + puncSample
    else:
        charSample = alphanumSample
    while len(password) < l:
        password += rc(charSample)
    if c == 1:
        for x in password:
            if x in puncSample:
                checkpoint = True
                break
            else:
                checkpoint = False
        if checkpoint == True:
            print("Generated password:", password, "\n")
        else:
            generator(l, c)
    else:
        print("Generated password:", password, "\n")
    repeat()

start()