# My solution

class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Leetcode Official Solution 
import math 
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()