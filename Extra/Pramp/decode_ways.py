class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[0] = 1

        for i in range(1, len(dp)):
            # e.g. 2[3]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # e.g. 23[4]
            if i >= 2:
                if 10 <= int(s[i - 2: i]) <= 26:
                    dp[i] += dp[i - 2]

        return dp[-1]

# dp index and its meaning: [:i] has dp[i] ways to decode the string
# dp[0] = 1 -> from definition ; required for dp equation
# iteration direction -> 正向
# dp[i] = dp[i - 1] + dp[i - 2]
# print dp and check 