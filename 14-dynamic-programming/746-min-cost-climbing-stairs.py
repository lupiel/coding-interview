# 1: 1
# 2: 11, 2
# 3: 21, 111, 12
# 4: 1111, 121, 211, 22, 112
# 5: 11111, 1112, 1121, 1211, 2111, 221, 212, 122

#       1 2 3 4 5 6 7
# cost  1 2 3 5 8 13


# c cost to get here
# 5 0
# 8 0 -2
# 4 5 -1
# 7 8
# 2 9
# 5 11
# 9 11
# 1 16
# 2 17

nums = [5,8,4,7,2,5,9,1,2]

def cheapest_climb(cost):
    
    cost_to_get_to_minus_1 = 0
    cost_to_get_to_minus_2 = 0

    n = len(cost)
    if n <= 2:
        return 0

    for i in range(2, n):
        cost_to_get_to_i = min(
            cost_to_get_to_minus_1 + cost[i-1],
            cost_to_get_to_minus_2 + cost[i-2]
        )

        cost_to_get_to_minus_2 = cost_to_get_to_minus_1
        cost_to_get_to_minus_1 = cost_to_get_to_i

    return cost_to_get_to_minus_1

print(cheapest_climb(nums))
