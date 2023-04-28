class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp five steps
        # 1. dp[i] meaning 
            # (, i] max product
            # [0]: 当前的最大
            # [1]: 当前的最小
        # 2. dp formula 
            # dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i], dp[i - 1][1] * nums[i])
            # 第 i 个位置最大的有三种情况
                # 1. dp[i - 1][0] * nums[i] -> 和最大子序列和一个道理
                # 2. nums[i] ->  和最大子序列和一个道理
                # 3. !!!!!! dp[i - 1][1] * nums[i] -> 最小的 * num 比如 -3 * -2 = 6
            # 第 i 个位置最小的有三种情况
                # 1. dp[i - 1][0] * nums[i] -> 和最大子序列和一个道理
                # 2. nums[i] ->  和最大子序列和一个道理
                # 3. !!!!!! dp[i - 1][0] * nums[i] -> 最大的 * num 比如100 * -1 = -100

            # dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i], dp[i - 1][0] * nums[i])
        # 3. dp initialization 
        # 4. dp iteration: from front to back 
        # 5. print(dp) / debug


        dp = [[0 for _ in range(2)] for _ in range(len(nums))]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]


        for i in range(1, len(nums)):

            dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i], dp[i - 1][0] * nums[i])
        
        res = float("-inf")
        for i in range(len(nums)):
            res = max(res, max(dp[i]))

        return res if res != float("-inf") else 0 


# Time Complexity: O(n * 2)
# Space Complexity: O(n * 2)