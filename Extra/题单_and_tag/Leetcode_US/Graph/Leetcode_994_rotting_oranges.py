from collections import deque
class Solution:            
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        
        fresh_orange = 0 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # que is used to save the rotting orange
                if grid[r][c] == 2:
                    que.append((r, c))
                # count freshorange number 
                elif grid[r][c] == 1:
                    fresh_orange += 1
                    
        # time ticker 
        que.append((-1, -1))
        # timestamp starts from -1
        minute = -1 
        # direction (left, up, right, down)
        directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]
        
        while que:
            row, col = que.popleft()
            
            # when row == -1, it means we finished scanning one level 
            if row == -1:
                minute += 1
                if que:
                    que.append((-1, -1))
                
            else:
                for d in directions:
                    neighbor_row = row + d[0]
                    neighbor_col = col + d[1]
                    
                    if len(grid) > neighbor_row >= 0 and len(grid[0]) > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_orange -= 1
                            
                            que.append((neighbor_row, neighbor_col))
                            
        return minute if fresh_orange == 0 else -1 
                
# Time Complexity: O((nm)^2)
# Space Complexity: O(nm)