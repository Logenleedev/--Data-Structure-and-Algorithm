# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0 
        self.target = 0

    def traversal(self, root, sum):
        # do operation in backtracking leaf node
        if sum == self.target:
            self.count += 1

        # backtracking
        if root.left == None and root.right == None:
            return 

        if root.left:
            sum += root.left.val 
            self.traversal(root.left, sum)
            sum -= root.left.val 


        if root.right:
            sum += root.right.val 
            self.traversal(root.right, sum)
            sum -= root.right.val 
    
    def find(self, root):
        if root == None:
            return
        
        # backtracking
        self.traversal(root, root.val)

        # single layer logic 
        # find left 
        self.find(root.left)
        # find right 
        self.find(root.right)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0 
        self.target = targetSum

        self.find(root)
        return self.count 