# 10.9: Create a list from the words in words.txt using two different methods
# Measure, which method is faster

import time

def append_method():
    with open('words.txt') as words:
        ls = list()
        for line in words:
            line = line.strip()
            ls.append(line)
        return


def plus_method():
    with open('words.txt') as words:
        ls = list()
        for line in words:
            line = line.strip()
            ls += [line]
        return

if __name__=='__main__':
    plus_start = time.time()
    plus_method()
    plus_time = time.time() - plus_start
    append_start = time.time()
    append_method()
    append_time = time.time() - append_start
    if plus_time > append_time:
        difference = round(plus_time - append_time, 5)
        print(f"The append method is {difference} seconds faster")
    elif append_time > plus_time:
        difference = round(append_time - plus_time, 5)
        print(f"The plus method is {difference} seconds faster")
    else:
        print("Both methods are equally fast.")