# [
#     [0,1,2,3],
#     [4,5,6,7]
# ]
# [
#     [1,2,3,4],[5,6,7,8]
# ]



def search(matrix, target):
    m, n = len(matrix), len(matrix[0])
    L, R = 0, m*n-1

    def get_val(x):
        i = x // n
        j = x % n
        return matrix[i][j]
    
    while L < R:
        M = (L+R) // 2
        
        if get_val(M) == target:
            return get_val(M)
        elif get_val(M) < target:
            L = M + 1
        else:
            R = M - 1

    return None

matrix = [
    [0,1,2,3],
    [4,5,6,7]
]

print(search(matrix, 5))
