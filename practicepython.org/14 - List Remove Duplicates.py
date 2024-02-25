"""Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates."""

import random

def create_list():
    the_list = []
    for i in range(20):
        the_list.append(random.randint(0,100))
    return the_list
    
def convert(my_list):
    my_list = list(set(my_list))
    print(my_list)
    
convert(create_list())