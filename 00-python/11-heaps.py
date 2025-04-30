import heapq

minHeap = [2,3,4]
heapq.heapify(minHeap)      # heapify  O(n)
heapq.heappush(minHeap, -7) # heappush O(log n)
minHeap[0]                  # peak     O(1)
heapq.heappop(minHeap)      # pop      O(log n)



# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, -7)
print(minHeap)
heapq.heappush(minHeap, -8)
print(minHeap)
heapq.heappush(minHeap, 0)
print(minHeap)
heapq.heappush(minHeap, 9)
print(minHeap)
heapq.heappush(minHeap, 4)
print(minHeap)
heapq.heappush(minHeap, 7)
print(minHeap)
heapq.heappush(minHeap, 2)

print(minHeap)
# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

print(minHeap)

arr = [(3, "A"),(5, "B"),(8,"C"),(4,"D"),(7,"E"),(1,"F"),(2,"G")]
heapq.heapify(arr)
print(arr)
while len(arr):
    print(heapq.heappop(arr))



print("---")
# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
print(arr)
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

