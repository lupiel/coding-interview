# iterate
# if target-curr found in hahs-map return idx
# else add diff to hash-map

from typing import List

def two_sum(nums: List, target: int) -> List[int]:
    diffs = dict()

    for i, n in enumerate(nums):
        diff = target - n
        if n in diffs.keys():
            return [diffs[n], i]
        else:
            diffs[diff] = i

    return []

    # nums = [2,7,11,15]
    # target = 9
    
    # iteration: 1
    # i = 0
    # n = 2
    # diff = 7
    # diffs = {7:0, }
    # if = False

    # iteration: 2
    # i = 1
    # n = 7
    # if = True
    # diff = 2
    # diffs = {7:0, }



def test():
    nums = [2,7,11,15]
    target = 9
    res = [0,1]
    print(two_sum(nums, target))
    assert two_sum(nums, target) == res

    nums = [3,2,4]
    target = 6
    res = [1,2]
    print(two_sum(nums, target))
    assert two_sum(nums, target) == res

    nums = [45, 99, 66, 200]
    target = 245
    res = [0,3]
    print(two_sum(nums, target))
    assert two_sum(nums, target) == res


test()

# compare each one with all others
# time O(n^2)
# space O(1) 


# run through the array and save values in hash map
# return when condition met
# time O(n)
# space O(n)
