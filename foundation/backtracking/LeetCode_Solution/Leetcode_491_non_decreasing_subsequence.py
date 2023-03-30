class Solution:
    


    def __init__(self):
        self.nums = []
    def backtracking(self, result, path, startIndex):
        # append answer 
        if len(path) >= 2:
            result.append(path[:])

        

        if startIndex == len(self.nums):
            return 

        used = set()

        for i in range(startIndex, len(self.nums)):
            # drop duplicate
            if (len(path) > 0 and self.nums[i] < path[-1]) or self.nums[i] in used:
                continue

            used.add(self.nums[i])
            path.append(self.nums[i])
            self.backtracking(result, path, i + 1)
            path.pop()


    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        result = []
        self.nums = nums

        self.backtracking(result, [], 0)


        return result 

# Time Complexity: O(2^n * n)
# Space Complexity: O(n)