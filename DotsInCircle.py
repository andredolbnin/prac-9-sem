x, y, r = eval(input())
answer = 'YES'
i = 0
while (i >= 0):
    x1, y1 = eval(input())
    if x1 == 0 and y1 == 0:
        break
    if (x1 - x)**2 + (y1 - y)**2 > r**2:
        answer = 'NO'
    i += 1
print(answer)