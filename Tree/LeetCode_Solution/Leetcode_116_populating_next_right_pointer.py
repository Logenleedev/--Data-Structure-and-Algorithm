"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        


        que = deque()
        que.append(root)

        while que:
            size = len(que)
            

            for i in range(size):
                node = que.popleft()

                

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

                if i == size - 1:
                    break

                node.next = que[0]
                


        return root




