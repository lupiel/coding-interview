
# while i < j
    # find mid
    # if nums[mid] == target return mid
    # if nums[mid] > target repeat on left slice
    # if nums[mid] < target repeat on right slice


def find(nums, target):
    print("nums=", nums, ", target=", target)
    i, j = 0, len(nums) - 1

    while i <= j:
        mid = int((i + j) / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
    return -1



arr = [-1, 0, 3, 9, 12, 99]
target = 3
assert find(arr, target) == 2

arr = [-1, 0, 3, 9, 12, 99]
target = 9
assert find(arr, target) == 3

arr = [-1, 0, 3, 9, 12]
target = 3
assert find(arr, target) == 2

arr = [-1, 0, 3, 9, 12]
target = 0
assert find(arr, target) == 1

arr = [-1, 0, 3, 9, 12]
target = 9
assert find(arr, target) == 3

arr = [-1, 0, 3, 9, 12]
target = 8
assert find(arr, target) == -1

arr = [-1, 0, 3, 9, 12]
target = 2
assert find(arr, target) == -1

arr = [-1, 0, 3, 9, 12]
target = 13
assert find(arr, target) == -1

arr = [-1, 0, 3, 9, 12]
target = -5
assert find(arr, target) == -1

