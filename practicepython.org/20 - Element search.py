"""Write a function that takes an ordered list of numbers (a list where
the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the
list and returns (then prints) an appropriate boolean."""

def elementSearch(numbers, element):
    numbers.sort()
    if element in numbers:
        return True
    else:
        return False

numbers = [3, 6, 2, 56, 14, 5, 9, 10]
element = 14

print(elementSearch(numbers, element))