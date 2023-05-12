class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)

        dp[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):

            # two states:
            # 1. 
            # 2. 
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < len(questions):
                dp[i] += dp[i + skip + 1]
            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]

# Time Complexity: O(n)
# Space Complexity: O(n)
