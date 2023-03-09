class Solution:
    def rob_list(self, num):
        dp = [0] * len(num)
        dp[0] = num[0]
        dp[1] = max(num[0], num[1])

        for i in range(2, len(num)):
            dp[i] = max(dp[i - 2] + num[i], dp[i - 1])


        return dp[len(num) - 1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        val1 = self.rob_list(nums[1:])
        val2 = self.rob_list(nums[:-1])

        return max(val1, val2)


# Time Complexity: O(n)
# Space Complexity: O(n)