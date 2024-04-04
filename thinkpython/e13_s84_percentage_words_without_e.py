# Write a program that reads words.txt and prints only the words that have
# no “e”. Compute the percentage of words in the list that have no “e”.

fname = open('words.txt', 'r')
total = 0
no_e = 0
for word in fname:
    word = word.strip()
    if "e" in word:
        total += 1
    else:
        total += 1
        no_e +=1
no_e_percentage = no_e / total * 100
print(no_e_percentage)