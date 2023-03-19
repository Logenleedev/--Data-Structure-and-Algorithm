class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]

        result  = float("-inf")
        for j in range(1, len(nums2) + 1):
            for i in range(1, len(nums1) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i - 1], dp[j][i - 1], dp[j - 1][i])


            result = max(result, max(dp[j]))
        return result 

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)