# Method I 
class Solution:
    

    def backtracking(self, n, k, result, path, startIndex):
        # base case
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return 

        for i in range(startIndex, 10 - (k) + 2):
            path.append(i)
            self.backtracking(n, k, result, path, i + 1)
            path.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        path = []
        self.backtracking(n, k, result, path, 1)
        return result 



# Method 2:

class Solution:
    

    def backtracking(self, n, k, result, path, sum,  startIndex):
        # base case
        if len(path) == k and sum == n:
            result.append(path[:])
            return 

        for i in range(startIndex, 10 - (k - len(path)) + 2):
            sum += i
            path.append(i)
            self.backtracking(n, k, result, path, sum,  i + 1)
            sum += i
            path.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        path = []
        sum = 0
        self.backtracking(n, k, result, path, sum, 1)
        return result 

# Method 2:

class Solution:
    

    def backtracking(self, n, k, result, path, sum,  startIndex):
        if sum > n:
            return 

        # base case
        if len(path) == k and sum == n:
            result.append(path[:])
            return 

        for i in range(startIndex, n - (k - len(path)) + 2):
            sum += i
            path.append(i)
            self.backtracking(n, k, result, path, sum,  i + 1)
            sum -= i
            path.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        path = []
        sum = 0
        self.backtracking(n, k, result, path, 0, 1)
        return result 

# Time Complexity: 
# O(Cr(n, k) * k)

# Space Complexity:
# O(9 + k) = O(9)