# 10.1: Add up all integers from nested lists
# 10.3: Return a list without the first and last elements of the input list

def middle(t):
    return t[1:-1]

def nested_sum(t):
    total_sum = 0
    for sequence in t:
        i_sum = sum(sequence)
        total_sum += i_sum
    return total_sum

if __name__=='__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))
    print(middle(t))