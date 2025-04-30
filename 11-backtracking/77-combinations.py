# n chose k


#   n!
# --------
# (n-k)!k!

# n = a b c
# k = 2

#                    []
#          [a]       [b]      [c]
#     [ab][ac]    [ba][bc]  [ca][cb]


#                     []                    a
#             []               [a]          b
#                  [b]    [a]      [ab]     c
#                   [bc]    [ac]            


def n_choose_k(n, k):
    ret, sol = [], []

    def backtrack(x):
        # if 2 elements then add sol to ret
        if len(sol) == k:
            ret.append(sol.copy())
            return

        sol.append(x)
        backtrack(x-1)
        sol.pop()

        # if still possible to construct k-size solution
        if k < x + len(sol):
            backtrack(x-1)

    backtrack(n)
    return ret

print(n_choose_k(4, 2))
# print(n_choose_k(60, 13))