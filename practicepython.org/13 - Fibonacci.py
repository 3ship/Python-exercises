def fibonacci(s, n):
    list1 = []
    a, b = 0, s
    while len(list1) < n:
        a, b = b, a + b
        list1.append(a)
    return list1

query = int(input("Start number: "))
query2 = int(input("How long should the Fibonacci sequence be? "))

print(fibonacci(query, query2))