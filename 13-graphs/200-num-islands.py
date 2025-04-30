# [
#     [1 ... n],
#     ...
#     [m ... n]
# ]

def num_islands(grid):
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    # right bottom corner coordinates are [m-1][n-1]

    # i in [0, n-1]
    # j in [0, m-1]
    def destroy_island(a, b):
        if a < 0 or a >=n or b < 0 or b >= m:
        #out of bound
            return
        if grid[a][b] == 0:
        # not an island
            return

        grid[a][b] = 0
        destroy_island(a-1, b)
        destroy_island(a+1, b)
        destroy_island(a, b-1)
        destroy_island(a, b+1)

    islands_destroyed = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                islands_destroyed += 1
                destroy_island(i, j)


    return islands_destroyed

grid = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]
print(num_islands(grid))


grid = [
  [1,1,0,1,0],
  [1,1,0,1,0],
  [1,1,0,0,1],
  [0,0,0,1,0]
]
print(num_islands(grid))
