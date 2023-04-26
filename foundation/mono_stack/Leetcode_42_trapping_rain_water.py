class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = [0]

        for i in range(1, len(height)):
            # 找右边第一个大的元素
            # 模版
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                
                # mid 
                mid = stack.pop()
                if stack:
                    left_height = height[stack[-1]]
                    right_height = height[i]

                    bar_height = min(left_height, right_height) - height[mid]
                    bar_width = i - stack[-1] - 1
                    result += bar_height * bar_width
                
            stack.append(i)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)

# e.g. 20, 10, 30