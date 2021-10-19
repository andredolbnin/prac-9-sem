N , M = eval(input())

a = len(str(N))
b = len(str(N))
c = len(str(N * N))

extra_size = 8
size = 6 + a + b + c
columns = 0
l = 0
while l < M:
    l += size
    if l < M:
        columns += 1
    l += 3

def print_delimiter():
    print('=' * M)
    return None

cur = 0
cur_base = 0
print_delimiter()
while cur < N:
    for i in range(1, N + 1):
        s = ''
        for col in range(columns):
            cur += 1
            s += f'{cur:{a}} * {i:<{b}} = {cur * i:<{c}}'
            if cur == N:
                break
            if col != columns - 1:
                s += ' | '
        print(s)
        cur = cur_base
    cur_base += columns
    cur = cur_base
    print_delimiter()
        

