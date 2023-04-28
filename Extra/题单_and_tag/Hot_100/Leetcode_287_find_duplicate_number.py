# Method 1: Brute force

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return nums[i]

# Time Complexity: O(n * log(n))
# Space Complexity: O(n)

# Binary Search
class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:

        left = 0

        right = len(nums) - 1

        while(left < right):

            mid=(left+right)//2

            count=0

            for num in nums:

                if(num<=mid):

                    count+=1
            
            # example: [1,2,3,3]
            if(count<=mid):
                # 搜索 (mid, right]
                left= mid+1
            
            # example: [1,1,2,3]
            else:
                # 搜索 [left, mid]
                right = mid

        return left


