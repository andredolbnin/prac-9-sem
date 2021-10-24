from math import sqrt

seq = set(eval(input()))
M = max(seq)

square_seq = set(i * i + j * j + k * k 
             for i in range(1, int(sqrt(M)) + 1)
             for j in range(i, int(sqrt(M - i * i)) + 1) 
             for k in range(j, int(sqrt(M - i * i - j * j)) + 1))

print(len(seq & square_seq))