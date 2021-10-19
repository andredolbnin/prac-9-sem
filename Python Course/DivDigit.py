def divdigit(N):
    orig_N = N
    count = 0
    while N != 0:
        last_digit = N % 10
        if last_digit != 0:
            if orig_N % last_digit == 0:
                count += 1
        N //= 10
        
    return count
