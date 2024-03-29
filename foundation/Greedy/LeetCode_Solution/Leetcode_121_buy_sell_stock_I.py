
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0

        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)

        return maxprofit

# DP 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        # hold 
        dp[0][0] = -prices[0]

        # not hold
        dp[0][1] = 0


        for i in range(1, len(dp)):
            # the state of holding the stock
            # state transition:
            # 1. in i - 1 th day, we already hold the stock
            # 2. we purchase the stock in i - th day. In i - 1 th day, we don't have the stock 
            dp[i][0] = max(dp[i - 1][0], -prices[i])


            # the state in which we don't have the stock
            # state transition:
            # 1. in i - 1 th day, we already don't hold the stock
            # 2. have the stock in i - 1 th day, and sell it on i th day
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])

        return max(dp[-1][0], dp[-1][1])
        

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 

        cost = float("inf")
        profit = float("-inf")



        for i in range(len(prices)):
            cost = min(prices[i], cost)
            profit = max(prices[i] - cost, profit)


        if profit < 0:
            return 0
        return profit 
        
# Time Complexity: O(n)
# Space Complexity: O(1)

