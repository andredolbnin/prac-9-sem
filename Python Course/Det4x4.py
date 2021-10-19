matrix = eval(input())

def det_definer(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        dop = m[1:len(m)]
        r = 0
        for j in range(len(m)):
            dop1 = []
            for i in range(len(dop)):
                dop1.append(dop[i][:j] + dop[i][j+1:])
            if j % 2 == 1:
                r += m[0][j] * det_definer(dop1)
            else:
                r -= m[0][j] * det_definer(dop1)

        return r
    
            
print(det_definer(matrix))