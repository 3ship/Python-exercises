'''p. 161 - Übung 1 - grep -c
Schreibe ein Programm, das der Funktion von grep -c unter Unix entspricht
Der Benutzer soll aufgefordert werden, einen regulären Ausdruck einzugeben,
mit dem dann die Anzahl der Zeilen gezählt werden, die mit dem regulären
Ausdruck übereinstimmen'''

import re

def grepc(file, keyword):
    fname = open(file)
    counter = 0
    for line in fname:
        line = line.rstrip()
        line = re.findall(keyword, line)
        if len(line) > 0:
            counter += 1
    return counter

if __name__=='__main__':
    query = input('Gib eine RegEx an: ')
    result = grepc('mbox.txt', query)
    print(f'Datei mbox.txt enthält {result} Ergebnisse für {query}')