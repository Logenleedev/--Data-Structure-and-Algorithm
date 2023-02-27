# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return 
        


        if root.val > val:
            result = self.searchBST(root.left, val)
        elif root.val < val:
            result = self.searchBST(root.right, val)
        elif root.val == val:
            return root 

        return result 
        
# Time Complexity: O(n) 
# Space Complexity: O(1)