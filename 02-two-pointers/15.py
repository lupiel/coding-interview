
# def three_sum(nums):
#     ret = set()
#     n = len(nums)
#     for i1 in range(n):
#         for i2 in range(i1+1, n):
#             for i3 in range(i2+1, n):
#                 if nums[i1]+nums[i2]+nums[i3] == 0:
#                     ret.add(tuple(sorted([nums[i1], nums[i2], nums[i3]])))
#     return [list(s) for s in list(ret)]



def three_sum(nums):
    res = []
    nums.sort()
    print(nums)
    i = 0
    while i < len(nums):
        num = nums[i]
        diff = 0 - num
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[j] + nums[k] < diff:
                j += 1
            elif nums[j] + nums[k] > diff:
                k -= 1
            else:
                # print(
                #     nums[i],
                #     nums[j],
                #     nums[k]
                # )
                res.append(
                    [
                        nums[i],
                        nums[j],
                        nums[k]
                    ]
                )
                # skipping repeated 3nd num
                while k > j and nums[k] == nums[k-1]:
                    k -= 1
                k -= 1

        # skipping repeated num
        while i < len(nums)-1 and nums[i] == nums[i+1]:
            i += 1
        
        i += 1

    return res


# print(three_sum(nums = [-5,-5,-4,-4,-3,-2,-1,0,1,2,3,4,5]))
print(three_sum(nums = [1,1,1,-1,0,1,2,-1,-4]))

# print(three_sum(nums = [0,2,2]))
# print(three_sum(nums = [0,0,0]))
# print(three_sum(nums = [-5,-5,-4,-4,-3,-2,-1,0,1,2,3,4,5]))
