# def k_top_frequent(nums, k):
#     occurences = {}
#     for n in nums:
#         occurences[n] = 1 + occurences.get(n, 0)

#     freq = [[] for i in range(len(nums)+1)]

#     for num, cnt in occurences.items():
#         freq[cnt].append(num)

#     ret = []
#     found_cnt = 0
#     for i in range(len(freq)-1, 0, -1):
#         for num in freq[i]:
#             found_cnt += 1
#             ret.append(num)

#             if found_cnt == k:
#                 return ret
    
#     return []

import heapq

def k_top_frequent(nums, k):
    print("nums", nums)

    # hashmap num, count
    count_hashmap = {}
    for n in nums:
        count_hashmap[n] = 1 + count_hashmap.get(n, 0)

    # heapify (count, num) min-heap
    heap = [(c, n) for n, c in count_hashmap.items()]
    print("array", heap)
    heapq.heapify(heap)
    print("heap", heap)
    
    # pop k times
    res = []
    k_cnt = 0
    for (c, n) in heap:
        res.append(n)
        k_cnt =+ 1
        if k_cnt == k:
            break

    return res


nums = [3,3,1,1,2,2] 
k = 2
print(k_top_frequent(nums, k))
# [1, 2]

nums = [3,3,1,1,2,2] 
k = 4
print(k_top_frequent(nums, k))
# [1, 2]

nums = [1,1,1,2,2,3] 
k = 2
print(k_top_frequent(nums, k))
# [1, 2]

nums = [1]
k = 1
print(k_top_frequent(nums, k))
# [1]

nums = [1]
k = 2
print(k_top_frequent(nums, k))
# []

nums = []
k = 3
print(k_top_frequent(nums, k))
# []

nums = [1,2,3]
k = 1
print(k_top_frequent(nums, k))
# []



# solution
# save occurences in a hashmap
# sort by occurences
# return top k