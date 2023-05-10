# Method 1 - Binary Search Algorithm

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (high + low)//2

            if (nums[mid] < target):
                low = mid + 1
            

            if (nums[mid] > target):
                high = mid - 1
            

            if (nums[mid] == target):
                return mid

        return -1

# Time Complexity: Log(n)
# Space Complexity: O(1)