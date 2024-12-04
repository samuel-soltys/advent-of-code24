sum = 0
grid = []
with open('./4.12./input.txt', 'r') as f:
    for s in f:
        grid.append(list(s)[:-1])

for i in range(len(grid) - 2):
    for j in range(len(grid[i]) - 2):
        right_diagonal = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
        left_diagonal = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
        if (right_diagonal == "MAS" or right_diagonal == "SAM") and (left_diagonal == "MAS" or left_diagonal == "SAM"):
            sum += 1
print(sum)