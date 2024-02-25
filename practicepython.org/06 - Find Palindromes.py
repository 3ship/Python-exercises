word = input("Give me a word! ")
drow = word[::-1]
if drow.upper() == word.upper() : print(word + " IS a palindrome!")
else : print(word + " is NOT a palindrome!")