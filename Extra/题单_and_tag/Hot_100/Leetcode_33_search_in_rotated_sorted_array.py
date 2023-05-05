# Method 1: Brute force + binary search 

class Solution:
    def binary(self, nums, target):
        # [left, right]

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] == target:
              
                return target

            else:
                left = mid + 1


        return 


    def search(self, nums: List[int], target: int) -> int:
        index = 0 

        array = sorted(nums)
 
        ans = self.binary(array, target)

        if ans == None:
            return -1 

        for i in range(len(nums)):
            if nums[i] == ans:
                return i 

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)


# Method 2:

# find lower bound method 

class Solution:
    def binary(self, nums, target, left, right):
        # [left, right]



        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid 


        return left


    def search(self, nums: List[int], target: int) -> int:
        
        i = nums.index(min(nums))
 
        ans_1 = self.binary(nums, target, 0, i - 1)
        ans_2 = self.binary(nums, target, i, len(nums) - 1)

        if nums[ans_1] == target:
            return ans_1
        
        if nums[ans_2] == target:
            return ans_2

        return -1 

        
# Time Complexity: O(log(n))
# Space Complexity: O(1)