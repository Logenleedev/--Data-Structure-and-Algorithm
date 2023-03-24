class Solution:
    


    def __init__(self):
        self.candidates = []
        self.target = 0

    def backtracking(self, result, path, sum, startIndex):

        # base case 
        if sum >= self.target:
            if sum == self.target:
                result.append(path[:])
            return 

        # backtracking and loop through the set 

        for i in range(startIndex, len(self.candidates)):
            # manipulate data 
            sum += self.candidates[i]
            path.append(self.candidates[i])
            self.backtracking(result, path, sum, i)
            sum -= self.candidates[i]
            path.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []
        self.candidates = candidates
        self.target = target
        sum = 0

        self.backtracking(result, path, sum, 0)

        return result

# Time Complexity: O(S): S是所有可行解的长度之和
# Space Complexity: O(target)