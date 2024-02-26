"""Write a function called eval_loop that iteratively prompts the user, takes
the resulting input and evaluates it using eval, and prints the result."""

import math

def eval_loop():
    while True:
        query = input("> ")
        if query == "done":
            break
        print(eval(query))

if __name__=='__main__':
    print("Enter a Python expression: ")
    eval_loop()