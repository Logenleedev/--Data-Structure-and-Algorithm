class Solution:
    
    def __init__(self):
        self.nums = []
        self.used = []

    def backtracking(self, result, path):


        if len(path) == len(self.nums):
            result.append(path[:])

        for i in range(len(self.nums)):
            # if used, then you cannnot use anymore 
            if self.used[i] == 1:
                continue 

            self.used[i] = 1
            path.append(self.nums[i])
            self.backtracking(result, path)
            self.used[i] = 0
            path.pop()
        

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.nums = nums    
        self.used = [0] * len(nums)

        

        self.backtracking(result, [])

        return result 

# Time Complexity: O(n! * n)
# Space Complexity: O(n)