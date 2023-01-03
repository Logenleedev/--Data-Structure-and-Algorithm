# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, p, q):
        if p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True 
        elif p.val != q.val:
            return False 
        
        outside = self.compare(p.left, q.left)
        inside = self.compare(p.right, q.right)

        return outside and inside
            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
   
        return self.compare(p, q) 
