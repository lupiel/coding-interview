#         []
#    [a]      []
#  [ab] [a] [b] [] 


def subsets(nums):

    result = []
    tracker = []

    def dfs(i):
        if i >= len(nums):
            result.append(tracker.copy())
            return
        
        tracker.append(nums[i])
        dfs(i+1)
        tracker.pop()
        dfs(i+1)

    dfs(0)
    return result

print(subsets(["a","b","c"]))
print(subsets([1,2,3]))




#         []
#    [a]      []
#  [ab] [a] [b] [] 


