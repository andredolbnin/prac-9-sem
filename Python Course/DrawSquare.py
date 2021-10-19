def filling(s, X, Y, r, c):
    for y in range(Y, Y + r):
        for x in range(X, X + r):
            s[y][x] = c


def squares(w, h, *args):
    s = []
    for y in range(h):
        extra_s = []
        for x in range(w):
            extra_s.append('.')
        s.append(extra_s)
        
    for i in range(len(args)):
        filling(s, args[i][0], args[i][1], args[i][2], args[i][3])
    
    for y in range(h):
        tmp = ''
        print(tmp.join(s[y]))