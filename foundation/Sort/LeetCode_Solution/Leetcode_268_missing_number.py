
# Brute force. First sort the array then find the missing number 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            base = nums[i]

            j = i - 1

            while j >= 0 and nums[j] > base:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = base
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i 

        return len(nums)

# Method 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)

# Method 3: Python hashing set
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i

# Method 4: Math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        arrSum = sum(nums)
        return total - arrSum


    