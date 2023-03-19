class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums = sorted(nums)


        i = 0


        for num in nums:
            if num > nums[i]:
                i += 1
        
        return i 

# Time Complexity: O(n)
# Space Complexity: O(1)