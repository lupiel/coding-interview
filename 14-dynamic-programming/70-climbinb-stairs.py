# 1: 1
# 2: 11, 2
# 3: 21, 111, 12
# 4: 1111, 121, 211, 22, 112
# 5: 11111, 1112, 1121, 1211, 2111, 221, 212, 122

# n 1 2 3 4 5 6 7
#   1 2 3 5 8 13


def n_ways_to_climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev, curr = 1, 2

    for i in range(3, n+1):
        prev, curr = curr, curr + prev

    return curr

print(n_ways_to_climb_stairs(5))
