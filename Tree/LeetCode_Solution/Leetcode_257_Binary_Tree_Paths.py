# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, path, result):
        path += str(root.val)
        if root.left == None and root.right == None:
            result.append(path)
        
        # 单层
        if root.left:
            self.traversal(root.left, path + "->", result)
        if root.right:
            self.traversal(root.right, path + "->", result)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        path = ''    
        if root == None:
            return []
        self.traversal(root, path, result)
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)