from collections import defaultdict
class Solution:

    def __init__(self):
        self.ref = defaultdict(list)        

    def buildgraph(self, n, edges):
        graph = [[] for _ in range(n)]

        for element in edges:
            from_, to_ = element[0], element[1]
            graph[from_].append(to_)
            self.ref[to_].append(from_)

        return graph 

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:


        graph = self.buildgraph(n, edges)

        ans = []

        for i in range(n):
            if i not in self.ref.keys():
                ans.append(i)

        return ans

# Time Complexity: O(n + v)
# Space Complexity: O(n)