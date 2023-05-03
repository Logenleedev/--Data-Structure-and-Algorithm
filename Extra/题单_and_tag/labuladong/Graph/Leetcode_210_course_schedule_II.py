class Solution:
    def __init__(self):
        self.visited = []
        self.onPath = []
        self.hasCycle = False
        self.postorder = []

    def traversal(self, graph, startIndex):
        if self.onPath[startIndex] == True:
            self.hasCycle = True 
            return 
        elif self.visited[startIndex] == True or self.hasCycle == True:
            return 

        self.visited[startIndex] = True 
        self.onPath[startIndex] = True 

        for v in graph[startIndex]:
            self.traversal(graph, v)

        ## 后序
        self.postorder.append(startIndex)

        self.onPath[startIndex] = False
            


    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for element in prerequisites:
            from_, to_ = element[1], element[0]
            graph[from_].append(to_)

        return graph


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses

        graph = self.buildGraph(numCourses, prerequisites)

        for n in range(numCourses):
            self.traversal(graph, n)

        if self.hasCycle == True:
            return []
        
        ## 拓扑排序其实就是后序的 revserse。可以用二叉树举一个例子
        return self.postorder[::-1]


        