class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1. dp[i] and meaning
        # 2. dp formula
        # 3. initialization 
        # 4. iteration direction 
        # 5. print dp 

        nums = [1] + nums + [1]

        # step 1: store[i] mean max score on (i, j)
        store = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # open interval (i, j)
        def findmax(nums, i, j):
            m = 0 
            for k in range(i + 1, j):
                left = store[i][k]
                right = store[k][j]

                res = left + right + nums[k] * nums[i] * nums[j]
                m = max(m, res)

            store[i][j] = m

        
        for i in range(2, len(nums)):
            for j in range(0, len(nums) - i):
                findmax(nums, j, j + i)

        return store[0][len(nums) - 1]


# Time Complexity: O(n^3)
# Space Complexity: O(n^2)