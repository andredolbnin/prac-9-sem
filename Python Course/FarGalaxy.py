from math import sqrt

galaxies = dict()
while True:
    input1 = input()
    if ' ' not in input1:
        break
    input_splitted = input1.split(' ')
    coords = (float(input_splitted[0]), float(input_splitted[1]), float(input_splitted[2]))
    name = input_splitted[3]
    galaxies[coords] = name
    
keys = list(galaxies.keys())
max_delta = 0.0
two_coords = None
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        delta = 0
        for k in range(3):
            delta += (keys[i][k] - keys[j][k]) ** 2
        delta = sqrt(delta)
        if delta >= max_delta:
            max_delta = delta
            two_coords = (keys[i], keys[j])
            
res = sorted([galaxies[two_coords[0]], galaxies[two_coords[1]]])
print(* res)