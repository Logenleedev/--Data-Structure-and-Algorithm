# Method 1: Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            for i in range(len(node.children)):
                stack.append(node.children[i])

        return res[::-1]

            
# Time Complexity: O(n)
# Space Complexity: O(n)

# Method 2: recursion 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, root, res):
        if root == None:
            return

        for child in root.children:
            self.traverse(child, res)

        res.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

    
        res = []
        self.traverse(root, res)
        return res


# Time Complexity: O(n)
# Space Complexity: O(n)