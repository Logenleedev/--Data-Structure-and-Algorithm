"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        results = []

        que = deque()
        que.append(root)

        while que:
            size = len(que)
            result = []

            for _ in range(size):
                node = que.popleft()

                result.append(node.val)

                if node.children:
                    length = len(node.children)
                    index = 0
                    while index < length:
                        que.append(node.children[index])
                        index += 1


            results.append(result)
        return results 