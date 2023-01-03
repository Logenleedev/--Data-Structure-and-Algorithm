# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        ans = []
       

        if root == None:
            return []

        temp = [root.val]

        def travserse(root, result, temp):
            
            if root.left == None and root.right == None:
                result.append(temp)
            if root.left:
                temp += [root.left.val]
                travserse(root.left, result, temp)
                temp.pop()
            if root.right:
                temp += [root.right.val]
                travserse(root.right, result, temp)
                temp.pop()
        
        travserse(root, result, temp)

        for a in result:
            if sum(a) == targetSum:
                ans.append(a)
        return ans 
            
                
