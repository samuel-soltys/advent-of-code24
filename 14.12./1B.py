import time

quadrants = [0, 0, 0, 0]
pos = []
vels = []
def print_grid(grid):
    for i in range(101):
        for j in range(103):
            if [i, j] in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()

with open('./14.12./input.txt', 'r') as f:
    for l in f:
        l = l.strip("\n").replace("p=", "").replace("v=", "").split(" ")
        p = list(map(int, l[0].split(",")))
        v = list(map(int, l[1].split(",")))
        pos.append(p)
        vels.append(v)

s = 1
while True:
    for i in range(len(pos)):
        pos[i][0] += vels[i][0]
        pos[i][0] %= 101
        if pos[i][0] < 0:
            pos[i][0] = 101 + pos[i][0]
        
        pos[i][1] += vels[i][1]
        pos[i][1] %= 103
        if pos[i][1] < 0:
            pos[i][1] = 103 + pos[i][1]
    # count how many have 4 neighbors
    count = 0
    for i in range(len(pos)):
        neighbors = 0
        for j in range(len(pos)):
            if i == j:
                continue
            if abs(pos[i][0] - pos[j][0]) <= 1 and abs(pos[i][1] - pos[j][1]) <= 1:
                neighbors += 1
        if neighbors >= 4:
            count += 1
    if count > 30:
        print(s)
        print_grid(pos)
        # wait for space to be pressed
        while True:
            if input() == " ":
                break
    s += 1
    
