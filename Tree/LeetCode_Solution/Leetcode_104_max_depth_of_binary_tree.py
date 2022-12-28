# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        count = 0
        

        que = deque()
        que.append(root)

        while que:
            size = len(que)

            for _ in range(size):
                node = que.popleft()



                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
                
            count += 1
        return count 