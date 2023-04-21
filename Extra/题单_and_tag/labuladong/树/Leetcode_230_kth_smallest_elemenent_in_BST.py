# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def travserse(self, root):
        if root == None:
            return 
        
        self.travserse(root.left)
        self.res.append(root.val)
        self.travserse(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.travserse(root)

        return self.res[k - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)


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
        self.res  = 0 

    def travserse(self, root, k):
        if root == None:
            return 
        
        
        self.travserse(root.left, k)

        self.count += 1
        if self.count == k:
            self.res = root.val
            
        self.travserse(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.travserse(root, k)

        return self.res

# Time Complexity: O(n)
# Space Complexity: O(1)