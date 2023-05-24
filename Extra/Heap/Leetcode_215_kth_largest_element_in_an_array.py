# heap 

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pri_que = []
        

        for num in nums:
            heapq.heappush(pri_que, num)
            if len(pri_que) > k:
                heapq.heappop(pri_que)


        return pri_que[0]

# Time Complexity: O(n log (k))
# Space Complexity: O(k)

# sort 


class Solution:
    
    def pivote(self, nums, i, j):
        left = i 
        
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1

            while i < j and nums[i] <= nums[left]:
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]

        return i 

    def partition(self, nums, left, right):
        if left >= right:
            return 

        pivote = self.pivote(nums, left, right)

        self.partition(nums, left, pivote - 1)
        self.partition(nums, pivote + 1, right)

    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.partition(nums, 0, len(nums) - 1)

        return nums[-k]
     
# Time Complexity: O(n log(n))
# Space Complexity: O(k)