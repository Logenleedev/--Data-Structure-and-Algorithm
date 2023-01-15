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