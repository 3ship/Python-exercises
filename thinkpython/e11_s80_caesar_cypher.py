"""Write a function called rotate_word that takes a string and an integer
as parameters, and returns a new string that contains the letters from the
original string rotated by the given amount."""

from string import ascii_lowercase as lows
# We could set all letters to .lower() and get rid off the elif statement
from string import ascii_uppercase as caps

def rotate_word(s, n):
    """Takes the input string s and rotates every letter by n.
    Using modulo 26 to 'wrap around' the alphabet string, if necessary."""
    new_s = ""
    for letter in s:
        if letter in lows:
            index = lows.find(letter)
            new_s += lows[(index + n) % 26]
        elif letter in caps:
            index = caps.find(letter)
            new_s += caps[(index + n) % 26]
        else:
            continue
    return new_s

if __name__=='__main__':
    print(rotate_word('TestStringWithCaps', 3))