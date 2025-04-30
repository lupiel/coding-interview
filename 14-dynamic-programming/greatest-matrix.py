def max_square_size(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    prev_max_square_cache = [0] * COLS
    prev_ones_up_cache = [0] * COLS

    curr_max_square_cache = [0] * COLS
    curr_ones_up_cache = [0] * COLS
    curr_ones_left_cache = [0] * COLS

    global_max_square = 0

    def ones_up(r, c):
        if r > 0:
            prev_ones_up_cache[r] = prev_ones_up_cache[r-1] + 1
            return prev_ones_up_cache[r]

        count = 0
        for y in range(r, -1, -1):
            if matrix[y][c] == 1:
                count += 1

        prev_ones_up_cache[r] = count
        return count

    def ones_left(r, c):
        if c > 0:
            curr_ones_left_cache[c] = curr_ones_left_cache[c-1] + 1
            return curr_ones_left_cache[c]

        count = 0
        for x in range(c, -1, -1):
            if matrix[r][x] == 1:
                count += 1

        curr_ones_left_cache[c] = count
        return count

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 1:
                curr_square = min(
                    1 + prev_max_square_cache[c-1],
                    ones_up(r, c),
                    ones_left(r, c)
                )
                prev_max_square_cache[c] = curr_square
                global_max_square = max(global_max_square, curr_square)
            # else:
            #     max_square_cache[(r, c)] = 0
        
        prev_max_square_cache = curr_max_square_cache
        prev_ones_up_cache = curr_ones_up_cache
        curr_max_square_cache = [0] * COLS
        curr_ones_left_cache = [0] * COLS

    return global_max_square

matrix = [
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
]
print(max_square_size(matrix))
