class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        nums = sorted(nums)

        dp[0] = 1

        # 先遍历包 再遍历物品
        for j in range(target + 1):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]

        return dp[target]