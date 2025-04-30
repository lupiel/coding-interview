
def longest_consecutive1(nums):
    nums = list(set(nums)) 
    nums.sort()

    res = 0
    streak = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            streak = streak + 1
            res = max(res, streak + 1)
        else:
            streak = 0

    return res

#create set
#sort the set
#go cell by cell !remember to skip repeating values!
#return longest streak
# Time O(n log)
# Space O(n)

def longest_consecutive(nums):
    nums_set = set(nums)

    res = 0
    streak = 0

    for n in list(nums_set):
        if (n-1) not in nums_set:
            # consecutive range starter detected
            i = 0
            while n + i in nums_set:
                i = i + 1
                streak = streak + 1
                res = max(res, streak)
            
            streak = 0

    return res
# Time O(n)
#space O(n)


nums = [2,20,4,10,3,4,5]
print(longest_consecutive(nums))

nums = [0,3,2,5,4,6,1,1]
print(longest_consecutive(nums))

nums = []
print(longest_consecutive(nums))

nums = [None,3,2,5,4,6,1,1]
print(longest_consecutive(nums))
