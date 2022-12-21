# Method 1: Brute force 
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return None

        ans = [] 

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans 

# Method 2: dictionary 
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records.keys():
                return [records[target - value], index]
            else:
                records[value] = index 
            
        return [] 






