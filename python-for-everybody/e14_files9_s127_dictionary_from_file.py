# Dictionaries - p. 127
# Übung 1: Erstelle dictionary aus Inhalt der Datei
with open('words.txt') as words:
    test = {}
    count = 0
    for line in words:
        line = line.strip()
        test[count] = line # Dateizeile als Wert
        count += 1

with open('words.txt') as words:
    test2 = {}
    for line in words:
        line = line.strip()
        test2[line] = 'ok' # Dateizeile als Schlüssel
    
print(13 in test)
print(test)
print(test2)