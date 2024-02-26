def is_power(a, b):
    if a == 1:
        return True
    if a % b == 0:
        return is_power(a/b, b)
    return False

if __name__=='__main__':
    print(is_power(81, 9))