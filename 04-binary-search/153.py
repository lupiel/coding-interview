# 6,7,8,1,2,3
# i   m     j
# M>J  --> i=m+1

# 6,7,8,1,2,3
# i     m   j
# M<J --> j = m


def find_min(nums):
    i, j = 0, len(nums) - 1

    while i < j:
        m = int((i+j)/2)
        if nums[m]>nums[j]:
            i = m + 1  
        else:
            j = m

    return [i, nums[i:] + nums[:i]]

print(find_min([3,4,5,1,2]))
print(find_min([4,5,6,7,0,1,2]))
print(find_min([11,13,15,17]))