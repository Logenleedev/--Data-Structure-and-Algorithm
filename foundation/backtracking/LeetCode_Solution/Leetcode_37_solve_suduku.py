class Solution:
    

    def valid(self, row, col, number, board, n):
        # valid row 
        for i in range(n):
            if board[row][i] == str(number):
                return False 

        # valid col 
        for j in range(n):
            if board[j][col] == str(number):
                return False 

        # valid 3 x 3
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == str(number):
                    return False 

        return True 

    def backtracking(self, board, n):

        for row in range(n):
            for col in range(n):
                if board[row][col] != ".":
                    continue 
                for i in range(1, 10):
                    if self.valid(row, col, i, board, n) == True:
                        board[row][col] = str(i)
                        # 如果发现解决完了立刻返回
                        result = self.backtracking(board, n)
                        if result == True:
                            return True 
                        board[row][col] = "."
                # 发现放不了,return false
                return False
        # 遍历到最后说明已经完成了数独
        return True 
                    


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """



        self.backtracking(board, 9)



# Time Complexity: O(9^m) m 是空格数量 但是实际上并不需要这么多 因为我们找到答案就返回了
# Space Complexity: O(m) 