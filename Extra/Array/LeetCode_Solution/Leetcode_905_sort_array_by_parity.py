class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        pointer = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 :
                # in which case we find odd integer 
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1

        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)