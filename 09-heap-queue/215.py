nums = [3,4,5,6,6,2,3,1]
k=2
answer = 6

import heapq
def get_k_largest(nums, k):
    min_heap = [ -n for n in nums]
    heapq.heapify(min_heap)

    k_largest = 0
    for _ in range(k):
        k_largest = -heapq.heappop(min_heap)

    return k_largest

print(get_k_largest(nums, k))
print(get_k_largest(nums, 1))
print(get_k_largest(nums, 3))