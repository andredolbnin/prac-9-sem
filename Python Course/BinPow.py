def BinPow(a, N, f):
    
    def func(x, y):
        return f(x,y)
    
    if N == 1:
        return a
    if N % 2 == 1:
        return func(BinPow(a, N - 1, f), a)
    else:
        return func(BinPow(a, N // 2, f), BinPow(a, N // 2, f))
    
