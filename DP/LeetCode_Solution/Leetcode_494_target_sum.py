class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 != 0:
            return 0
        if sum(nums) < abs(target):
            return 0

        
        bag_size = int((sum(nums) + target) / 2)

        dp = [0] * (bag_size + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[bag_size]