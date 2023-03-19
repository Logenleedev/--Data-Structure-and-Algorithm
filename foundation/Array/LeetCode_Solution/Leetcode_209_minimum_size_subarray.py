class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sum = 0
        pointer = 0

        for i in range(len(nums)):
            sum += nums[i]

            while sum >= target:
                res = min(res, i - pointer + 1)
                sum -= nums[pointer]
                pointer += 1
                

        if res == float("inf"):
            return 0
        else:
            return res
# Time complexity O(n)
# Space complexity O(1)