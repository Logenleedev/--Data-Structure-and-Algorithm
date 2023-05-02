class Solution:
    # [left, right)
    def lower(self, nums, target):
        i = 0 
        j = len(nums)
        
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid 

        return i
    # [left, right]
    def lower(self, nums, target):
        i = 0 
        j = len(nums) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return i

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = self.lower(nums, target + 1) - 1
        return [start, end]

# Time Complexity: O(log(n))
# Space Complexity: O(1)