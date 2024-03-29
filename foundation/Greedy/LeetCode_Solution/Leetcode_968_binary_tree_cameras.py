# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traversal(root):
            nonlocal result 
            if root == None:
                return 2
            
            left = traversal(root.left)
            right = traversal(root.right)


            if left == 2 and right == 2:
                return 0

            if left == 0 or right == 0:
                result += 1
                return 1
            
            if left == 1 or right == 1:
                
                return 2
            
        
        if traversal(root) == 0:
            result += 1
        
        return result 

