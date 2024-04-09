# Find a word or words with three consecutive double-letters

def triple_double(word):
    i = 0
    pairs = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            pairs += 1
            if pairs == 3:
                return True
            i += 2
        else:
            pairs = 0
            i += 1
    return False

with open('words.txt') as wordlist:
    for word in wordlist:
        word = word.strip()
        if triple_double(word):
            print(word)
        else:
            continue