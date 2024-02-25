''' Seite 80 - Übung 1
Schreiben Sie eine while-Schleife, die beim letzten Zeichen in der
Zeichenkette beginnt und sich rückwärts bis zum ersten Zeichen in
der Zeichenkette vorarbeitet, wobei jeder Buchstabe in einer eigenen
Zeile ausgegeben wird, natürlich rückwärts.'''

frucht = "banane"
index = -1
while abs(index) <= len(frucht):
    print(frucht[index])
    index -= 1
