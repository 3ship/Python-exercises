# Beispiel: Dictionary zum Zählen von identischen Elementen
# in einem String verwenden:

word = 'brontosaurus'
d = dict()
for char in word:
    if char not in d:
        d[char] = 1
    else:
        d[char] = d[char] + 1
print(d)

# Mit get()-Funktion.
# get() Gibt Standardwert (hier 0) als Wert zurück, wenn der Schlüssel nicht vorkommt.

word = 'brontosaurus'
d = dict()
for char in word:
    d[char] = d.get(char, 0) + 1
print(d)