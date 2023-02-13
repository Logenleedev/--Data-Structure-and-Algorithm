class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 0
        dp[2] = 1


        for i in range(3, n + 1):
            # 下面的这个 for loop 的 upper bound 可以优化为 n // 2 + 1
            for j in range(1, n):

                dp[i] = max(j * (i - j), j * dp[i - j], dp[i])

        return dp[n]

# Time Complexity: O(n^2)
# Space Complexity: O(n)