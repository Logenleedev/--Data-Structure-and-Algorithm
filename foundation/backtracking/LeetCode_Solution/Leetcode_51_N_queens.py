





class Solution:
    def __init(self):
        self.chessboard = []


    def isValid(self, row, col, n, chessboard):
        # row 
        for i in range(n):
            if chessboard[i][col] == 'Q':
                return False 
        # col 
        for i in range(n):
            if chessboard[row][i] == 'Q':
                return False 
        # upper left 
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False 
            i -= 1
            j -= 1

        # upper right
        i = row - 1
        j = col + 1
        while i < n and j < n:
            if chessboard[i][j] == 'Q':
                return False 
            i -= 1
            j += 1

        return True 

    def backtracking(self, result, row, n, chessboard):
        # base case 
        if row == n:
            
            temp = []
            for i in range(len(chessboard)):
                temp.append("".join(chessboard[i]))
            result.append(temp)
            return 

        for i in range(n):
            if self.isValid(row, i, n, chessboard) == False:
                continue 
            chessboard[row][i] = 'Q'
            self.backtracking(result, row + 1, n, chessboard)
            chessboard[row][i] = '.'



    def solveNQueens(self, n: int) -> List[List[str]]:
        self.chessboard = [["." for _ in range(n)] for _ in range(n)]
        result = []
        self.backtracking(result, 0, n, self.chessboard)
        return result




# N queen problem:
# 1. row: depth of the tree
# 2. column: width of the tree  
# isValid(row, i, chessboard, n) -> 第 row 行 第 row 个位置是否在 n x n 的 chessboard 合法。记住一定是要在放这个动作之前去操作


# parameters
# row: 有点像 startIndex 去控制遍历的行数
# n: size of the 棋盘。有点像 len(nums)


# Time Complexity: N!
# Space Complexity: O(n^2)
# https://www.codingninjas.com/codestudio/library/n-queen