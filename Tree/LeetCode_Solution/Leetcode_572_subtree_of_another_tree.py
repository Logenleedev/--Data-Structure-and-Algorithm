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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        elif root == None and subRoot != None:
            return False
        elif root != None and subRoot == None:
            return False
        
        if self.compare(root, subRoot):
            return True
        return  self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 