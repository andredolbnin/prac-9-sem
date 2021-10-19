pict = []
pict.append([*input()])
while True:
    current_input = [*input()]
    pict.append(current_input)
    if '-' in current_input:
        break
count = 0
for i in range(len(pict)):
    for j in range(len(pict[0])):
        if pict[i][j] == '#' and pict[i+1][j] != '#' and pict[i][j+1] != '#':
            count += 1
print(count)
