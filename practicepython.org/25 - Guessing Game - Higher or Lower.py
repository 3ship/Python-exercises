import random

start_game = input("Choose a number between 0 and 100. "
                    "If you're ready, press Enter.")

low = 1
high = 99
counter = 0

def guesser(low, high):
    global counter
    guess = random.randint(low, high)
    query = input("Is your number higher [1], lower [2] or equal [3] to "
                    + str(guess) + "? ")
    if query == "1":
        low = guess + 1
        counter += 1
        guesser(low, high)
    elif query == "2":
        high = guess - 1
        counter += 1
        guesser(low, high)
    else:
        counter += 1
        if counter == 1:
            print("I guessed correctly! It only took me one attempt!" )
        else:
            print("I guessed correctly! It only took me", str(counter), "attempts!" )
    
guesser(low, high)