class Solution:
    def __init__(self):
        self.nums = []
        self.used = []

    def backtracking(self, result, path, startIndex):
        # 收集所有child
        result.append(path[:])


        if startIndex == len(self.nums):
            return 

        for i in range(startIndex, len(self.nums)):
            # 树层去重逻辑
            if i > 0 and self.nums[i] == self.nums[i - 1] and self.used[i - 1] == 0:
                continue 

            path.append(self.nums[i])
            self.used[i] = 1
            self.backtracking(result, path, i + 1)
            self.used[i] = 0
            path.pop()



    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        # 树层去重一定要排序！！！！
        self.nums = sorted(nums)

        # 用来树层去重

        self.used = [0] * len(nums)


        self.backtracking(result, path, 0)


        return result 


# Time Complexity: O(2^n * n)
# Space Complexity: O(n)