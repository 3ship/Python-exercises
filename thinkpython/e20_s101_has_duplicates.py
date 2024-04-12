# 10.7: Check list for duplicates
# Integers 1 and 0 are handled as booleans

def has_duplicates(ls):
    s = set((ls))
    if len(ls) != len(s):
        return False
    return True

def alt_has_duplicates(ls):
    ls_cache = dict()
    for element in ls:
        if element not in ls_cache:
            ls_cache[element] = 1
        else:
            ls_cache[element] += 1
    for element in ls_cache:
        if ls_cache[element] > 1:
            return False
    return True

if __name__=='__main__':
    ls = [True, 1, 2, 3, 4, 5, 6]
    ls2 = [1, 2, 2, 3, 4, 5, 6]
    ls3 = [1, 2, 3, 4, 5]
    print(alt_has_duplicates(ls))
    print(alt_has_duplicates(ls2))
    print(alt_has_duplicates(ls3))