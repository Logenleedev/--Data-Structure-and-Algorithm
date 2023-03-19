# Method 1: Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0


        que = deque([root])
        results = []

        while que:
            size = len(que)
            results.append(que[0].val)

            for _ in range(size):
                node = que.popleft()
     
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return results[-1]
# Method 2: Recusion
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -float("INF")
        leftmost_val = 0

        def __traverse(root, cur_depth): 
            nonlocal max_depth, leftmost_val
            if not root.left and not root.right: 
                if cur_depth > max_depth: 
                    max_depth = cur_depth
                    leftmost_val = root.val  
            if root.left: 
                cur_depth += 1
                __traverse(root.left, cur_depth)
                cur_depth -= 1
            if root.right: 
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1

        __traverse(root, 1)
        return leftmost_val

# Time Complexity: O(n)
# Space Comlexity: O(n)

