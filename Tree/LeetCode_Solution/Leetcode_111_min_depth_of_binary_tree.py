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