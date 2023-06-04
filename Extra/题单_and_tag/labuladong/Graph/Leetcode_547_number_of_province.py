class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * len(isConnected)
        number = 0 

        def dfs(startIndex):
            nonlocal visited, number 

            # base case 
            if visited[startIndex] == True:
                return 

            # operation
            visited[startIndex] = True 

            # neighbor 
            for v in range(n):
                # if connected and not hasn't been visited 
                if isConnected[startIndex][v] == 1 and visited[v] == False:
                    dfs(v)


        for i in range(len(isConnected)):
            if visited[i] == False:
                dfs(i)
                # 计数
                number += 1
        
        return number 

