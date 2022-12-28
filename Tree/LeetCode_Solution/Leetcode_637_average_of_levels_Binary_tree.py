# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        results = []

        que = deque()
        que.append(root)

        while que:
            size = len(que)
            result = []

            for _ in range(size):
                node = que.popleft()

                result.append(node.val)

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
            ave = sum(result) / len(result)
            results.append(ave)
        return results  





