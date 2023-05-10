# BFS 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        
        stack = [start]
        seen = set()
        
        while stack:
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False

# DFS 
class Solution:
    def __init__(self):
        self.reach = False 
        self.visited = []
        self.destination = 0
        
    def dfs(self, graph, startIndex):
        if self.visited[startIndex] == True:
            return 
        
        if startIndex == self.destination:
            self.reach = True 
        
        self.visited[startIndex] = True
        
        
        for v in graph[startIndex]:
            self.dfs(graph, v)
            
        
    def graph(self, edges, n):
        graph = [[] for _ in range(n)]
        
        for element in edges:
            from_, to_ = element[0], element[1]
            
            graph[from_].append(to_)
            graph[to_].append(from_)
            
        return graph
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.destination = destination
        self.visited = [False] * n
        graph = self.graph(edges, n)
        self.dfs(graph, source)
        
        
        return self.reach
