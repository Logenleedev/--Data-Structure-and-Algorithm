# DP method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = [0] * len(prices)

        counter = len(res) - 1
        for i in range(len(prices) - 1, 0, -1):
            res[counter] = prices[i] - prices[i - 1]
            counter -= 1
        
        result = 0

        for ele in res:
            if ele > 0:
                result += ele
        
        return result 

# Time Complexity: O(n)
# Space Complexity: O(n)

# DP method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            # the state of holding the stock
            # state transition:
            # 1. in i - 1 th day, we already hold the stock
            # 2. we purchase the stock in i - th day. In i - 1 th day, we don't have the stock 
            dp[i][0] = max(dp[i - 1][0] , dp[i - 1][1]-prices[i])

            # the state in which we don't have the stock
            # state transition:
            # 1. in i - 1 th day, we already don't hold the stock
            # 2. have the stock in i - 1 th day, and sell it on i th day
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return max(dp[-1][0], dp[-1][1])