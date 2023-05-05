class Solution:
    def __init__(self):
        self.destination = 0
        self.hasCycle = False
        self.onPath = []
        self.visited = []
        
    def hascycle(self, graph, startIndex):
        
        if self.onPath[startIndex] == True:
            self.hasCycle = True 
      

        if self.visited[startIndex] == True or self.hasCycle == True:
            return 


        self.onPath[startIndex] = True
        self.visited[startIndex] = True 
        

        for v in graph[startIndex]:
            self.hascycle(graph, v)
            
        self.onPath[startIndex] = False 
        
        
    
    def buildgraph(self, edges, n):
        graph = [[] for _ in range(n)]
        
        for element in edges:
            from_, to_ = element[0], element[1]
            graph[from_].append(to_)
            
        return graph 

    def search(self, graph, startIndex):
        if graph[startIndex] == []:
            return startIndex == self.destination

        return all(self.search(graph, v) for v in graph[startIndex])
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.destination = destination
        self.visited = [False] * n
        self.onPath = [False] * n
        graph = self.buildgraph(edges, n)
        
        self.hascycle(graph, source)
        

        return not self.hasCycle and self.search(graph, source)

# detect whether has cycle first 
# then search for the actual value 