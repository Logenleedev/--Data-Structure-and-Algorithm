
# 局部 翻转 = 全局翻转 
# step1: 沿着对角线先 mirror
# step2: 把每一行 reverse
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # mirror 
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            # 也可以把这一行改成 "matrix[i].reverse()"
            matrix[i] = matrix[i][::-1]

        return matrix

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)
