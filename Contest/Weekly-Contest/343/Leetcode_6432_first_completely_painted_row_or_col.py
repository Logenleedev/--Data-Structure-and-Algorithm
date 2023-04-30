class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # val -> position
        pos = [0] * (m * n + 1)

        for i, row in enumerate(mat):
            for j, col in enumerate(mat[0]):
                pos[mat[i][j]] = (i, j)

        # pos | row -> count 
        row = [0] * m
        # pos | col -> count
        col = [0] * n
        for i, value in enumerate(arr):
            r = pos[value][0]
            c = pos[value][1]

            row[r] += 1
            col[c] += 1

            if row[r] == n or col[c] == m:
                return i 
      
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)