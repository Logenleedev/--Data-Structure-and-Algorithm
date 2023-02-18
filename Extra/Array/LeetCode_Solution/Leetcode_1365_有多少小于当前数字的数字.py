# Method 1:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):

            count = 0

            for j in range(len(nums)):

                if i != j and nums[j] < nums[i]:
                    count += 1
            ans.append(count)

        return ans 

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Method 2:

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []
        res = nums[:]
        res = sorted(res)
        key_value = dict()

        for index, element in enumerate(res):
            if element not in key_value.keys():
                key_value[element] = index

        for num in nums:
            ans.append(key_value[num])


        return ans 

# Time Complexity: O(n)
# Space Complexity: O(n)