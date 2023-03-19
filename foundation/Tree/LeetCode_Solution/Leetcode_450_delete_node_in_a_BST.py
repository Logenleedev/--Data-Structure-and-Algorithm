# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return 

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            
            if root.left != None and root.right == None:
                return root.left
            
            if root.left == None and root.right != None:
                return root.right 
            
            if root.left == None and root.right == None:
                return 

            node = root.right 
            while node.left:
                node = node.left 
            node.left = root.left 
            root = root.right 
        
        return root 