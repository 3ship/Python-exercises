'''Beispiel - p.97 - Über Dateizeilen mit find iterieren

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 or line.find('Author') == -1: continue
    print(line)'''

# find loop mit input:

finput = input('Gib eine Datei an: ')
fhand = open(finput)
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 or line.find('Author') == -1: continue
    print(line)