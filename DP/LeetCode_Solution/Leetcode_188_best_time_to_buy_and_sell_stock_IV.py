class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:


        # Corner case
        if len(prices) == 0:
            return 0

        if len(prices) == 1:
            return 0




        # dp table

        dp = [[0 for _ in range(2 * k + 1)] for _ in range(len(prices))] 

        # 初始化

        for i in range(2 * k + 1):
            if (i % 2) == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = -prices[0]

        # 遍历：先遍历i

        for i in range(1, len(prices)):

            for j in range(1, 2 * k + 1):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
            


        return dp[len(prices) - 1][2 * k]

