class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for str_char in strs:

            x = str_char.count("0")
            y = str_char.count("1")

            for j in range(n, y - 1, -1):
                for i in range(m, x - 1, -1):
                    dp[i][j] = max(dp[i - x][j - y] + 1, dp[i][j])

        return dp[m][n]