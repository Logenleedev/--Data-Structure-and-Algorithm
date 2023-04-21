# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if root == None:
            return []
        ref = defaultdict(int)
        self.traverse(root, ref)
        return self.res 

    def traverse(self, root, ref):
        if root == None:
            return '#'

        left = self.traverse(root.left, ref)
        right = self.traverse(root.right, ref)

        chain = left + ',' + right + ',' + str(root.val)
        ref[chain] += 1
        if ref[chain] == 2:
            self.res.append(root)
        return chain
