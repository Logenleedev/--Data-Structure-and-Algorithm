


# 思路
# 1. 从右往左找到第一个递减元素
# 2. 记录 as modify 
# 3. 从右往左找到第一个比 nums[modify] 大的元素
# 4. swap 这两个element
# 5. 把 modify + 1 到最后的所有 element 全部交换顺序



class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n <= 1:
            return 

        modify = -1 

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                modify = i 
                break
        
        if modify == -1:
            nums[:] = nums[::-1]

        else:
            target = -1 

            for i in range(n - 1, modify, -1):
                if nums[i] > nums[modify]:
                    target = i 
                    break 

            nums[target], nums[modify] = nums[modify], nums[target]

            i, j = modify + 1, n - 1
            # [left, right]

            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            

   
# Time Complexity: O(n)
# Space Complexity: O(1)