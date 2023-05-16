class Solution:
    # 0 -> 
    # 1 -> rect area 
    # 2 -> visited 


        

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0 
        arr = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    arr[j] = 0
                elif matrix[i][j] == '1':
                    arr[j] += 1
            ans = max(ans, self.largestRectangleArea(arr))
        return ans

    def largestRectangleArea(self, height):
        height = [0] + height + [0]
        stack = [0]
        res = 0

        for i in range(1, len(height)):
            # min stack
            if height[i] > height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.append(i)
            else:
                # < 
                while len(stack) > 0 and height[i] < height[stack[-1]]:
                    mid_idx = stack.pop()
                    mid_idx_height = height[mid_idx]

                    if stack:
                        left_idx = stack[-1]
                        left_height = height[left_idx]
                        right_idx = i 
                        right_height = height[right_idx]
                        area = (i - left_idx - 1) * mid_idx_height
                        res = max(area, res)
                stack.append(i)

        return res 
# n -> num of col 
# m -> num of row 
# Time Complexity: O(mn)
# Space Complexity: O(n)












        