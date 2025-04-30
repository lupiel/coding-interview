
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float("-inf")

    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(val)
        self.min_val = min(self.min_val, val)

    def pop(self):
        ret = self.stack.pop()
        self.min_val = self.min_stack.pop()
        return ret

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def get_min(self):
        return self.min_val


minStack = MinStack()
minStack.top()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.get_min()) # return 0
print(minStack.pop())
print(minStack.top())     # return 2
print(minStack.get_min()) # return 1
