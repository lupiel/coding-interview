#         []
#    [a]      []
#  [ab] [a] [b] [] 


def combination_sum(nums, target):

    result = set()
    tracker = []

    def dfs(total):
        if target < total:
            return
        if target == total:
            result.add(tuple(tracker.copy()))

        for n in nums:
            tracker.append(n)
            dfs(total + n)
            tracker.pop()
            dfs(total + n)

    dfs(0)
    return [list(t) for t in result]

print(combination_sum([1,2,3], 3))

