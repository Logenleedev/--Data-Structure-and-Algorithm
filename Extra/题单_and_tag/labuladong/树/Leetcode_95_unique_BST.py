# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generator(self, start, end):
        base case
        if start > end:
            return [None]
        
        res = []
        # choose a given num as root node
        for i in range(start, end + 1):
            # generate left tree
            left = self.generator(start, i - 1)
            # generate right tree
            right = self.generator(i + 1, end)

            for l in left:
                for r in right:
                    # connect the tree together
                    mid = TreeNode(val = i)
                    mid.left = l 
                    mid.right = r
                    res.append(mid)
        return res 

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans = self.generator(1, n)
        return ans 

# Time Complexity: O(Catalan * n)
# Space Complexity: O(Catalan * n)