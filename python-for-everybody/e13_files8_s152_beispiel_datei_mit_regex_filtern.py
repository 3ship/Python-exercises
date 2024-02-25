import re

file = open('mbox-short.txt')

mails = []
for line in file:
    line = line.rstrip()
    mail = re.findall('\S+@\S+\.\S+', line)
    if len(mail) == 0:
        continue
    mail = mail[0]
    for char in mail:
        if char in '<>;':
            mail = mail.replace(char, '')
    if mail not in mails:
        mails.append(mail)

mails.sort()
mails = '\n'.join(mails)
output = open('output.txt', 'w')
output.write(mails)
output.close()