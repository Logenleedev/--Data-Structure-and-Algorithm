# use [1,1,2] to derive the result 
class Solution:
    
    def __init__(self):
        self.candidates = []
        self.target = 0
        self.used = []
    def backtracking(self, result, path, sum, startIndex):

        # base case 
        if sum >= self.target:
            if sum == self.target:

                result.append(sorted(path[:]))
            return 

        # backtracking and loop through the set 

        for i in range(startIndex, len(self.candidates)):
            if i > 0 and self.candidates[i] == self.candidates[i - 1] and self.used[i - 1] == 0:
                continue 
            # manipulate data 
            sum += self.candidates[i]
            self.used[i] = 1
            path.append(self.candidates[i])
            self.backtracking(result, path, sum, i + 1)
            sum -= self.candidates[i]
            self.used[i] = 0
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []

        candidates = sorted(candidates)
        used = [0] * len(candidates)

        self.used = used
        self.candidates = candidates
        self.target = target
        sum = 0

        self.backtracking(result, path, sum, 0)

        return result

# Time Complexity: O(2^n * n)
# Space Complexity: O(target)