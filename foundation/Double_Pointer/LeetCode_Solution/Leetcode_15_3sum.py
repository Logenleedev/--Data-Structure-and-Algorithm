class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1

        return nums


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.insertionSort(nums)
        
        ans = []

        if len(nums) < 3:
            return ans
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if ans != [] and ans[-1][0] == nums[i]:
                continue

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    while left < right - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left + 1 and nums[right] == nums[right - 1]:
                        right -= 1

                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
                
        return ans



                


# drop duplicate use array
class Solution:
    def insertionSort(self, nums):

        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums = self.insertionSort(nums)

        ans = []

        for i in range(len(nums)):
            cur, left, right = nums[i], i + 1, len(nums) - 1
            
            while left < right:
                if cur + nums[left] + nums[right] == 0:
                    if [cur, nums[left], nums[right]] not in ans:
                        ans.append([cur, nums[left], nums[right]])

                if cur + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans 

# Another version
class Solution:
    def insertionSort(self, nums):

        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums

# ----------------------------------------------------------------
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums = self.insertionSort(nums)

        ans = []

        for i in range(len(nums)):
            cur, left, right = nums[i], i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while left < right:
                if cur + nums[left] + nums[right] > 0:
                    
                    right -= 1

                elif cur + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.append([cur, nums[left], nums[right]])

                    while left < right - 1 and nums[left] == nums[left + 1]:
                        left += 1

                    while right > left + 1 and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return ans 


                
# Time Complexity: O(n^2)
# Space Complexity: O(n)


            
                


            