# BFS
from collections import deque

class Solution:
    def __init__(self):
        self.hasCycle = False
        self.indegree = []

    def BFS(self, graph):
        count = 0 

        que = deque()


        for i in range(len(self.indegree)):
            # 优先把没有 indegree 的加入
            if self.indegree[i] == 0:
                que.append(i)

        while que:
            node = que.popleft()
            count += 1

            # 加入 邻居
            for v in graph[node]:
                self.indegree[v] -= 1

                # 如果没有 indegree 那么就加入
                if self.indegree[v] == 0:
                    que.append(v)

        # 如果 不等于 那么必定有环
        return count == len(graph)


        


    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for element in prerequisites:
            from_ = element[1]
            to_ = element[0]
            self.indegree[to_] += 1
            graph[from_].append(to_)


        return graph

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.indegree = [0] * numCourses
        graph = self.buildGraph(numCourses, prerequisites)

        ans = self.BFS(graph)

        return ans
        
# DFS
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




