# Method 1: Stack 
# Step1: buildgraph
# Step2: traverse

class Solution:

    
    def __init__(self):
        self.destination = 0
    def traversal(self, graph, source):
        # graph can help loop. This is one difference from trees 
        visited = set()

        stack = [source]

        while stack:

            node = stack.pop()

            if node == self.destination:
                return True 

            if node in visited:
                continue 
            
            visited.add(node)

            # add neighbor element 
            for v in graph[node]:
                stack.append(v)

        return False 
        
        
        
    def buildGraph(self, edges, n):
        graph = [[] for _ in range(n)]
        
        for element in edges:
            from_, to_ = element[0], element[1]
            graph[from_].append(to_)
            graph[to_].append(from_)
            
        return graph 
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        self.destination = destination
        
        graph = self.buildGraph(edges, n)
        
        ans = self.traversal(graph, source)
        
        return ans 

# Method 2: Recursion 
# Step1: buildgraph
# Step2: traverse

class Solution:
    def __init__(self):
        self.reach = False 
        self.visited = []
        self.desitination = 0
    
        
    def traversal(self, graph, startIndex):
        if self.visited[startIndex] == True:
            return 
        
        # node 
        if startIndex == self.destination:
            self.reach = True 
            
        # single layer logic 
        self.visited[startIndex] = True 
        
        for v in graph[startIndex]:
            self.traversal(graph, v)
            
        
        
    def buildGraph(self, edges, n):
        graph = [[] for _ in range(n)]
        
        for element in edges:
            from_, to_ = element[0], element[1]
            graph[from_].append(to_)
            graph[to_].append(from_)
            
        return graph 
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.visited = [False] * n 
        self.destination = destination
        
        graph = self.buildGraph(edges, n)
        
        self.traversal(graph, source)
        
        return self.reach
# m: number of edge 
# n: number of vertex 
# Time Complexity: O(m + n) 
# SPace Complexity: O(m + n)