class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ref = sorted(nums)
        if ref == nums:
            return 0 

        left = 0 
        right = len(nums) - 1


        while left <= right:
            if nums[left] == ref[left]:
                left += 1
            
            if nums[right] == ref[right]:
                right -= 1
            
            if nums[left] != ref[left] and nums[right] != ref[right]:
                break

        return right - left + 1
# Time Complexity: O(n) 
# Space Complexity: O(n)