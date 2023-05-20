# Method 1: Brute Force 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        temp = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    temp.append([i, j])

        for element in temp:
            # change row 
            r, c = element[0], element[1]
            matrix[r] = [0] * n 
            
            for j in range(m):
                matrix[j][c] = 0

        return matrix


                    

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)


# Method 2: clever way 

