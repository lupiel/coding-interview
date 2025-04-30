# 6,7,8,1,2,3
# i   m     j
# nums[m] > nums[j]
# i = m + 1

# 6,7,8,1,2,3
# i     m   j
# j = m

# 1,2,3,6,7,8
# i   m     j

# 1,2,3,6,7,8
# i m j

#  1,2,3,6,7,8
# im j

#   1,2,3,6,7,8
# imj
 

def find_index_of_min(nums):
    i, j = 0, len(nums) - 1

    while i < j:
        m = (i + j) // 2
        if nums[m] > nums[j]:
            i = m + 1
        else:
            j = m

    return i

def find(nums, target):
    index_of_min = find_index_of_min(nums)

    if index_of_min == 0:
        i, j = 0, len(nums) - 1
    elif target >= nums[0] and target <= nums[index_of_min - 1]:
        i, j = 0, index_of_min - 1
    else:
        i, j = index_of_min, len(nums) - 1

    while i <= j:
        m = (i + j) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            j = m - 1
        else:
            i = m + 1

    return -1

print(find([3,4,5,1,2], 5))
print(find([4,5,6,7,0,1,2], 4))
print(find([4,5,6,7,0,1,2], 5))
print(find([4,5,6,7,0,1,2], 7))
print(find([4,5,6,7,0,1,2], 0))
print(find([4,5,6,7,0,1,2], 1))
print(find([4,5,6,7,0,1,2], 2))


print(find([0,1,2,4,5,6,7], -10))
print(find([0,1,2,4,5,6,7], 0))
print(find([0,1,2,4,5,6,7], 1))
print(find([0,1,2,4,5,6,7], 4))
print(find([0,1,2,4,5,6,7], 6))
print(find([0,1,2,4,5,6,7], 7))


print(find([-1,0,1,2,4,5,6,7], -10))
print(find([-1,0,1,2,4,5,6,7], 1))
print(find([-1,0,1,2,4,5,6,7], 4))
print(find([-1,0,1,2,4,5,6,7], 6))
print(find([-1,0,1,2,4,5,6,7], 7))


print(find([11,13,15,17], -1))

