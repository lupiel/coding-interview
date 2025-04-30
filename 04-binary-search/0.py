# find row using binary search
    # if found row - find number in a row using binary search
        # if found number return true
        # else return false
    # else return False


# def find(matrix, target):

#     for row in matrix:
#         for cell in row:
#             if cell == target:
#                 return True
#     return False

# def find(matrix, target):

#     for row in matrix:
#         # binary search in row
#         i, j = 0, len(row) - 1
#         while i <= j:
#             mid = int((i + j)/2)
#             if row[mid] == target:
#                 return True
#             if row[mid] < target:
#                 i = mid + 1
#             if row[mid] > target:
#                 j = mid - 1
#     return False

def find(matrix, target):

    a, b = 0, len(matrix) - 1
    while a <= b:
        matrix_mid = int((a + b) / 2)
        mid_row = matrix[matrix_mid]
        if target >= mid_row[0] and target <= matrix[matrix_mid][-1]:
            # binary search in row
            i, j = 0, len(mid_row) - 1
            while i <= j:
                mid = int((i + j)/2)
                if mid_row[mid] == target:
                    return True
                if mid_row[mid] < target:
                    i = mid + 1
                if mid_row[mid] > target:
                    j = mid - 1
        #go left
        if mid_row[0] > target:
            b = matrix_mid - 1
        #go right
        if mid_row[-1] < target:
            a= matrix_mid + 1

    return False


m = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

print(find(m, 10))
print(find(m, 13))
print(find(m, 11))
print(find(m, 1))
print(find(m, 8))
print(find(m, 14))
print(find(m, 40))



print(find(m, 50))
print(find(m, -1))
print(find(m, 9))

