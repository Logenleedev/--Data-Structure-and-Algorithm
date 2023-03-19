class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = prices[0]
        result = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            elif prices[i] > min_price + fee:
                result += prices[i] - min_price - fee
                min_price = prices[i] - fee
            else:
                continue
        
        return result 