class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        curDistance = 0
        nextDistance = 0


        step = 0

        for i in range(len(nums) - 1):
            nextDistance = max(nextDistance, nums[i] + i)

            if i == curDistance:
                curDistance = nextDistance
                step += 1

                if i == len(nums) - 1:
                    break

        return step 


