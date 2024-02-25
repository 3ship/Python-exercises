# Recursively, a word is a palindrome if the first and last
# letters are the same and the middle is a palindrome.

def palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palindrome(word[1:-1])