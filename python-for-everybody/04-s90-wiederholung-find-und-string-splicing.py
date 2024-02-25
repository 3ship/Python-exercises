'''Seite 90
Verwenden Sie find und String-Slicing, um den Teil der Zeichenkette nach dem
Doppelpunkt zu extrahieren, und verwenden Sie dann die Funktion float, um die
extrahierte Teilzeichenkette in eine Fließkommazahl zu konvertieren.'''

str1 = 'X-DSPAM-Confidence: 0.8475'
str2 = str1.find(" ")
str3 = str1[str2:]
flo = float(str3)
print(flo, type(flo))

'''Vielleicht möchten Sie mit einigen von ihnen experimentieren,
um sicherzustellen, dass Sie verstehen, wie sie funktionieren.
strip und replace sind besonders nützlich.'''

str1 = 'X-DSPAM-Confidence: 0.8475'
str2 = str1.find(" ")
str3 = str1[str2:].strip()
print(float(str3))

# replace() Test

str1 = 'X-DSPAM-Confidence: 0.8475'
str2 = str1.replace('X-DSPAM-Confidence: ', '')
print(str2)
print(float(str2))