
# 总体思路：
# 把 ( / ) 括号问题转化成 选 / 不选 的问题。那其实就是一个组合的问题

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0 
    def dfs(self, i, open, result, path):
        # if combo is full 
        if i == self.m:
            # append answer 
            result.append(''.join(path[:]))
            return 

        # (similiar to if root.left)    
        # 选左括号 (
        if open < self.n:
            # 回溯三明治 操作 - 递归 - 撤销

            path.append('(')
            self.dfs(i + 1, open + 1, result, path)
            path.pop()

        # (similiar to if root.right)
        # 选右括号 )
        if i - open < open:
            path.append(')')
            self.dfs(i + 1, open, result, path)
            path.pop()



    def generateParenthesis(self, n: int) -> List[str]:

        self.m = n * 2 
        self.n = n 
        result = []
        path = []
        self.dfs(0, 0, result, path)
        return result 

# Time Complexity: O(2^2n * n)
# Space Complexity: O(2n)