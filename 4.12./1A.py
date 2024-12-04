sum = 0
grid = []
with open('./4.12./input.txt', 'r') as f:
    for s in f:
        sum += s.count("XMAS")
        sum += s.count("SAMX")
        grid.append(list(s)[:-1])

for i in range(len(grid) - 3):
    for j in range(len(grid[i])):
        word = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
        if word == "XMAS" or word == "SAMX":
            sum += 1

for i in range(len(grid) - 3):
    for j in range(len(grid[i]) - 3):
        word = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]
        if word == "XMAS" or word == "SAMX":
            sum += 1

for i in range(len(grid) - 3):
    for j in range(3, len(grid[i])):
        word = grid[i][j] + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3]
        if word == "XMAS" or word == "SAMX":
            sum += 1
print(sum)