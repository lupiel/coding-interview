# import math
# piles = [30,11,23,4,20]
# h = 6

# # k = [1  2  3  4  5  6  7  8  9  10         23  24  25     30]
# # ti  [88 45 31 23 19 16 15 13 13 11   ...   7   6   6  ... 5 ]
# #      i                                                    j                                    

# # k = [1  2  3  4  5  6  7  8  9  10         23  24  25     30]
# # ti  [88 45 31 23 19 16 15 13 13 11   ...   7   6   6  ... 5 ]
# #      i                          m                         j   

# # k = [1  2  3  4  5  6  7  8  9  10         23  24  25     30]
# # ti  [88 45 31 23 19 16 15 13 13 11   ...   7   6   6  ... 5 ]
# #                                    i                      j   

# # k = [1  2  3  4  5  6  7  8  9  10         23  24  25  29 30]
# # ti  [88 45 31 23 19 16 15 13 13 11   ...   7   6   6   5  5 ]
# #                                    i                   m  j   

# # k = [1  2  3  4  5  6  7  8  9  10         23  24  25  29 30]
# # ti  [88 45 31 23 19 16 15 13 13 11   ...   7   6   6   5  5 ]
# #                                    i                   m  j  


# h = 33
# # speed       = [1  2  3  4  5  6  7  8  9  10  11  12]
# # time_to_eat = [99 88 77 66 55 44 33 33 33 22  22  11]
# #                i              m                   j
# time_to_eat > h: go right

# # speed       = [1  2  3  4  5  6  7  8  9  10  11  12]
# # time_to_eat = [99 88 77 66 55 44 33 33 33 22  22  11]
# #                                  i         m       j
# time_to_eat <= h: go left

# # speed       = [1  2  3  4  5  6  7  8  9  10  11  12]
# # time_to_eat = [99 88 77 66 55 44 33 33 33 22  22  11]
# #                                  i  m  j         
# time_to_eat <= h: go left

# # speed       = [1  2  3  4  5  6  7  8  9  10  11  12]
# # time_to_eat = [99 88 77 66 55 44 33 33 33 22  22  11]
# #                                  imj      
# time_to_eat <= h: go left


# # speed       = [1  2  3  4  5  6  7  8  9  10  11  12]
# # time_to_eat = [99 88 77 66 55 44 33 33 33 22  22  11]
# #                               j  i      
# j<i end loop

# for i in range(1,max(piles)+1):
#     print([sum([math.ceil(p/i) for p in piles])])



import math

def find_eating_speed(piles, h):
    n = len(piles)
    if h < n:
        return -1


    max_pile = max(piles)
    # speed range [1; max(piles)]
    i, j = 1, max_pile
    ret = max_pile

    while i <= j:

        mid = int((i + j) / 2)
        mid_hours = sum([math.ceil(p/mid) for p in piles])
        print("mid", mid, "mid_hours", mid_hours)

        if mid_hours <= h:
            ret = min(ret, mid)
            j = mid - 1
        else:
            i = mid + 1

    return ret


print(find_eating_speed([3,6,7,11], 8))
print(find_eating_speed([30,11,23,4,20], 5))
print(find_eating_speed([30,11,23,4,20], 6))
print(find_eating_speed([30,11,23,4,20], 60))
print(find_eating_speed([30,11,23,4,20], 600))