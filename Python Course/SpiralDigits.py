n, m = eval(input()) # m - строка, n - столбец
spiral_list = [[-1 for j in range(n)] for i in range(m)]
i, j = 0, 0
direction_list = ['e', 's', 'w', 'n']
direction = 'e'
direction_index = 0
count = 0
current_number = 0
i_min, j_min, i_max, j_max = 0, 0, m - 1, n - 1
while count < n * m:
    spiral_list[i][j] = current_number
    current_number = (current_number + 1) % 10
     
    has_to_change_direction = False
    if direction == 'e':
        if j != j_max:
            j += 1
        else:
            i += 1
            i_min += 1   
            has_to_change_direction = True
    elif direction == 's':
        if i != i_max:
            i += 1
        else:
            j -= 1
            j_max -= 1  
            has_to_change_direction = True
    elif direction == 'w':
        if j != j_min:
            j -= 1
        else:
            i -= 1
            i_max -= 1   
            has_to_change_direction = True
    elif direction == 'n':
        if i != i_min:
            i -= 1
        else:
            j += 1
            j_min += 1
            has_to_change_direction = True
    
    if has_to_change_direction:
        if direction_index == 3:
            direction_index = -1
        direction_index += 1
        direction = direction_list[direction_index]
        
    count += 1
        
    
for item in spiral_list:
    print(*item)
    
