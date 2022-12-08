# Method 1 Brute force | Time out error since time complexity is O(n^2)
# First square each element then run a shorting algorithm

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final_list = [i**2 for i in nums]
        n = len(final_list)

        for i in range(n-1):
            for j in range(n-i-1):
                if final_list[j] > final_list[j+1]:
                    final_list[j], final_list[j+1] = final_list[j+1], final_list[j]
        return final_list

# Method 2 | Double pointer 
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)

        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while i <= j:
            if nums[j]**2 > nums[i]**2:
                ans[k] = nums[j]**2
                k -= 1
                j -= 1
            else:
                ans[k] = nums[i]**2
                k -= 1
                i += 1
        return ans


