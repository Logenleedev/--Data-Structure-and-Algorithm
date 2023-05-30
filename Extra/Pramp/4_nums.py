class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []


        ans = [] 
        nums = sorted(nums)


        for i in range(len(nums)):


            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1



                while left < right:

                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right -1 and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while left < right -1 and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1 
                        right -= 1
                    
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
        return ans 

