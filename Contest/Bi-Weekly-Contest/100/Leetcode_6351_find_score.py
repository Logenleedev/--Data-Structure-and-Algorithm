class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = sorted(enumerate(nums), key = lambda x: x[1])

        a = [False] * (len(nums) + 2)

        result = 0

        for i, item in nums:
            if a[i] == False:
                result += item 
                a[i] = True 
                a[i - 1] = True 
                a[i + 1] = True 
            
        return result 
        
# Time Complexity: O(n)
# Space Complexity: O(n)