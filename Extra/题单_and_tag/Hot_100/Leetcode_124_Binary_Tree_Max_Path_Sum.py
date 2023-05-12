# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 1. root 
        # 2. left 
        # 3. right 
        # 4. left + root 
        # 5. right + root 
        # 6. root + left + right 
        

        max_val = float("-inf")
        def scan(root):
            nonlocal max_val

            if root == None:
                return 0

            # Post order 
            left = scan(root.left)
            right = scan(root.right)
            # case 6
            max_val = max(max_val, root.val + left + right)
            # case 4, 5, 1, 2, 3
            return max(0, max(left, right) + root.val)
            

        scan(root)

        return max_val

# Time Complexity: O(n)
# Space Complexity: O(n)