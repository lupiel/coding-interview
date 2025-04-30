nums1 = [9, 1, 1,  9,  1,  15, 100]
#    9 1 1  9  1  15 100
#9 1 9 9 10 18 18 33 118
nums2 = [1,  100, 100, 1,    1,    100]
# 1   100 100 1    1    100
# 1   100 101 101  102  201
# x_2 x_1  ^

def house_robber(nums):
    n = len(nums)
    
    if n <= 2:
        return max(nums[:2])

    x_1, x_2 = 0, 0   # max robbed at the house

    for house in range(n):
        curr_max = max(
            x_1,
            x_2 + nums[house]
        )

        x_1, x_2 = curr_max, x_1

    return curr_max

print(house_robber(nums1))
print(house_robber(nums2))
print(house_robber([1]))
