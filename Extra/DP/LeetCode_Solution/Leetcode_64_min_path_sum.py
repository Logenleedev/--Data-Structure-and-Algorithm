class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]


        # initialization
        sum_1 = 0
        for i in range(len(grid[0])):
            sum_1 += grid[0][i]
            dp[0][i] = sum_1

        sum_2 = 0
        for j in range(len(grid)):
            sum_2 += grid[j][0]
            dp[j][0] = sum_2

        # interation:
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)