# Beispiel - p.94-96 - Mit .startswith() bestimmte Zeilen zählen

fhand = open('mbox-short.txt')
count = 0
fromcount = 0
for line in fhand:
    count += 1
    line = line.rstrip() # right strip um Zeilenumbrüche zu löschen
    if line.startswith('From: '):
        print(line)
        fromcount += 1
print('\nLine Count:', count)
print('From Count:', fromcount)


fhand = open('mbox-short.txt')
inp = fhand.read()
print('Character count:', len(inp))

'''Alternativ - Schleife mit continue:
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)'''