# 10.6: Return True, if the second input is an anagram of the latter

def is_anagram(first, second):
    first = first.lower()
    second = second.lower()
    if len(first) != len(second):
        return False
    first_counter = dict()
    for letter in first:
        if not first_counter.get(letter):
            first_counter[letter] = 1
        else:
            first_counter[letter] += 1
    second_counter = dict()
    for letter in second:
        if letter not in first:
            return False
        if not second_counter.get(letter):
            second_counter[letter] = 1
        else:
            second_counter[letter] += 1
    for letter in first_counter:
        if first_counter[letter] != second_counter[letter]:
            return False
    return True

if __name__=='__main__':
    first = input('Enter your first word: ')
    second = input('Enter your second word: ')
    if is_anagram(first, second):
        print('The two words are anagrams of each other!')
    else:
        print('These are not anagrams.')