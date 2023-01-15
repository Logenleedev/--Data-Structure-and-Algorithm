# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def traverse(self, root, result):
        if root == None:
            return 
        
        self.traverse(root.left, result)

        result.append(root.val)

        self.traverse(root.right, result)

        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        self.traverse(root1, self.result)
        self.traverse(root2, self.result)


        ans = sorted(self.result)

        return ans 
        