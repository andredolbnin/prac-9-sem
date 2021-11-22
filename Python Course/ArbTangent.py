from decimal import *
from math import factorial
#import time #

A = Decimal(input())
P = int(input())

#start = time.time() #

def inv_pi():
    s = Decimal(0)
    prev = -1
    n = 0
    while True:
        s += ((factorial(6 * n) * Decimal(13591409 + 545140134 * n)) / 
              (factorial(3 * n) * factorial(n) ** 3 * Decimal(-262537412640768000) ** n))
        check = int(s * 10 ** P) 
        if check == prev:
            break
        prev = check
        n += 1
    return s / (426880 * Decimal(10005).sqrt())

def sin(x):
    s = Decimal(0)
    prev = -1
    n = 0
    while True:
        s += (-1) ** n * Decimal(x ** (2 * n + 1)) / Decimal(factorial(2 * n + 1))
        check = int(s * 10 ** P) 
        if check == prev:
            break
        prev = check
        n += 1
    return s

def cos(x):
    s = Decimal(0)
    prev = -1
    n = 0
    while True:
        s += (-1) ** n * Decimal(x ** (2 * n)) / Decimal(factorial(2 * n))
        check = int(s * 10 ** P) 
        if check == prev:
            break
        prev = check
        n += 1
    s += Decimal(10 ** (- 2 * P)) # to overcome 1
    return s

getcontext().prec = P + 3
x = A / (200 * inv_pi())
res = Context(prec = P).create_decimal(sin(x) / cos(x))
print(res)

#print(time.time() - start) #