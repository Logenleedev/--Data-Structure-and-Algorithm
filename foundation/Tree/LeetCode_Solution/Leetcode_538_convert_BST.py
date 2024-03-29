# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        
        # 右
        self.convertBST(root.right)



        # 中

        self.count += root.val

        root.val = self.count 


        # 左


        self.convertBST(root.left)

        return root 
        