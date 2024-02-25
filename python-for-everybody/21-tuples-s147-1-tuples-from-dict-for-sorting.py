'''Das vorherige Programm (16) soll auf folgende Weise überarbeitet werden:
Die From-Zeilen sollen gelesen und geparst werden, um daraus die Adressen zu
extrahieren. Dabei soll mit Hilfe eines Dictionarys die Anzahl der Nachrichten
von jeder Person gezählt werden.
Nachdem alle Daten gelesen wurden, soll die Person mit den meisten Nachrichten
ausgegeben werden, indem eine Liste von (count, email)-Tupel aus dem Dictio-
nary erstellt wird. Dann muss die Liste in umgekehrter Reihenfolge sortiert und
schließlich die Person mit den meisten Nachrichten ausgegeben werden.'''

mails = open('mbox.txt', 'r')

addresses = dict()
for line in mails:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2 and words[1] not in addresses:
            addresses[words[1]] = 1
        elif len(words) > 2 and words[1] in addresses:
            addresses[words[1]] += 1

address_list = list()
for key, val in addresses.items():
    address_list.append((val, key))
address_list.sort(reverse=True)
for count, address in address_list[:1]:
    print(address, count)