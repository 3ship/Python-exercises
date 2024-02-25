# Regex - Suchen und extrahieren - Beispiele

import re

hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if re.search('^X-DSPAM-Conf\S*: [0-9.]+', line):
        print(line)

extract = open('mbox-short.txt', 'r')
for line in extract:
    line = line.rstrip()
    line = re.findall('^X-DSPAM-Conf\S*: ([0-9.]+)', line)
    if len(line) > 0:
        line = float(line[0])
        print(line)

orderedTimes = list()
timestamps = open('mbox-short.txt', 'r')
for line in timestamps:
    line = line.rstrip()
    line = re.findall('^From .* ([0-9]+):', line)
    if len(line) > 0:
        orderedTimes.append(line)
orderedTimes.sort()
print(orderedTimes)