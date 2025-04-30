def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


A = [-3, -1, 0, 1, 4, 7]
#traditional
def traditional_binary_serarch(nums, target):
    L, R = 0, len(nums) - 1

    while L <= R:
        M = (L + R) // 2

        if nums[M] == target:
            return True
        elif target < nums[M]:
            R = M - 1
        else:
            L = M + 1

    return False
print(traditional_binary_serarch(A, -10))

# condition based
B = [False,False,False,False,True]
#                             ^
#                              L    M    R
def condition_binary_search(nums):
    print(nums)
    L, R = 0, len(nums) - 1

    while L < R:
        M = (L+R) // 2

        if nums[M] == True:
            R = M
        else:
            L = M + 1
        print("(L,M,R)=" + f"({L},{M},{R})")

    return L

print(condition_binary_search(B))
