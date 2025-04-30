import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)             # O(n)
        while len(self.min_heap) > k:            # O(n)
            heapq.heappop(self.min_heap)

    # Time: O(n), Space: O(n)

    def add(self, val):
        heapq.heappush(self.min_heap, val) # O(log k)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)   # O(log k)
        return self.min_heap[0]            # O(1)

    # Time: O(log k), Space: O(1)


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.min_heap)
print(kthLargest.add(3))     # return 4
print(kthLargest.min_heap)
print(kthLargest.add(5))     # return 5
print(kthLargest.min_heap)
print(kthLargest.add(10))     # return 5
print(kthLargest.min_heap)
print(kthLargest.add(9))     # return 8
print(kthLargest.min_heap)
print(kthLargest.add(4))     # return 8
