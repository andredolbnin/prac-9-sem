from collections import deque

def search(start, end, d):
    q = deque()
    q += d[start]
    searched = set()
    while q:
        cur = q.popleft()
        if not cur in searched:
            if cur == end:
                print('YES')
                return
            else:
                q += d[cur]
                searched.add(cur)
                
    print('NO')
    return


start = None
end = None
d = dict()
while True:
    input1 = input()
    if ' ' not in input1:
        start = input1
        end = input()
        break
    else:
        input1_list = input1.split()
        in1 = input1_list[0]
        in2 = input1_list[1]
        
        if in1 in d:
            d[in1].add(in2)
        else:
            d[in1] = {in2}
            
        if in2 in d:
            d[in2].add(in1)
        else:
            d[in2] = {in1}
            
search(start, end, d)