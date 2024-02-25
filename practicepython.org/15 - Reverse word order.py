def split(sample):
    result = sample.split()
    reverse(result)

def reverse(liste):
    liste2 = liste[::-1]
    print(' '.join(liste2))
    
query = input('Schreibe einen vollständigen Satz: ')
split(query)