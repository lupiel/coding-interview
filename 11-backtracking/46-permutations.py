# nums = [1,2,3]
# answer = [[123],[132],[213],[231],[312],[321]]

# nums = ["a", "b", "c"]

#            []
#     a       b        c
# ab    ac  ba bc     ca cb
#abc   acb bac bca   cab cba


def permutations(nums):
    ans, sol = [], []


    def dfs():
        if len(sol) == len(nums):
            ans.append(sol.copy())
            return

        for num in nums:
            if num not in sol:
                sol.append(num)
                dfs()
                sol.pop()

    dfs()
    return ans

print(permutations(["a","b","c"]))