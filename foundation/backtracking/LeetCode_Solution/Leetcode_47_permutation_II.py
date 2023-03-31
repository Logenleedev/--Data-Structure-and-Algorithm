class Solution:
    
    def __init__(self):
        self.nums = []
        self.used = []

    def backtracking(self, result, path):


        if len(path) == len(self.nums):
            result.append(path[:])

        for i in range(len(self.nums)):
            if self.used[i] == 1 or (i > 0 and self.nums[i] == self.nums[i - 1] and self.used[i - 1] == 0):
                continue 
            

            self.used[i] = 1
            path.append(self.nums[i])
            self.backtracking(result, path)
            self.used[i] = 0
            path.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.nums = sorted(nums)
        self.used = [0] * len(nums)

        

        self.backtracking(result, [])

        return result 

# Time Complexity: O(n! * n)
# Space Complexity: O(n)