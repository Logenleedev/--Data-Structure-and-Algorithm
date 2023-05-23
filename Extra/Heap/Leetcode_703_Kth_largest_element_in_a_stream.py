import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.pri_que = []

        # 都存下来
        for i in nums:
            heapq.heappush(self.pri_que, i)



    def add(self, val: int) -> int:
        heapq.heappush(self.pri_que, val)
        
        # 弹出去
        while len(self.pri_que) > self.k:
            heapq.heappop(self.pri_que)

        return self.pri_que[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# O(n * log(n))
# O(k)