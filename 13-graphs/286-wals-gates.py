
map = [
    [float("inf"),-1,0,float("inf")],
    [float("inf"),float("inf"),float("inf"),-1],
    [float("inf"),-1,float("inf"),-1],
    [0,-1,float("inf"),float("inf")]
]


# for each field
#   if chest found traverse bfs and update land values


def walk_map(map):
    n = len(map)
    m = len(map[0])
    
    visited = set()

    def walk(i, j, distance):
        if i < 0 or i >= n or j < 0 or j >= m or map[i][j] < 0 or (i, j) in visited:
            return
        if map[i][j] > 0:
            map[i][j] = min(map[i][j], distance)
        visited.add((i,j))

        walk(i+1, j, distance + 1)
        walk(i-1, j, distance + 1)
        walk(i, j+1, distance + 1)
        walk(i, j-1, distance + 1)


    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                visited = set()
                walk(i, j, 0)

    return map

print(map)
print(walk_map(map))



# [
#     [inf, -1, 0, inf],
#     [inf, inf, inf, -1],
#     [inf, -1, inf, -1],
#     [0, -1, inf, inf]
# ]

# [
#     [3, -1, 0, 1],
#     [2, 2, 1, -1],
#     [1, -1, 2, -1],
#     [0, -1, 3, 4]
# ]
