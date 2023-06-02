from collections import deque
from collections import defaultdict
class Solution:
    # build the graph
    def buildgraph(self, equations, values):

        graph = defaultdict(list)


        for i, eq in enumerate(equations):
            a, b = eq

            # directed graph
            # node -> (target, value)
            # if a / b = 3, then we know for sure that b / a = 1/3
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        return graph



    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildgraph(equations, values)

        def bfs(source, target):
            if source not in graph.keys() or target not in graph.keys():
                return -1

            que = deque([(source, 1)])
            
            visited = set()
            visited.add(source)


            # DFS 四部曲：p, a, 操, nei
            while que:
   
                n, w = que.popleft()
               

                if n == target:
                    return w 
                
                

                for v, weight in graph[n]:
                    if v not in visited:
                        que.append((v, w * weight))
                        visited.add(v)
            return -1

        return [bfs(q[0], q[1]) for q in queries]

# Time Complexity: O()
# Space Complexity: O()



