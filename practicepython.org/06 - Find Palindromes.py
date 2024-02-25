#Ask the user for a string and print out whether this string is a palindrome or not

word = input("Give me a word! ")
drow = word[::-1]
if drow.upper() == word.upper() : print(word + " IS a palindrome!")
else : print(word + " is NOT a palindrome!")