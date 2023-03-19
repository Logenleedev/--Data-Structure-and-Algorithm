
# Time Complexity O(n)
# Space complexity O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        
        pointer = 0

        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
