segments = sorted(eval(input()))
length = 0
minus = 0
b_prev = -1
for a, b in segments:
    if b_prev > b:
        continue
    elif b_prev > a:
        minus -= b_prev - a
    length += b - a
    b_prev = b
print(length + minus)