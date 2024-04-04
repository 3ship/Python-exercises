# Parse the Moby Project text file containing unique English words and print
# all words containing more than 20 characters without white space

fname = open('words.txt', 'r')
for word in fname:
    word = word.strip()
    if len(word) > 20:
        print(word)