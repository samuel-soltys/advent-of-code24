sum = 0
grid = []
directions = [
    (-1, 0),    # UP
    (0, 1),     # RIGHT
    (1, 0),     # DOWN
    (0, -1),    # LEFT
]
dir_index = 0
i = 0

with open('./6.12./input.txt', 'r') as f:
    for l in f:
        l = list(l)[:-1]
        if "^" in l:
            current = [i, l.index("^")]
        grid.append(l)
        i += 1

starting = list(current)
final_sum = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        old = grid[i][j]
        current = list(starting)
        dir_index = 0
        if grid[i][j] != "#":
            iterations = 0
            grid[i][j] = "#"
            while current[0] < len(grid) and current[0] > 0 and current[1] < len(grid[0]) and current[1] > 0:
                grid[current[0]][current[1]] = "X"
                nextRow = current[0] + directions[dir_index][0]
                nextCol = current[1] + directions[dir_index][1]
                try:
                    next = grid[nextRow][nextCol]
                except IndexError:
                    break
                if next == "." or next == "X":
                    current[0] = nextRow 
                    current[1] = nextCol
                elif next == "#":
                    dir_index += 1
                    dir_index = dir_index % 4
                iterations += 1
                # Check if infinite loop
                if iterations > 10000:
                    final_sum += 1
                    break
        grid[i][j] = old
                    
for n in grid:
    sum += n.count("X")

print(final_sum)