from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ref = defaultdict(int)


        for num in nums:
            ref[num] += 1
        a = set(ref.keys())
        b = set([i for i in range(1, len(nums) + 1)])

        
        return list(b - a)
        
# Time Complexity: O(n)
# Space Complexity: O(1)