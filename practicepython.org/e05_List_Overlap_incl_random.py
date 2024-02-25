"""Take two lists and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""

import random

a = []
b = []
c = []

while len(a) < random.randint(10,15):
    a.append(random.randint(1,100))
while len(b) < random.randint(15,21):
    b.append(random.randint(1,100))
print(a)
print(b)

for x in a:
    if x in b and x not in c:
        c.append(x)
        
print(c)