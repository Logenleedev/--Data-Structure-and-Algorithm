class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        res = 0

        while left < right:

            width = right - left 
            
            # left bar < right bar 
            if height[left] < height[right]:
                area = width * height[left]
                res = max(res, area)
                left += 1
            # (left bar > right bar) or (left bar == right bar)
            else:
                area = width * height[right]
                res = max(res, area)
                right -= 1
        return res 



# Time Complex: O(n) 
# Space Complex: O(1)