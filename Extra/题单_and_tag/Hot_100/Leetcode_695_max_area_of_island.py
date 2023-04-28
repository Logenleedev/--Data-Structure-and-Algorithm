# Recursion 1: no return value 
class Solution:
    def __init__(self):
        self.area = 0

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            return 
        
        if grid[i][j] != 1:
            return 

        self.area += 1
        grid[i][j] = 2 

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.area = 0
                    self.dfs(grid, i, j)
                    result = max(self.area, result)

        return result

# Recursion 2: with return value 
class Solution:
    def __init__(self):
        self.area = 0

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        
        if grid[i][j] != 1:
            return 0

        num = 1
        grid[i][j] = 2 

        num += self.dfs(grid, i + 1, j)
        num += self.dfs(grid, i - 1, j)
        num += self.dfs(grid, i, j - 1)
        num += self.dfs(grid, i, j + 1)
        return num 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.area = max(self.dfs(grid, i, j), self.area)


        return self.area

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)