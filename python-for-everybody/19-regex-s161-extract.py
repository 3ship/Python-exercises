'''p. 161 - Übung 2 - Zahlen extrahieren
Es soll ein Programm geschrieben werden, das nach Zeilen der folgenden
Form sucht:
New Revision: 39772
Die Zahl soll aus jeder der Zeilen mit einem regulären Ausdruck und der Methode
findall() extrahiert werden. Es soll dann der Durchschnitt der Zahlen berechnet
und als Ganzzahl ausgegeben werden.'''

import re

def extract(input):
    fname = open(input)
    results = list()
    for line in fname:
        line = line.rstrip()
        line = re.findall('New Revision: ([0-9]+)', line)
        if len(line) > 0:
            results.append(int(line[0]))
    average = sum(results) / len(results)
    return int(average)
    
if __name__=='__main__':
    inputfile = 'mbox.txt'
    print(extract(inputfile))