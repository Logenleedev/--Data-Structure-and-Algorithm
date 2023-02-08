class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
     
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if (j - i) == 0:
                    
                        dp[i][j] = 1
                    elif  j - i == 1:
                        dp[i][j] = 2
              

                    else:
                        
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] =  max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][len(s) - 1]