def sumFib(start, until):
    x = 0
    y = 1
    count = 0
    while x < until:
        sum = x + y
        if(sum % 2 == 0):
            count += sum
        x = y
        y = sum
    print(repr(count))


sumFib(0, 4000000)