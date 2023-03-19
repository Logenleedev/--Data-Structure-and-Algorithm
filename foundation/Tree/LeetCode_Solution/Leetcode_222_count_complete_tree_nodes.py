# Method 1: Recusion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        
        result = 1 + self.countNodes(root.left)
        result = result + self.countNodes(root.right)

        return result 

# Method 2: Traverse

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        que = deque([root])

        count = 0

        while que:
            size = len(que)

            for _ in range(size):
                node = que.popleft()

                count += 1

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
        return count 

        