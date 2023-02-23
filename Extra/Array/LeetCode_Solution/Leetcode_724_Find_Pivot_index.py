class Solution:
    def pivotIndex(self, nums: List[int]) -> int:



        total = sum(nums)

        sum_left = 0
        for i in range(len(nums)):
            if total - sum_left - nums[i] == sum_left:
                return i

            sum_left += nums[i]
            
        
        return -1 

# Time Complexity: O(n)
# Space Complexity: O(1)