'''Schreiben Sie ein Programm, welches die Häufigkeit von Nachrichten
pro Tageszeit (ganze Stunden) ermittelt. Die Stunden sollen aus der From-
Zeile extrahiert werden, indem die Uhrzeit gefunden und diese Zeichenfolge
dann anhand des Doppelpunkts in Teile zergliedert wird. Sobald die Nachrichten-
häufigkeit für jede Stunde gesammelt wurde, sollen diese wie weiter unten
gezeigt ausgegeben werden (eine pro Zeile, sortiert nach Stunde).'''

import re

orderedTimes = dict()
fname = open('mbox.txt', 'r')
for line in fname:
    line = line.rstrip()
    line = re.findall('^From .* ([0-9]+):', line)
    if not line:
        continue
    else:
        line = line[0]
    if line not in orderedTimes:
        orderedTimes[line] = 1
    else:
        orderedTimes[line] += 1
orderedTimes = list(orderedTimes.items())
orderedTimes.sort()

for time, count in orderedTimes:
    print(time, count)