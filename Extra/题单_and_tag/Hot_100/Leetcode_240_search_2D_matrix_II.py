# 缩减搜索方法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1

        while matrix[i][j] != target:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True 
            if i >= len(matrix) or j < 0:
                return False 

        return True 