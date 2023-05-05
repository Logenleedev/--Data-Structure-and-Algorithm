






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

