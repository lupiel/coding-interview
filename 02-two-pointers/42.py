def trapped_water(heights):

    n = len(heights)
    water_sum = 0

    left_max = [0] * n
    right_max = [0] * n

    max_height = 0
    for i in range(n):
        max_height = max(max_height, heights[i])
        left_max[i] = max_height

    max_height = 0
    for i in range(n-1, -1, -1):
        max_height = max(max_height, heights[i])
        right_max[i] = max_height

    for i in range(n):
        i_water_height = min(left_max[i], right_max[i]) - heights[i]
        if i_water_height < 0: i_water_height = 0
        water_sum = water_sum + i_water_height

    return water_sum

# prefil arrays left_max, right_max with max heights to the left/right of i
# for each i calculate water height as min(left_max, right_max) - heights[i], add to the sum
# return sum

print(trapped_water([0,2,0,3,1,0,1,3,2,1]))
print(trapped_water([0,1,0,3,1,0,1,2,0,1,0,6]))
