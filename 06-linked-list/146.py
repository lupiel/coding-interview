from collections import deque, defaultdict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.usage = defaultdict(int)
        self.d = defaultdict(deque)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.d[key]:
            self.usage[key] -= 1
            return self.d[key].pop()
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.usage[key] += 1
        self.d[key].append(value)

        if self.usage[key] > self.capacity:
            self.usage[key] -= 1
            self.d[key].popleft()

        print("key", key, "first/last", self.d[key][0], self.d[key][-1])    
        


lRUCache = LRUCache(2)
lRUCache.put(1, 10)    # cache: {1=10}
print(lRUCache.get(1))        # return 10
lRUCache.put(2, 20)    # cache: {1=10, 2=20}
lRUCache.put(2, 30)    # cache: {1=10, 2=20}
lRUCache.put(2, 40)    # cache: {1=10, 2=20}
lRUCache.put(3, 50)    # cache: {2=20, 3=30}, key=1 was evicted
print(lRUCache.get(2))        # returns 20 
print(lRUCache.get(1))        # return -1 (not found)