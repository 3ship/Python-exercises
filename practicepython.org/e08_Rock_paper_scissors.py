# Make a two-player Rock-Paper-Scissors game. 

def game():
    player1 = input("Player 1! Rock, paper or scissors? ")
    while player1 != "rock" and player1 != "paper" and player1 != "scissors":
        player1 = input("Choose rock, paper or scissors: ")
    player2 = input("Player 2! Rock, paper or scissors? ")
    while player2 != "rock" and player2 != "paper" and player2 != "scissors":
        player2 = input("Choose rock, paper or scissors: ")

    if player1 != player2:
        if player1 == "rock":
            if player2 == "scissors" : print("Player 1 won!")
            else : print("Player 2 won!")
        elif player1 == "scissors":
            if player2 == "paper" : print("Player 1 won!")
            else : print("Player 2 won!")
        elif player1 == "paper":
            if player2 == "rock" : print("Player 1 won!")
            else : print("Player 2 won!")
    else:
        print("It's a draw!")
        
    loop = input("Play again? ")
    match loop:
        case 'Yes' | 'yes' | 'y':
            game()
        
game()