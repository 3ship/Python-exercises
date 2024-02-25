"""Take a list and write a program that prints out all the elements of the
list that are less than 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for x in a:
    if x < 5:
        b.append(x)

print(b)

"""Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user."""

c = []
number = int(input("Give me a number! "))
for x in a:
    if number > x and x not in c: # prevents numbers from being added twice
        c.append(x)
        
print(c)