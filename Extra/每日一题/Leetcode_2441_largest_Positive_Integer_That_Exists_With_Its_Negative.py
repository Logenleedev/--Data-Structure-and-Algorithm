class Solution:
    def findMaxK(self, nums: List[int]) -> int:


        
        max_val = float("-inf")

        for i in range(len(nums)):
            if nums[i] * (-1) in nums:
                max_val = max(max_val, max(nums[i], -1 * nums[i]))

        return max_val if max_val != float("-inf") else -1
            
        
# Time Complexity: O(n)
# Space Complexity: O(1)

