"""a = int(input("Stick 1: "))
b = int(input("Stick 2: "))
c = int(input("Stick 3: "))
sticks = [a, b, c]
sticks.sort()

if sticks[2] > sticks[0] + sticks[1]:
    print("No.")
else:
    print("Yes.")"""
    
sticks2 = input("Sticks: ").split(",")
sticks2.sort()
print(sticks2)