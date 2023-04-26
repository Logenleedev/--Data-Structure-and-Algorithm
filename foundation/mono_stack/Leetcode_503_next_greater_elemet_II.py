class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        total = nums + nums

        stack = []
        ans = [-1] * len(total)

        for i in range(len(total)):
            while len(stack) > 0 and total[i] > total[stack[-1]]:
                ans[stack[-1]] = total[i]
                stack.pop()
            stack.append(i)

        return ans[: len(nums)]


