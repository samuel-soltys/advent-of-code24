# Global variable to track the number of paths
sum1 = 0
sum2 = 0

def search(grid, cur, num, endings):
    # If the current number is 9, increment the SUM and return
    if num == 9:
        endings.append(cur)
        return endings
    
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = cur[0] + dx, cur[1] + dy
        # Check if the move is within bounds and matches the next number
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == num + 1:
            search(grid, (nx, ny), num + 1, endings)
    return endings

grid = []
starting = []

# Read the grid from input file
with open('./10.12./input.txt', 'r') as f:
    for l in f:
        grid.append(list(map(int, l.strip())))

# Identify all starting positions where the value is 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            starting.append((i, j))

# Traverse from all starting positions
for start in starting:
    endings = search(grid, start, 0, [])
    sum1 += len(set(endings))
    sum2 += len(endings)

print(sum1)
print(sum2)