class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        m = len(matrix)
        n = len(matrix[0])

        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]

        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j - 1 >= 0 and j + 1 < n:
                    # didn't cross the boundary 
                    dp[i][j] = min(dp[i - 1][j - 1] + matrix[i][j], dp[i - 1][j] + matrix[i][j], dp[i - 1][j + 1] + matrix[i][j])
                elif j - 1 < 0:
                    dp[i][j] = min(dp[i - 1][j] + matrix[i][j], dp[i - 1][j + 1] + matrix[i][j])
                elif j + 1 >= n:
                    dp[i][j] = min(dp[i - 1][j - 1] + matrix[i][j], dp[i - 1][j] + matrix[i][j])

        return min(dp[-1])

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)