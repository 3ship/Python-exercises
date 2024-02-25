import string
fhand = open('romeo-full.txt')

# Create dictionary with word counts:
counts = dict()
for line in fhand:
    line = line.lower().strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    for word in line.split():
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Switch key and value to sort the dictionary by word count.
# When comparing tuples, the first element in each tuple
# will be compared first.
sortinglist = list()
for key, value in counts.items():
        sortinglist.append((value, key))
sortinglist.sort(reverse=True)

for key, value in sortinglist[:10]:
    print(key, value)