#   3 4 5 6 7 8 8 8 9 9
#   3 4 5 6 7 8 8 8
#   3 4 5 6 7 8
#   1 3 4 5 6
#   1 1 3 4
#   1 1 1
#   1

import heapq

def wight_of_last_stone(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)          #O(n)

    while len(stones) >= 2:        #O(n)
        y = -heapq.heappop(stones) #O(log n)
        x = -heapq.heappop(stones) #O(log n)

        print("fight", y, x)        
        clash = y - x
        print("result", clash)

        if clash:
            heapq.heappush(stones, -clash) #O(log n)

    return 0 if not stones else -stones[0]
# Time: nlog(n)    

print(wight_of_last_stone([2,7,4,1,8,1]))
print(wight_of_last_stone([3,4,8,8,9,9,5,6,8,8,9,9,7,8]))