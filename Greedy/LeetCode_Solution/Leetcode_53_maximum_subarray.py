class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0

        result = -float("inf")

        for i in range(len(nums)):
            sum += nums[i]
            result = max(sum, result)
            if sum < 0:
                
                sum = 0
            
        return result 
