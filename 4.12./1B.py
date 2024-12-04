sum = 0
grid = []
with open('./4.12./input.txt', 'r') as f:
    for s in f:
        # sum += s.count("XMAS")
        # sum += s.count("SAMX")
        grid.append(list(s)[:-1])
# 1692

for i in range(len(grid) - 2):
    for j in range(len(grid[i]) - 2):
        print(i, j)
        right_diagonal = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
        left_diagonal = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
        print(right_diagonal)
        print(left_diagonal)
        if (right_diagonal == "MAS" or right_diagonal == "SAM") and (left_diagonal == "MAS" or left_diagonal == "SAM"):
            sum += 1
print(sum)