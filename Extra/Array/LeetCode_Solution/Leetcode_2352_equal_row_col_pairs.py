'''
思路：直接模拟
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        col_pair = []

        for i in range(len(grid[0])):
            ans = []
            for j in range(len(grid)):
                ans.append(grid[j][i])
            col_pair.append(ans)

        c = 0

        for i in range(len(grid)):
            if grid[i] in col_pair:
                c += col_pair.count(grid[i])

        return c

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)