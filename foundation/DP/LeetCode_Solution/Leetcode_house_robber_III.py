# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if root == None:
            return (0, 0)

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        # 不偷
        val_0 = max(left[0], left[1]) + max(right[0], right[1])
        
        # 偷
        val_1 = left[0] + right[0] + root.val

        return (val_0, val_1)
        

    def rob(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        ans = self.traverse(root)

        return max(ans)



