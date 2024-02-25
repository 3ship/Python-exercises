# Beispiel Userinput mit try/except abfangen

def filename():
    result = input("Gib einen Dateinamen an: ")
    return result

fname = filename()
try:
    fhand = open(fname)
except:
    print(f'Datei {fname} konnte nicht gefunden werden!')
    fname = filename()
    fhand = open(fname)

count = 0
for line in fhand:
    count += 1
print(f'Die Datei {fname} hat {count} Zeilen.')