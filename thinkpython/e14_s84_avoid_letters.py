# Return True, if the word entered by the user contains any of the forbidden
# letters.

def avoids(word, verboten):
    forbidden_letters = 0
    for letter in verboten:
        if letter in word:
            forbidden_letters += 1
        else:
            continue
    if forbidden_letters > 0:
        return False
    else:
        return True

if __name__=='__main__':
    w = input('Enter a word: ')
    v = input('Enter a string of forbidden letters: ')
    print(avoids(w, v))