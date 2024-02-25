a = 81
b = 9

def is_power(a, b):
    if a == 1:
        return True
    if a % b == 0:
        return is_power(a/b, b)
    return False