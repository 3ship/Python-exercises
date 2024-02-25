import re

try:
    file = open(input('Choose file: '))
except:
    print('File doesn\'t exist.')
    exit()
spamValue = []
for line in file:
    line = line.rstrip()
    spam = re.findall('X-DSPAM-Confidence: \S+', line)
    if len(spam) > 0:
        print(spam)
        spam = spam[0]
        spamValue.append(float(spam[20:]))
result = sum(spamValue) / len(spamValue)
print(f'Wahrscheinlichkeit fuer kein-Spam: {result}')