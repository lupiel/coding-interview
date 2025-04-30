# maximum subarray

nums = [1,-2,2,4,-7,1,8,-2,4]

def max_sum(nums):

    i, j = 0, 0
    max_sum = 0
    window_sum = 0

    while j < len(nums):
        window_sum += nums[j]

        if window_sum < 0:
            i = j + 1
            j = j + 1
            window_sum = 0
        
        max_sum = max(max_sum, window_sum)
        j += 1

    return max_sum

