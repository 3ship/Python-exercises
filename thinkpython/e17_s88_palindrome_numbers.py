"""Print all numbers in the six-digit range that form a palindrome.
This is a simplified version of the exercise 9.8, to keep the output shorter
With additional string-slicing we could print all numbers where four or five
of its digits form a palindrome. Example:
str(number)[1:5] == str(number)[-1:-5:-1]
"""

for number in range(100000,1000000):
    if str(number) == str(number)[::-1]:
        print(number)