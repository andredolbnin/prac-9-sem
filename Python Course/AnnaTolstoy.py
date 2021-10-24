import sys
import random

def tokenize(s):
    return s.replace('\n    ', ' @ ').split()


def magic(t, l, d, prev, prevprev):
    s1 = set(d[prevprev])
    l2 = d[prev]
    s2 = set([x - 1 for x in l2])
    g = list(s1 & s2)
    return t[random.choice(g) + 2]
    

N = int(input())
Txt = tokenize(sys.stdin.read())
#Txt = tokenize(input())
d = dict()
l = len(Txt)
for i in range(l - 2):
    if Txt[i] in d:
        d[Txt[i]].append(i)
    else:
        d[Txt[i]] = [i]
        
res = []
first = random.choice(d['@'])
res.append(Txt[first])
res.append(Txt[first + 1])
while len(res) < N:
    res.append(magic(Txt, l, d, res[-1], res[-2]))
    
print(' '.join(res).replace('@', '\n    '))      