data = input()
pattern = input()

first = pattern
for i in range(len(pattern)):
    if pattern[i] == '@':
        first = pattern[:i]
        break
 
j = -1
while True:
    j = data.find(first, j + 1)
    if j == -1:
        break

    is_break = True
    for i in range(len(pattern)):
        if len(data) <= i + j:
            j = -1
            break
        if data[i + j] != pattern[i] and pattern[i] != '@':
            is_break = False
            break
        
    if is_break:
        break
    
print(j)