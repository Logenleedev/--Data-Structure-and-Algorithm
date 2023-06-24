class Solution:
    def inorderSuccessor(self, root, num):
        successor = None 

        while root:
            if root.val >= num:
                root = root.left 
            else:
                successor = root
                root = root.right
                 
                

        return successor