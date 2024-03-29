class Solution:
    def traversal(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            return 
        elif grid[i][j] == "2" or grid[i][j] == "0":
            return 

        grid[i][j] = "2"
        self.traversal(grid, i - 1, j) # up
        self.traversal(grid, i + 1, j) # down
        self.traversal(grid, i, j - 1) # left 
        self.traversal(grid, i, j + 1) # right 

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.traversal(grid, i, j)

        return res

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)