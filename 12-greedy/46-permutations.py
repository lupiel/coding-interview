# [0,1]

#       []
#    [0]  [1]
#   [01]  [10]

# [a,b,c]

#                []
#         a       b       c
#        b c     a c     a b
#        c b     c a     b a

def permutations(nums):
    n_ = len(nums)
    res, walker = [], []

    def backtrack():
        if len(walker) == n_:
            res.append(walker.copy())
            return
        
        for n in nums:
            if n not in walker:
                walker.append(n)
                backtrack()
                walker.pop()

    backtrack()
    return res

print(permutations([1,2,3]))