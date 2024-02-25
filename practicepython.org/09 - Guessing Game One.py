import random
counter = 1
win = 0

def game():
    global win
    rando = random.randint(1,10)
    user = int(input("Give me a number from 1 to 9: "))

    if rando > user:
        print("Your number was too low. The correct number was " + str(rando))
        loop()
    elif rando < user:
        print("Your number was too high. The correct number was " + str(rando))
        loop()
    else:
        print("You guessed correctly!")
        win += 1
        loop()
    
def loop():
    global counter
    inp = input("\nPress enter to play again. Type 'exit' and press enter to quit. ")
    if inp == "exit":
        print("You played", counter, "time(s). And won", win, "of them!")
    else:
        counter += 1
        game()

game()