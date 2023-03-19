# Method 1

class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 1
        
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Method 2
class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)

        weight = [1, 2]

        dp[0] = 1

        
        for j in range(n + 1):
            for i in range(len(weight)):
                if j - weight[i] >= 0:
                    dp[j] += dp[j - weight[i]]


        return dp[n]