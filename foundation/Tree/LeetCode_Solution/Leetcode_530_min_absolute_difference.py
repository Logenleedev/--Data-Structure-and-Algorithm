# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.ans = float("inf")

    def traversal(self, cur):
        if cur == None:
            return 
        
        self.traversal(cur.left)



        if self.pre != None and cur != None:
            difference = abs(cur.val - self.pre.val)

            self.ans = min(difference, self.ans)

        self.pre = cur 
        

        self.traversal(cur.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 
        self.traversal(root)
        return self.ans