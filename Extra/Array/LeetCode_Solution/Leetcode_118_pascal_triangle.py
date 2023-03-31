# Brute force
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = [[1]]

        # i means the # of element in each row
        for i in range(2, numRows + 1):
            temp = []
            # j index loop through each row
            for j in range(i):
                # start and end of every row must be 1
                if j == 0 or j == i - 1:
                    temp.append(1)
                # sum the element based on the definition 
                else:
                    temp.append(res[-1][j] + res[-1][j - 1])

            res.append(temp)

        return res 

# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)