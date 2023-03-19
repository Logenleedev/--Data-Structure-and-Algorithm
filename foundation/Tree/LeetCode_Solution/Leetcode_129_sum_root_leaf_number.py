# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, path, result):

        if root.left == None and root.right == None:
            num_str = ""
            for element in path:
                num_str += element
            number = int(num_str)
            result.append(number)
        
        if root.left:
            path.append(str(root.left.val))
            self.traversal(root.left, path, result)
            path.pop()
        
        if root.right:
            path.append(str(root.right.val))
            self.traversal(root.right, path, result)
            path.pop()



    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        path = [str(root.val)]

        if root == None:
            return 
        
        self.traversal(root, path, result)

        return sum(result)
        



        