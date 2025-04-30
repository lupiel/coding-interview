
# # if open_n == closed_n == n -> append combination
# # if open_n < n -> add "("
# # if open_n > closed_n add ")"


# def generate_brackets(n):

#     res = []

#     def backtrack(open_n, closed_n, stack):
#         if open_n == closed_n == n:
#             res.append("".join(stack))
#             return

#         if open_n < n:
#             print(stack + ["("])
#             backtrack(open_n + 1, closed_n, stack + ["("])

#         if closed_n < open_n:
#             print(stack + [")"])
#             backtrack(open_n, closed_n + 1, stack + [")"])

#     backtrack(0, 0, [])

#     return res

# print(generate_brackets(2))






def generate_brackets(n):
    stack = []
    res = []

    def backtrack(open_n, closed_n):
        if open_n == closed_n == n:
            res.append("".join(stack))
            return

        if open_n < n:
            stack.append("(")
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(")")
            backtrack(open_n, closed_n + 1)
            stack.pop()

    backtrack(0, 0)

    return res

print(generate_brackets(3))