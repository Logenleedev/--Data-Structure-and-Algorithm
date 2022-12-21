class Solution:
    

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        if len(nums) < 4:
            return ans

        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                q = j + 1
                p = len(nums) - 1

                while q < p:
                    if nums[i] + nums[j] + nums[p] + nums[q] == target:
                        ans.append([nums[i], nums[j], nums[q], nums[p]])
                        while q < p - 1 and nums[q] == nums[q + 1]:
                            q += 1
                        while p > q + 1 and nums[p] == nums[p - 1]:
                            p -= 1

                    if nums[i] + nums[j] + nums[p] + nums[q] > target:
                        p -= 1
                    
                    else:
                        q += 1

        return ans 
                





