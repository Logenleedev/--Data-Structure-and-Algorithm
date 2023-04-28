# 周长有两种 state:
# 1. 边界导致的
# 2. 海洋导致的

# 所以思路是直接在 base case 里面改

class Solution:
    def __init__(self):
        self.perimeter = 0 
    
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            self.perimeter += 1
            return 
        elif grid[i][j] == 0:
            self.perimeter += 1
            return 
        elif grid[i][j] == 2:
            return 


        grid[i][j] = 2
     

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)

        return self.perimeter

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)