class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        # index and its meaning 
        # i => amount, dp[i] => # of combo
        
        # initialization 
        dp[0] = 1
        # dp relation:
        # dp[j] += dp[j - coins[i]]

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]


        return dp[amount]


# Time Complexity: O(n * amount)
# Space Complexity: O(amount)