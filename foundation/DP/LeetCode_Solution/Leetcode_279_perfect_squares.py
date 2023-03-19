class Solution:
    def numSquares(self, n: int) -> int:
    
        dp = [float("inf")] * (n + 1)

        weight = []

        for i in range(1, n + 1):
            if i * i <= n:
                weight.append(i * i)

        dp[0] = 0

        for i in range(len(weight)):
            for j in range(weight[i], n + 1):
                dp[j] = min(dp[j - weight[i]] + 1, dp[j])


        return dp[n] 