# Method 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:



        total = sum(nums)

        sum_left = 0
        for i in range(len(nums)):
            if total - sum_left - nums[i] == sum_left:
                return i

            sum_left += nums[i]
            
        
        return -1 


# Method 2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0


        left_most = 0
        total = sum(nums)

        for i in range(len(nums)):
            if total - sum(nums[: left_most + 1]) != sum(nums[: left_most]):
                left_most += 1
            else:
                return left_most

        return -1 
# Time Complexity: O(n)
# Space Complexity: O(1)