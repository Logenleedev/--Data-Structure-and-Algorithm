class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # num -> freq 


        map = dict()

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        target = len(nums) // 3 

        ans = []
        for key, freq in map.items():
            if freq > target:
                ans.append(key)


        return ans 


# Time Complexity: O(n)
# Space Complexity: O(n)