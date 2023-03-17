# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # mid 
        # right 
        # left

        if root == None:
            return 

        stack = [root] 

        while stack:

            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack != []:
                node.left = None
                node.right = stack[-1]

        return root 

# Time Complexity: O(n)
# Space Complexity: average O(log(n)); worse case O(n)