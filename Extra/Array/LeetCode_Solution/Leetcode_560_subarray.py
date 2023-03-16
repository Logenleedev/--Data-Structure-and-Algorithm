class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        pre = 0
        ref = dict()
        ref[0] = 1


        for i in range(len(nums)):
            pre += nums[i]


            if pre - k in ref.keys():
                count += ref[pre - k]


            ref[pre] = ref.get(pre, 0) + 1
                
               


        return count 

# Time Complexity: O(n)
# Space Complexity: O(n)