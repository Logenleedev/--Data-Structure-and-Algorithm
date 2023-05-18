class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] and its meaning 
            # 以 [i][j] 右下角的的最大边长
        # dp formula 
        # initialization 
        # iteration direction 
        # print(dp)
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = 1 

        for j in range(len(matrix)):
            if matrix[j][0] == '1':
                dp[j][0] = 1 

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
           

        res = 0 

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dp[i][j])

        return res ** 2



# Time Complexity: O(m * n)
# Space Complexity: O(m * n)