class Solution:
    

    def backtracking(self, n, k, result, path, start_index):
        
        if len(path) == k:
            result.append(path[:])
            return 

        # 元素集
        for i in range(start_index, n - (k - len(path)) + 2 ):
            # 开始取
            path.append(i)
            # 递归 -> 新的元素集
            self.backtracking(n, k, result, path, i + 1)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:

        
        result = []
        path = []

        self.backtracking(n, k, result, path, 1)

        return result

# Time Complexity: 
O(Cr(n, k) * k)

# Space Complexity:
O(n + k)
