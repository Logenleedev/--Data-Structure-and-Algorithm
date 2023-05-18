## 岛屿问题模版 
状态：
1. 0 -> 海洋
2. 1 -> 陆地 （没有遍历过）
3. 2 -> 陆地 （遍历过了）

```python 
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
```

## BFS 
```python 3
# [[1,3],[0,2],[1,3],[0,2]]



from collections import deque
def BFS(graph, startIndex):
    
    que = deque([startIndex])
    res = []
    visited = [False] * len(graph)
    
    while len(que) > 0:
        element = que.popleft()
        
        # 看看之前见没见过
        if visited[element] == True:
                continue 
            
        # 没有见过
        res.append(element)
        visited[element] = True
        
        # 附加neighbor
        for v in graph[element]:
            que.append(v)
            
    return res 
```