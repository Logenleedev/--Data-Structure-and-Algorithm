class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for j in range(len(s) + 1):
            for word in wordDict:
                if j >= len(word):
                    print(dp[j - len(word)] and word == s[j - len(word): j])
                    dp[j] =  dp[j] or (dp[j - len(word)] and word == s[j - len(word): j])
        return dp[len(s)]
