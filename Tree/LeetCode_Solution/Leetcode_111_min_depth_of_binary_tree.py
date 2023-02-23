# Method 1: Traverse

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        count = 0

        que = deque()
        que.append(root)

        while que:
            size = len(que)
  
            count += 1
            
            for _ in range(size):
                node = que.popleft()

                
                
                if node.left == None and node.right == None:
                    return count 

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

            

                
        return count 

# Method 2: Recusion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        elif root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        elif root.left != None and root.right == None:
            return 1 + self.minDepth(root.left)

        
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        result = 1 + min(leftHeight, rightHeight)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)