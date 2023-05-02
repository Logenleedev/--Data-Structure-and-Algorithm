# Method 1: Brute Force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)


        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue 
                else:
                    product *= nums[j]

            ans[i] = product

        return ans 

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Method 2: left and right product array. Prefix product array 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)

        left_product = 1
        for i in range(len(left) - 1):
            left_product *= nums[i]
            left[i + 1] = left_product
        
        right_product = 1
        for i in range(len(right) - 1, 0, -1):
            right_product *= nums[i]
            right[i - 1] = right_product

        for i in range(len(ans)):
            ans[i] = left[i] * right[i]

        return ans 
# Time Complexity: O(n)
# SPace Complexity: O(n)




