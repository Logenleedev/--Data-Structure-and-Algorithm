# Time Complexity: O(n)



from collections import deque

class myQue():
    def __init__(self):
        self.que = deque()
    
    def pop(self, value):
        if len(self.que) != 0 and value == self.que[0]:
            self.que.popleft()
    
    def push(self, value):
        while len(self.que) != 0 and value > self.que[-1]:
            self.que.pop()
        self.que.append(value)
        
    def front(self):
        if len(self.que) != 0:
            return self.que[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        que = myQue()

        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        
        return result

# Time Complexity: O(n)
# Space Complexity: O(k)

