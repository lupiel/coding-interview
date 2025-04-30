# points = [
#     [x, y]
# ]

# distances = [
#     [d, [x, y]]
# ]

import math
import heapq

def k_closest(points, k):
    distances = [[math.sqrt(math.pow(x, 2) + math.pow(y, 2)), [x, y]] for x, y in points]  # O(n)

    heapq.heapify(distances) # O(n)

    ret = []
    for _ in range(k): 
        ret.append(heapq.heappop(distances)[1])
    # O(k logk)

    return ret

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(k_closest(points, k))

points = [[1,3],[-2,2]]
k = 1
print(k_closest(points, k))
points = [[1,1],[3,3],[5,-1],[-2,4],[0,0]]
k = 4
print(k_closest(points, k))
