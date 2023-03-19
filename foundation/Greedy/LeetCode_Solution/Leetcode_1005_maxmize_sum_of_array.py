class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key = abs, reverse=True)



        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1

        while k > 0:
            nums[-1] *= -1
            k -= 1

        
        return sum(nums)


# Time Complexity: O(n)
# Space Comlexity: O(1)