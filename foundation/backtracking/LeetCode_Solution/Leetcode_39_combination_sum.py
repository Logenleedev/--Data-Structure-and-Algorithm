class Solution:
    

    def __init__(self):
        self.candidates = []



    def backtracking(self, result, path, target, startIndex):
        
        if sum(path) >= target:
            if sum(path) == target:
                result.append(path[:])
            return 
        

        for i in range(startIndex, len(self.candidates)):
            path.append(self.candidates[i])

            # i 的原因是我们可以重复取元素
            self.backtracking(result, path, target, i)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
  

        result = []
        path = []

        self.backtracking(result, path, target, 0)

        return result 





# Time Complexity: O(n * 2^n) -> 一个比较松的上界