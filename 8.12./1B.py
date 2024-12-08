from collections import defaultdict

antennas = set()
nodes = set()
positions = defaultdict(list)
line_n = 0

with open('./8.12./input.txt', 'r') as f:
    for l in f:
        l = list(l)[:-1]
        grid_len_x = len(l)
        for i in range(len(l)):
            if l[i] != ".":
                positions[l[i]].append([line_n, i])
                antennas.add(l[i])
        line_n += 1
    
    for antenna in antennas:
        for i in range(len(positions[antenna])):
            for j in range(i + 1, len(positions[antenna])):
                a = positions[antenna][i]
                b = positions[antenna][j]
                # adding antennas automatically to nodes because they are in resonance of themsleves
                nodes.add((a[0], a[1]))
                nodes.add((b[0], b[1]))
                y_dif = a[0] - b[0]
                x_dif = a[1] - b[1]
                for k in range(1, 100):
                    new_y = [a[0] + y_dif * k, b[0] + (y_dif * -1 * k)]
                    new_x = [a[1] + x_dif * k, b[1] + (x_dif * -1 * k)]
                    a_new = [new_y[0], new_x[0]]
                    b_new = [new_y[1], new_x[1]]
                    nodes.add((a_new[0], a_new[1]))
                    nodes.add((b_new[0], b_new[1]))
                    
sum = 0
for n in nodes:
    if n[0] >= 0 and n[0] < line_n and n[1] >= 0 and n[1] < grid_len_x:
        sum += 1
print(sum)
            