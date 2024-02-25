"""Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order."""

def split(sample):
    result = sample.split()
    reverse(result)

def reverse(liste):
    liste2 = liste[::-1]
    print(' '.join(liste2))
    
query = input('Schreibe einen vollständigen Satz: ')
split(query)