# 1..j..n
# .
# i
# .
# m

grid = [
    [1,1,0,0,1],
    [0,1,0,0,1],
    [1,0,1,0,1],
    [0,1,0,0,1],
]

def biggest_island(grid):
    biggest_so_far = 0
    m = len(grid)
    n = len(grid[0])

    def destroy_island(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        return 1 + destroy_island(i-1, j) + destroy_island(i+1, j) + destroy_island(i, j-1) + destroy_island(i, j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                destroyed_size = destroy_island(i, j)
                biggest_so_far = max(biggest_so_far, destroyed_size)


    return biggest_so_far

print(biggest_island(grid))