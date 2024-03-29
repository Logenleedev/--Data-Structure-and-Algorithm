class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 01 knackpack problem 
        # first iterate through the items
        for str_char in strs:

            x = str_char.count("0")
            y = str_char.count("1")

            # then iterate through the bag 
            for j in range(n, y - 1, -1):
                for i in range(m, x - 1, -1):

                    # notice the value of the item here is 1 since we only interested in the 
                    # length of the element
                    dp[i][j] = max(dp[i - x][j - y] + 1, dp[i][j])

        return dp[m][n]

# l -> length of strs
# Time Complexity: O(mnl)
# Space Complexity: O(mn)