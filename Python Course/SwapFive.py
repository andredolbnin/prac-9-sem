k = eval(input())
n = k
len_of_n = 1
dop = 0
while n * k != n // 10 + k * (10 ** (len_of_n - 1)):
    cur = n // (10 ** (len_of_n - 1))
    ending = cur * k % 10
    extra1 = ending + dop
    extra2 = 0
    if extra1 > 9: 
        extra1 = (ending + dop) % 10
        extra2 = (ending + dop) // 10
    n += extra1 * 10 ** len_of_n
    dop = cur * k // 10 + extra2
    len_of_n += 1
print(n)

