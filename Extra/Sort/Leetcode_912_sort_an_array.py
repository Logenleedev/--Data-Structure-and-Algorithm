# Neetcode heap 经典模版题

import heapq
class Solution:


    def sortArray(self, nums: List[int]) -> List[int]:  
        pri_que = []

        for i in range(len(nums)):
            heapq.heappush(pri_que, nums[i])

        ans = []

        while len(pri_que):
            ans.append(heapq.heappop(pri_que))

        return ans
        
# Time Complexity: O(n * log(n))
# Space Complexity: O(1)

