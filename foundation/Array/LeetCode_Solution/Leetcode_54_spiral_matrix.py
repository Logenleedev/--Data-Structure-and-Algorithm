# shrink boundary 

# Time complexity O(mn)
# Space complexity O(mn)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        midx, midy = m//2, n//2
        loop = max(m, n) // 2
        startx = 0
        starty = 0

        for offset in range(1, loop + 1):
            # From left to right
            for i in range(starty, n - offset):
                if(len(ans) < m*n):
                    ans.append(matrix[startx][i])
            # From top to bottom
            for i in range(startx, m - offset):
                if(len(ans) < m*n):
                    ans.append(matrix[i][n - offset])
            # From right to left
            for i in range(n - offset, starty, -1):
                if(len(ans) < m*n):
                    ans.append(matrix[m - offset][i])

            # From bottom to top 
            for i in range(m - offset, startx, -1):
                if(len(ans) < m*n):
                    ans.append(matrix[i][starty])

            startx += 1
            starty += 1

        if m == n and n % 2 != 0:
            ans.append(matrix[m // 2][n // 2]) 
        return ans
        


# Online solution (not mine)

class Solution:
    
    def spiralOrder(self, matrix):

        if not matrix or not matrix[0]:

            return []



        res = []

        L, T = 0, 0

        R, B = len(matrix[0])-1, len(matrix)-1

        sum = len(matrix[0]) * len(matrix)

        

        while sum >= 1:

            for i in range(L, R+1):

                if sum >= 1:

                    res.append(matrix[T][i])

                    sum -= 1

            T += 1

            for i in range(T, B+1):

                if sum >= 1:

                    res.append(matrix[i][R])

                    sum -= 1

            R -= 1

            for i in range(R, L-1, -1):

                if sum >= 1:

                    res.append(matrix[B][i])

                    sum -= 1

            B -= 1

            for i in range(B, T-1, -1):

                if sum >= 1:

                    res.append(matrix[i][L])

                    sum -= 1

            L += 1

        return res
