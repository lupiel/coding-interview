def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] > target:
            right = right - 1
        elif  nums[left] + nums[right] < target:
            left = left + 1
        else:
            return [left+1, right+1]
    return [-1, -1]
# T O(n)
# M O(1)


numbers = [2,7,11,15]
target = 9
assert two_sum(numbers, target) == [1,2]



numbers = [1,2,3,5,8,9,10]
target = 8
assert two_sum(numbers, target) == [3,4]

