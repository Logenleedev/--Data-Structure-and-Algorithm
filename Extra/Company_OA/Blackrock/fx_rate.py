'''
USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155
USD
JPY
'''
from collections import defaultdict
from collections import deque
import sys



equations = []
values = []
a = ""
b = ""

for line in sys.stdin:
    if equations == []:
        temp = line.split(';')
       
        for c in temp:
            element = c.split(',')
            source = element[0]
            target = element[1]
            value = float(element[2])
    
            equations.append([source, target])
            values.append(value)
        # print(values)
    elif a == "":
        a = line.strip()
    elif b == "":
        b = line.strip()
        break


print(equations)
# print(values)
# print(a)
# print(b)










# print(equations)
# print(values)
# print(a)

def buildgraph(equations, values):
    
    graph = defaultdict(list)


    for i, eq in enumerate(equations):
        a, b = eq

        # directed graph
        # node -> (target, value)
        # if a / b = 3, then we know for sure that b / a = 1/3
        graph[a].append((b, values[i]))
        graph[b].append((a, 1 / values[i]))

    return graph



def calcEquation(equations, values, queries):
    graph = buildgraph(equations, values)

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
print("-----")
print(a)
print(b)
print(calcEquation(equations, values, [[a, b]]))