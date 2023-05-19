'''
Matrix Spiral Copy

Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise. 
Your function then should return that array. Analyze the time and space complexities of your solution.


input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
'''


def spiral_copy(matrix):

    m = len(matrix)
    n = len(matrix[0])
    ans = []
    offset = max(m, n) // 2 
    startX = 0 
    startY = 0 

    for offset in range(1, offset + 1):

        for i in range(startY, n - offset):
            ans.append(matrix[startX][i])


        for i in range(startX, m - offset):
            ans.append(matrix[i][n - offset])


        for i in range(n - offset, startY, -1):
            ans.append(matrix[m - offset][i])

        for i in range(m - offset, startX, -1):
            ans.append(matrix[i][startY])


        startX += 1
        startY += 1

    if m == n and m % 2 != 0:
        ans.append(matrix[m // 2][n // 2])

    return ans 


print(spiral_copy( [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]))


