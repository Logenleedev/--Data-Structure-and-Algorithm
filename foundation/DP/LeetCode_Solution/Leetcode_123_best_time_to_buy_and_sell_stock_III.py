class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        if len(prices) == 1:
            return 0

        dp = [[0 for _ in range(5)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0


        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        # print(dp)

        return dp[len(prices) - 1][4]



# Time Complexity: O(n)
# Space Complexity: O(n)