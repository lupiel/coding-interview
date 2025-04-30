

1 2 3 4 4 .. n+1
n distinct

sum 1...n -> (1 + n)/2*n


1 2 3 -> 6

1 2 3 4 -> (1+4)/2 *4 ->


def find_duplicate(nums):

    max_num = float("-inf")
    nums_sum = 0
    for n in nums:
        max_num = max(max_num, n)
        nums_sum += n

    # sum 1, 2 ..., n
    no_duplicate_sum = ((1 + max_num)/2)*(len(nums) - 1)

    duplicate = nums_sum - no_duplicate_sum
    return duplicate



