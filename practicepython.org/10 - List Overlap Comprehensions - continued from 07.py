a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = [x for x in set(a) if x in set(b)]
print(result)

print("")
# Alternatively:
result2 = list({x for x in a if x in b})
print(result2)