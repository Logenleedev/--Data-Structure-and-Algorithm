class Solution:
    def __init__(self):
        self.hasCycle = False

    def traverse(self, graph, visited, onPath, startIndex):
        if onPath[startIndex] == True:
            self.hasCycle = True 

        if visited[startIndex] == True or self.hasCycle == True:
            return 

        visited[startIndex] = True 
        onPath[startIndex] = True 

        for v in graph[startIndex]:
            self.traverse(graph, visited, onPath, v)

        onPath[startIndex] = False 

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        # O(m) m -> # of classes/edge
        for element in prerequisites:
            from_ = element[1]
            to_ = element[0]

            graph[from_].append(to_)

        return graph

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = self.buildGraph(numCourses, prerequisites)

        visited = [False] * numCourses
        onPath = [False] * numCourses

        # O(n)
        for n in range(numCourses):
            self.traverse(graph, visited, onPath, n)

        return not self.hasCycle

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)




