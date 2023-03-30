class Solution:
    def __init(self):
        self.string = ''
    def backtracking(self, result, path, startindex):
        if startindex == len(self.string):
            result.append(path[:])
            return 

        for i in range(startindex, len(self.string)):
            temp = self.string[startindex : i + 1]
            if temp == temp[::-1]:
                path.append(temp)
                self.backtracking(result, path, i + 1)
                path.pop()
            

    def partition(self, s: str) -> List[List[str]]:

        result = []
        path = []
        self.string = s
        self.backtracking(result, path, 0)
        return result 

# let k be the average length of the path array 
# Time Complexity: O(k * 2^n)
# Space Complexity: O(len(s))