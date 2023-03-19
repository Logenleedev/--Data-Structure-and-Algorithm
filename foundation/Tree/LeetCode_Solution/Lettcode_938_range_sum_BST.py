# Method 1 Brute Force: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, result):
        if root == None:
            return 
        
        result.append(root.val)
        self.traversal(root.left, result)
        self.traversal(root.right, result)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 
        result = []
        count = 0

        self.traversal(root, result)
        for num in result:
            if num >= low and num <= high:
                count += num
        
        return count 

# Method 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def traversal(self, root, low, high):
        if root == None:
            return 
        
        self.traversal(root.left, low, high)

        if root.val >= low and root.val <= high:
            self.count += root.val



        self.traversal(root.right, low, high)
        
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 
        self.traversal(root, low, high)

        return self.count 