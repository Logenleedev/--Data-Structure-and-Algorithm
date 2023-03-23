"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # preorder traversal 

        # mid -> left -> right 

        # traversal order: mid -> right -> left
        if root == None:
            return []

        result = []

        stack = [root]

        while stack:

            node = stack.pop()

            result.append(node.val)

            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return result
                
# Time Complexity: O(n)
# Space Complexity: O()









