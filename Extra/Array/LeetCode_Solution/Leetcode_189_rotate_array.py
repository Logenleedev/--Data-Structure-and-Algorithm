# Method 1: 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # corner case 
        if len(nums) == 0:
            return []

        test = nums[:]

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = test[i]


        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)




# Method 2: 整体翻转 + 局部反转

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先整体 再局部

        # corner case 
        if len(nums) == 0:
            return []

        ref = k % len(nums)

        nums[:] = nums[::-1]
        nums[:ref] = reversed(nums[:ref])
        nums[ref:] = reversed(nums[ref:])
        return nums
