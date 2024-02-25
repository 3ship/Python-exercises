"""Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the
string is in column 70 of the display."""

def right_justify(s):
    while len(s) < 70:
        s = " " + s
    return s

# Without loop; with concatenation/repetition:
def right_concat(s):
    spaces = " " * (70 - len(s))
    s = spaces + s
    return s

print(right_justify("This is a test."))
print(right_concat("This is another test."))