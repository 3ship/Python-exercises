# Return True, if the entered word only uses letters from the entered string
# of letters.

def uses_only(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

if __name__=='__main__':
    w = input('Enter a word: ')
    l = input('Enter a string of letters: ')
    print(uses_only(w, l))