# Method 1: insertion sort 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1

# Method 2: quick sort
class Solution:
    def partition(self, nums, left, right):
        i = left 
        j = right 

        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i], nums[left] = nums[left], nums[i]
        
        return i

    def quicksort(self, nums, left, right):
        if left >= right:
            return 
        
        pivot = self.partition(nums, left, right)
        self.quicksort(nums, left, pivot - 1)
        self.quicksort(nums, pivot + 1, right)
        return nums


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)
        
# Time Complexity: O(n * (log n))
# Space Complexity: O(n)