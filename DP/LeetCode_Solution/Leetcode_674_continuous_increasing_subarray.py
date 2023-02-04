class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        dp = [1] * len(nums)
        

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = max(dp[i - 1] + 1, dp[i])

        return max(dp)