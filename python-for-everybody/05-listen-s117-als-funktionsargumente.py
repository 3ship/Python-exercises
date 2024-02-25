''' Seite 117
Schreiben Sie eine Funktion namens remove_all, die eine Liste und
einen Wert entgegennimmt und alle Vorkommen des Wertes aus der Liste entfernt.
Die Funktion soll die Liste in-place verändern und als Ergebnis None zurückgeben.
Es ist wichtig, zwischen Operationen zu unterscheiden, die Listen verändern, und
Operationen, die neue Listen erzeugen.'''


def purge(liste, wert):
    count = 0
    for listenobj in liste:
        if listenobj == wert:
            del liste[count] # liste.pop(count)
        count += 1
    return liste

example = ["1", "2", "1", "3", "4", "1"]
print(purge(example, "1"))