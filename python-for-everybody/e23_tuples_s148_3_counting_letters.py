'''Schreiben Sie ein Programm, das eine Datei liest und die Buchstaben
in absteigender Reihenfolge der Häufigkeit ausgibt. Das Programm sollte alle
Eingaben in Kleinbuchstaben umwandeln und nur die Buchstaben a-z zählen. Es
soll keine Leerzeichen, Ziffern, Interpunktionszeichen oder irgendetwas anderes als
die Buchstaben a-z zählen.'''

import string

# Remove non-letter characters from the input, count letters in a dict()
# and transform the dict() into a list of tuples for sorting:

def count_letters(d):
    letter_counter = dict()
    for line in d:
        line = line.lower()
        line = line.translate(str.maketrans('', '', 
                                    string.punctuation + 
                                    string.digits + 
                                    string.whitespace))
        for letter in line:
            if letter not in letter_counter:
                letter_counter[letter] = 1
            else:
                letter_counter[letter] += 1
    letter_counter = list(letter_counter.items())
    return sort_letters(letter_counter)

# Sort the letters by letter count (descending):

def sort_letters(l):
    sorted_letters = list()
    for letters, count in l:
        sorted_letters.append((count, letters))
    sorted_letters.sort(reverse=True)
    return(sorted_letters)

if __name__=='__main__':
    query = input('Choose a file: ')
    test = count_letters(open(query, 'r'))
    for count, letter in test:
        print(f'{letter}: {str(count)}')