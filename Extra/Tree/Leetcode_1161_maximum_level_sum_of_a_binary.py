# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 
        
        que = deque([root])
        res = 0
        max_val = float("-inf")
        count = 0

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

            count += 1

            if max_val < sum(result):
                max_val = sum(result)
                res = count
            



        return res

# Time Complexity: O(n)
# Space Complexity: O(n)