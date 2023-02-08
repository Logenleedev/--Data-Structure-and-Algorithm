# Method 1:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pointer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        
        return pointer 

# Method 2:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pointer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        
        return pointer 


# Method 3:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        fast, slow = 1, 1
        while(fast < length):

            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)