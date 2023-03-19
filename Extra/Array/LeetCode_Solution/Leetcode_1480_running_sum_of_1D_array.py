# Method 1:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = 0

        ans = [0] * len(nums)
        for i in range(len(nums)):
            result += nums[i]
            ans[i] = result 


        return ans 






# Time Complexity: O(n)
# Space Complexity: O(n)





# Method 2:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:



        for i in range(1, len(nums)):  
            nums[i] = nums[i] + nums[i - 1]


        return nums



# Time Complexity: O(n)
# Space Complexity :O(1)