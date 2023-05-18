from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0 
            
        ref = defaultdict(int)

        for num in nums:
            ref[num] += 1

        count = 1 
        res = 1

        arr = sorted(list(ref.keys()))

        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i]:
                count = 1
            elif arr[i + 1] == arr[i] + 1:
                count += 1
            else:
                # either diff > 2 or < 
                count = 1
            res = max(res, count)

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)