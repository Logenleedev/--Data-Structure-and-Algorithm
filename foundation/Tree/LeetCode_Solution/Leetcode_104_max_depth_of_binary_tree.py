# Method 1: BFS

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

# Method 2: DFS - Post order
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
        
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        result = 1 + max(leftHeight, rightHeight)
        return result 

# 前序
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 1

    def getDepth(self, root, depth):
        self.result = max(depth, self.result)

        if root.left == None and root.right == None:
            return 

        if root.left != None:
            depth += 1
            self.getDepth(root.left, depth)
            depth -= 1
        
        if root.right != None:
            depth += 1
            self.getDepth(root.right, depth)
            depth -= 1

            

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0



        self.getDepth(root, 1)

        return self.result

# Time Complexity: O(n)
# Space Complexity: O(n)