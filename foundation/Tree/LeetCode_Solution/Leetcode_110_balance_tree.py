class Solution:
    def getHeight(self, root):
        if root == None:
            return 0

        elif self.getHeight(root.left) == -1:
            return -1 
        elif self.getHeight(root.right) == -1:
            return -1 

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if abs(left - right) > 1:
            return -1 
        else:
            return 1 + max(left, right)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 
        ans = self.getHeight(root)
        if ans == -1:
            return False 
        return True 
        






# Time Complexity: O(n)
# Space Complexity: O(n)