                # f
# nums = [2,3,1,1,4]
        # 0 1 2 3 4


def can_jump(nums):

    f = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if f - i <= nums[i]:
            f = i

    return not f

nums = [2,3,1,1,4]
print(can_jump(nums))

nums = [2,2,1,0,4]
print(can_jump(nums))