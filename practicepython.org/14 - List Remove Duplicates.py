import random

def create_list():
    the_list = []
    for i in range(20):
        the_list.append(random.randint(0,100))
    return the_list
    
def convert(my_list):
    return list(set(my_set))
    print(len(my_set))
    
convert(create_list())