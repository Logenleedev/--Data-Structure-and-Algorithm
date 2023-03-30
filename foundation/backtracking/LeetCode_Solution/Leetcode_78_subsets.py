class Solution:
    



    def __init__(self):
        # define global variable
        self.nums = []

    def backtracking(self, result, path, startIndex):
        # 在最开始收集结果
        result.append(path[:])

        # ⚠️ 注意：这里不能是 startIndex == len(self.nums) - 1。要不然会少很多种
        # 情况

        # base case
        if startIndex == len(self.nums):
            return 

        for i in range(startIndex, len(self.nums)):
            path.append(self.nums[i])
            self.backtracking(result, path, i + 1)
            path.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.nums = nums

        self.backtracking(result, path, 0)
        
        return result 

# Time Complexity: O(2^n * n)

# Space Complexity: O(len(nums))