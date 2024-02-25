"""word = 'Banane'
count = 0
for zeichen in word:
    if zeichen == 'a':
        count = count + 1
    print(count)

Wird zu:"""

word = 'Banane'
count = 0

def counter(a, b):
    for zeichen in a:
        if zeichen == 'a':
            b = b + 1
    print(b)

counter(word, count)