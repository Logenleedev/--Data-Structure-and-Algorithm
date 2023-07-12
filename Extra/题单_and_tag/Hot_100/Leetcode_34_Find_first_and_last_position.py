# 思路：
# 最后的分类讨论要 discuss corner cases
# 注意其实只要围绕着 start 讨论就可以了
# 两种情况
# 1. start 越界
# 2. nums[start] 根本就不是target


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

