def add(n):
    if n ==1:
        return n
    return n + add(n-1)



print(add(100))