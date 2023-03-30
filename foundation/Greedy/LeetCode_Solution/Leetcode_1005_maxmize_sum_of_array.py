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

'''
本题用了两个贪心（两个局部最优）：
1. 如果把所有的负数用k取反，那么 sum 一定大
2. 如果剩余一个 k 那么我们肯定想让 k 放到 abs value 小的 value 这样影响最小
'''
 



# Time Complexity: O(n)
# Space Comlexity: O(1)