
'''
def factorList(n):
    factors = []
    for x in range(1,n+1):
        if n % x == 0:
            factors.append(x)
    return factors
'''


def factorCount(n):
    factors = 0
    for x in range(1,n+1):
        if n % x == 0:
            factors += 1
    return factors


'''
def triangleNums(n):
    nums = []
    count = 0
    for x in range(1, n + 1):
        count += x
        nums.append(count)
    return nums
'''


def triangleNum(n):
    num = 0
    for x in range(n+1):
        num += x
    return num


'''
def overNDivisors(n):
    nums = []
    x = 10000
    while True:
        triNum = triangleNum(x)
        fac = factorList(triNum)
        if len(fac) > n:
            break
        x += 1
    return triNum
'''


def overNDivisors(n):
    nums = []
    x = 1000
    while True:
        triNum = triangleNum(x)
        fac = factorCount(triNum)
        print(fac)
        if fac >= n:
            break
        x += 1
    return triNum


print(overNDivisors(500)) #takes for-freaking-ever. like FOREVER!!