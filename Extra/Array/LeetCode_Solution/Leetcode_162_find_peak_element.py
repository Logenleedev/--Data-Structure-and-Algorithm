
# Brute Force
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        start = 0 
        
        arr = nums 
        if len(arr) == 1:
            return 0 
        if sorted(arr) == nums:
            return len(arr) - 1

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                start = i - 1
                break


        return start 

# Time Complexity: O(n)
# Space Complexity: O(1)