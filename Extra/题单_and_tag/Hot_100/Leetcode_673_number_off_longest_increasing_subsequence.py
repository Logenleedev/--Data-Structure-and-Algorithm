from collections import defaultdict
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i] => max length
        dp = [1] * len(nums)

        # count[i] => max_length_count 
        count = [1] * len(nums)

        for i in range(1, len(dp)):

            for j in range(i):
                if nums[i] > nums[j]:

                    if dp[i] < dp[j] + 1:
                        count[i] = count[j]
                        
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]

                    dp[i] = max(dp[i], dp[j] + 1)


                    

        res = max(dp)
        counter = 0
        for i in range(len(dp)):
            if dp[i] == res:
                counter += count[i]

        return counter
                    
                        
                    # dp[i] => max length
        return res
                
             
                
# Time Complexity: O(n^2)
# Space Complexity: O(n)