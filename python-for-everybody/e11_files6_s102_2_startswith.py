'''Schreiben Sie ein Programm, das nach einem Dateinamen fragt, und
iterieren Sie dann durch die Datei und sucht nach Zeilen der Form:
X-DSPAM-Confidence: 0.8475
Wenn Sie auf eine Zeile stoßen, die mit X-DSPAM-Confidence: beginnt, trennen
Sie die Zeile auf, um die Fließkommazahl in der Zeile zu extrahieren. Zählen Sie
diese Zeilen und berechnen Sie dann die Summe der Werte aus diesen Zeilen. Wenn
Sie das Ende der Datei erreichen, geben Sie den Durchschnittswert aus.'''

pickFile = open(input("Datei: "))
spamValue = []
for line in pickFile:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence: '): continue
    line = line.split()
    spamValue.append(float(line[1]))
result = sum(spamValue) / len(spamValue)
print(f'Wahrscheinlichkeit fuer kein-Spam: {result}')