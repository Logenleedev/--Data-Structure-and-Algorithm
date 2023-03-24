# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 1
        self.maxCount = 1
        self.result = []
        self.pre = None
    
    def travseral(self, root):
        if root == None:
            return 
        
        self.travseral(root.left)

        # mid 
        #      0
        #     /  \
        #   
        # 1. count 
        # 2. move pointer 
        # 3. update maxcount and append if necessary
        # define when to update count 
        if self.pre != None and root.val == self.pre.val:
            self.count += 1
        else:
            self.count = 1

        # move pointer 
        self.pre = root 

        # check when to append 
        if self.count > self.maxCount:
            self.maxCount = self.count 
            self.result = []
            self.result.append(self.pre.val)
        elif self.count == self.maxCount:
            self.result.append(self.pre.val)
            
            



        self.travseral(root.right)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return 

        self.travseral(root)

        return self.result
