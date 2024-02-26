a = 81
b = 7

def is_power(a, b):
    if a == 1:
        return True
    if a % b == 0:
        return is_power(a/b, b)
    return False