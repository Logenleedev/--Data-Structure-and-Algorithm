class Solution:
    def dfs(self, graph, startIndex, visited):
        if visited[startIndex] == True:
            return 

        visited[startIndex] = True 

        for v in graph[startIndex]:
            # if visited[v] == False:
            self.dfs(graph, v, visited)

    def buildgraph(self, n, edges):
        graph = [[] for _ in range(n)]

        for element in edges:
            from_, to_ = element[0], element[1]
            graph[from_].append(to_)
            graph[to_].append(from_)

        return graph

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.buildgraph(n, edges)
        visited = [False] * len(graph)
        res = 0 


        for i in range(n):
            # 如果没有被 visited 过
            if visited[i] == False:
                self.dfs(graph, i, visited)
                # 遍历完 +1 
                res += 1

        return res 

        