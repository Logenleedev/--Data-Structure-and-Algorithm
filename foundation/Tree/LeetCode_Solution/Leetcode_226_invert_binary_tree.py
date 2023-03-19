#  Method 1: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 
        
      

        que = deque([root])

        while que:

            size = len(que)

            for _ in range(size):
                node = que.pop()
                
                
                node.left, node.right = node.right, node.left
                

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
                


        
        return root

#  Method 2: DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 














# Time Complexity:  O(n)
# Space Complexity: O(n)