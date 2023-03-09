# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return 0



        que = deque([root])

        results = []


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

            results.append(sum(result))

        results = sorted(results)
        
        counter = 1
        if len(results) < k:
            return -1 
        
        for i in range(len(results) - 1, -1, -1):
            if counter == k:
                return results[i]
            else:
                counter += 1

        
# Time Complexity: O(n)
# Space Complexity: O(n)