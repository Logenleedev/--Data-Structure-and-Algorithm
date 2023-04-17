# Method 1: Hash
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref = dict()

        for num in nums:
            ref[num] = ref.get(num, 0) + 1
        
        for key, value in ref.items():
            if value > (len(nums) // 2):
                return key 

# Time Complexity: O(n)
# Space Complexity: O(n)

