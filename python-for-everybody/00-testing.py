stuff = "Hi"
print(dir(stuff))
test = ['capitalize', 'casefold', 'center', 'count', 'encode',
'endswith' , 'expandtabs', 'find', 'format', 'format_map',
'index' , 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier' , 'islower', 'isnumeric', 'isprintable',
'isspace' , 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip' , 'maketrans', 'partition', 'replace', 'rfind',
'rindex' , 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split' , 'splitlines', 'startswith', 'strip', 'swapcase',
'title' , 'translate', 'upper', 'zfill']

test2 = "This is a test. Don't pay attention."

print(test2.find("a"))

word = 'banane'
test3 = []
for i in word:
    test3.extend(i)
test3.sort()
print(test3)
print(word.count("a"))

count = 2
zeichen = 'a'
print('Buchstabe: ' + zeichen + ' Anzahl: ' + str(count))

print(hex(42))