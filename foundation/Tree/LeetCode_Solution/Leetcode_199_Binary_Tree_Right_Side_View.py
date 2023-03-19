# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        results = []

        que = deque()
        que.append(root)

        while que:
            size = len(que)
            node = que[-1]
            
            results.append(node.val)

            for _ in range(size):
                node = que.popleft()

                if node.left:
                    que.append(node.left)
                     
                if node.right:
                    que.append(node.right)
                
                
            
        return results  
