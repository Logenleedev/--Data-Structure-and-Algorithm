# Method 1: My solution | Double pointer
class Solution:
    def reverse_string(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


    def reverseStr(self, s: str, k: int) -> str:
        nums = list(s)
        for i in range(0, len(s), k * 2):
            nums[i : i + k] = self.reverse_string(nums[i : i + k])
        return "".join(nums)

# Method 2: Carl's solution
class Solution:
    def reverse_string(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


    def reverseStr(self, s: str, k: int) -> str:
        nums = list(s)
        for i in range(0, len(s), k * 2):
            nums[i : i + k] = self.reverse_string(nums[i : i + k])
        return "".join(nums)
        

# Time Complexity: O(n)      
# Space Complexity: O(1)