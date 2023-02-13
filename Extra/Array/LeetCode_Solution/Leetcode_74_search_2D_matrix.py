# Method 1: Brute Force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True 

        return False 

# Time Complexity: O(m * n)
# Space Complexity: O(1

# Method 2: normal approach 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])


        left = 0
        right = m * n - 1


        while left <= right:
            mid = (left + right) // 2
            cur = matrix[mid // n][mid % n]

            if cur == target:
                return True 
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Time Complexity: O(log(m * n))
# Space Complexity: O(1)