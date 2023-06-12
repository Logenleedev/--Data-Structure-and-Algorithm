class Solution:
    

    def __ini__(self):
        self.board = []
        self.used = []
        self.word = ""

    def backtracking(self, i, j, startIndex):
        m = len(self.board)
        n = len(self.board[0])

        # Base case
        # 注意点：这个 if 必须是第一个
        # 如果不是第一个的话 board = [["a"]] word = "a" 通过不了
        if startIndex == len(self.word):
            return True 

        # 越界
        if i < 0 or j < 0 or i >= m or j >= n:
            return False

        # 对的上 + 没来过
        if self.board[i][j] == self.word[startIndex] and self.used[i][j] == False:
            # backtracking -> adding operation

            self.used[i][j] = True 
            # find one and then return 
            
            # 找到一个就返回
            ans = self.backtracking(i + 1, j, startIndex + 1) or self.backtracking(i, j + 1, startIndex + 1) or self.backtracking(i - 1, j, startIndex + 1) or  self.backtracking(i, j - 1, startIndex + 1)

            if ans:
                return True 

            # backtracking -> undo operation
            self.used[i][j] = False

        # 没找到根本
        return False 


        
        


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.word = word

        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = self.backtracking(i, j, 0)
                    if ans == True:
                        return ans 

        return ans

# Time Complexity: O((m * n)^2)
# Space Complexity: O(m * n)
