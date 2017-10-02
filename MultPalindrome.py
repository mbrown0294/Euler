import math


def multPali(n):
    count = 0
    base = (int)(math.pow(10,n)) - 1
    end = (int)(math.pow(10,(n-1)))
    for x in range(base, end - 1, -1):
        for y in range(base, end - 1, -1):
            if isPali(x * y):
                if((x * y) > count):
                    count = x * y
    return count


def isPali(n):
    num = str(n)
    leng = len(num)
    halfLen = math.floor(leng / 2)
    phr1 = num[0:halfLen]
    if(leng % 2 == 0):
        phr2 = num[leng:halfLen-1:-1]
    else:
        phr2 = num[leng:halfLen:-1]
    return phr1 == phr2


print(multPali(3))