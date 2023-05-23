class Solution:
    # index: 应该是什么颜色
    # color[startIndex]: 实际是什么颜色
    def dfs(self, graph, color, startIndex, index):
        if color[startIndex] != 0:
            return color[startIndex] == index

        color[startIndex] = index 

        for v in graph[startIndex]:
            # 如果邻居的 color 不 match
            # 找到一个就 return
            if not self.dfs(graph, color, v, -index):
                return False 

        # 顺利走完
        return True 


    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 1 -> group 1 
        # -1 -> group -1 
        # 0 -> not visited 

        color = [0] * len(graph)



        for i in range(len(graph)):
            # 没有 visit
            if color[i] == 0:
                # 出现异常 比如不 match
                if not self.dfs(graph, color, i, 1):
                    return False 

        return True 

# Time Complexity: O(N + V)
# Space Complexity: O(N)







