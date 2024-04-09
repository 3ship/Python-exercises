# Return True, if the word entered by the user contains any of the forbidden
# letters.

def avoids(word, verboten):
    for letter in verboten:
        if letter in word:
            return False
    return True

if __name__=='__main__':
    w = input('Enter a word: ')
    v = input('Enter a string of forbidden letters: ')
    print(avoids(w, v))