class Solution:
    # [left, right)
    def binary_search(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid 
            else:
                right = mid
        
        return left 

    # [left, right]
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid 
            else:
                right = mid - 1
        
        return left 

    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = self.binary_search(nums, target)
        return ans 