# Method 1: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 
        stack = []
        cur = root
        result = []

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
            
        flag = True 
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                flag = False
        return flag
 
# Method 2: Recusion - inorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, result):
        if root == None:
            return 
        
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 

        result = []

        self.traverse(root , result)
            
        flag = True 
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                flag = False
        return flag
 

# Method 3: Recusion - general method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        max_value = -float("inf")
        if root == None:
            return True

        def _isvalid(root):
            nonlocal max_value
            if root == None:
                return True
            
            left_valid = _isvalid(root.left)

            if max_value < root.val:
                max_value = root.val
            else:
                return False
            
            right_valid = _isvalid(root.right)
            return left_valid and right_valid

        result = _isvalid(root)
        return result 

        
 


