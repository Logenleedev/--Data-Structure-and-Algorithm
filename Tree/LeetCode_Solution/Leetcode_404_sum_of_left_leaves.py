# Method 1: Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        sum = 0

        que = deque([root])
        

        while que:
            size = len(que)
            
            for _ in range(size):
                node = que.popleft()

                
                    
                
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        sum += node.left.val
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return sum 


# Method 2: Recusion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 0
        
        left_current = self.sumOfLeftLeaves(root.left)

        if root.left != None and root.left.left == None and root.left.right == None:
            left_current = root.left.val
        
        right_current = self.sumOfLeftLeaves(root.right)

        return left_current + right_current 


# Method 2: Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        sum = 0

        que = deque([root])
        

        while que:
            size = len(que)
            
            for _ in range(size):
                node = que.popleft()

                
                    
                
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        sum += node.left.val
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return sum 
                

        

                

        
                

        