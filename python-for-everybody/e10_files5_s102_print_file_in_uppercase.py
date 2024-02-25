'''
p. 102
Schreiben Sie ein Programm, das eine Datei einliest und den
Inhalt der Datei (Zeile für Zeile) in Großbuchstaben ausgibt.
'''

try:
    fhandle = input('Datei: ')
    fname = open(fhandle)
except:
    print('Existiert nicht.')
    exit()
for line in fname:
    line = line.upper()
    print(line.strip())