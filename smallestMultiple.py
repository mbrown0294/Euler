def smallestMultiple(n):
    mult = n
    x = 1
    while x <= n:
        if mult % x != 0:
            x = 1
            mult += 1
        x += 1
    return mult


print(smallestMultiple(20))