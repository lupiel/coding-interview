from typing import List

def has_duplicates(nums: List[int]) -> bool:
    #TOD handle empty nums

    seen = dict()
    for n in nums:
        x = seen.get(n, 0)
        if x > 0:
            return True
        else:
            seen[n] = x + 1

    return False

def test():
    nums = [1,2,3,1]
    res = True
    assert has_duplicates(nums) == res

    nums = [1,2,3,4]
    res = False
    assert has_duplicates(nums) == res

    nums = []
    False
    assert has_duplicates(nums) == res

if __name__ == "__main__":
    test()


# bruteforce
#compare each cell with every other cell
#time O(n^2)
#space O(1)

# sorting
#sort and run through an array
#time O(n logn)
#space O(1)

# using hashmap to save count of values
#time O(n)
#space O(n)