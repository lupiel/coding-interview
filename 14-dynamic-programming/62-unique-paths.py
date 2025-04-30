# R.....
# ......
# .....F


# m x n
# 3 x 6

# R11111
# 123456
# 13605F

def unique_paths(rows, cols):
    prev_row = [0] * cols
    curr_row = [0] * cols

    for r in range(rows):
        for c in range(cols):

            # above
            if r > 0:
                above = prev_row[c]
            else:
                above = 0

            # left
            if c > 0:
                left = curr_row[c-1]
            else:
                left = 0
            print(r, c, above+left)
            curr_row[c] = max(above + left, 1)

        prev_row = curr_row
        curr_row = [0] * cols

    return prev_row[-1]

print(unique_paths(3, 6))