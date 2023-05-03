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
        self.res = []

    def traversal(self, graph, path, startIndex):
        path.append(startIndex)

        if startIndex == len(graph) - 1:
            self.res.append(path[:])
            # 也可以这么写：
            # path.pop() -> 如果不写 pop 会报错。因为上一层节电还会留着 n - 1
            # return 

        # 单层逻辑 类似 n 叉树遍历 child
        for v in graph[startIndex]:
            self.traversal(graph, path, v)

        # 回溯
        path.pop()
        
        

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        self.traversal(graph, path, 0)
        return self.res 

# 时间复杂度：O(n^2n)，要遍历 n 层，最坏的情况是每个节点都可以去比它大的节点，与 2n2^n2n 成正比，不是严格的 2n2^n2n ，可以相像成二叉树的遍历，第 n 层有 2n2^n2n 个节点，相当于有 2n2^n2n 条路径。
# 空间复杂度：O(n^2n)，有 2^n 条路径，每条路径都需要 O(n) 的额外空间，所以，总共是 O(n * 2^n) 的额外空间复杂度。

