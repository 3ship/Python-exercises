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
    for character in s:
        if character in lows:
            index = lows.find(character)
            new_s += lows[(index + n) % 26]
        elif character in caps:
            index = caps.find(character)
            new_s += caps[(index + n) % 26]
        else:
            new_s += character
    return new_s

if __name__=='__main__':
    print(rotate_word('TestString. WithCaps!', 4))

# The book suggests that this could also be done with the built-in functions
# ord() and chr() which translate letters to numeric characters and the other
# way around.