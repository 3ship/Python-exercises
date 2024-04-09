# Return True, if the entered word only uses letters from the entered string
# of letters.

def uses_only(word, letters):
    uses_letters = True
    for letter in letters:
        if letter not in word:
            uses_letters = False
        else:
            continue
    if uses_letters == True:
        return True
    else:
        return False

if __name__=='__main__':
    w = input('Enter a word: ')
    l = input('Enter a string of letters: ')
    print(uses_only(w, l))