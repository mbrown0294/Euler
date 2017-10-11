import math


def pythTriplets(x):
    nums = []
    for m in range(x):
        for n in range(x):
            if n > m:
                a = math.pow(n, 2) - math.pow(m, 2)
                b = 2 * n * m
                c = math.pow(n, 2) + math.pow(m, 2)
                if(a + b + c) == x:
                    nums.append(a)
                    nums.append(b)
                    nums.append(c)
    return nums


#did not end up using this function
def isTriplet(x,y,z):
    a = x
    b = y
    c = z
    if (a > c):
        c = x
        a = z
    elif (b > c):
        c = y
        b = z
    if (a > b):
        temp = b
        b = a
        a = temp
    if (math.pow(a,2) + math.pow(b,2)) == math.pow(c,2):
        return True
    return False


print(pythTriplets(1000))
print(375 * 200 * 425)