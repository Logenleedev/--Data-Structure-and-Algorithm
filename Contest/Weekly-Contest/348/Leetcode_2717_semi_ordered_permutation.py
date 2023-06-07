# we only care about 1 and n. The rest of the element do not quite matter 
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        one_index = nums.index(1)
        ans = 0 
        
        
        for i in range(one_index, 0, -1):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            ans += 1
            
        
        target_index = nums.index(len(nums))
        
        for i in range(target_index, len(nums) - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            ans += 1
            
        return ans 
        
        
        
        
# Time Complexity: O(n)
# Space Complexity: O(1)