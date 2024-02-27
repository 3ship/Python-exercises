"""Copy the mysqrt() function based on Newton's method and write a
test_square_root() function to compare the results to math.sqrt()
Display the results in a table."""

import math

def mysqrt(a):
    """Uses Newton's method to approximate the square root of a"""
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

def square_root(a):
    return math.sqrt(a)

def test_square_root(a):
    """Prints a table with the results of mysqrt() and square_root()
    from 1 to a. The 4th column shows the difference between the two results.
    """
    print("a     mysqrt(a)          math.sqrt(a)       diff")
    print("-     ---------          ------------       ----")
    for i in range(1, a+1):
        # Print the results along with the right amount of whitespace:
        print(f"{i}" + (6-len(str(i)))*" " +
              f"{mysqrt(i)}" + (19-len(str(mysqrt(i))))*" " +
              f"{square_root(i)}" + (19-len(str(square_root(i))))*" " + 
              f"{square_root(i) - mysqrt(i)}")

if __name__=='__main__':
    test_square_root(30)