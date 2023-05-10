"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def dfs(self, node):
        # base case 
        # node is None 
        if node == None:
            return 

        # self loop 
        if node in self.visited.keys():
            return self.visited[node]

        copy = Node(node.val, [])
        self.visited[node] = copy 

        for v in node.neighbors:
            copy.neighbors.append(self.dfs(v))

        return copy
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        # visited[0] is 0, but it is fine 
        ans = self.dfs(node)
        return ans 
        
        
# Time Complexity: O(V + E)
# Space Complexity: O(V)