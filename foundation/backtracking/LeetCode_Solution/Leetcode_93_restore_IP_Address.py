class Solution:
    def __init__(self):
        self.string = ''



    def backtracking(self, result, path, startIndex):
        if len(path) > 4:
            return 
        if len(path) == 4 and len("".join(path)) == len(self.string):
            
            result.append(".".join(path))
            return 
                

        for i in range(startIndex, len(self.string)):
            char = self.string[startIndex : i + 1]
            temp = int(char)
            if temp >= 0 and temp <= 255:
                if len(char) > 1 and char[0] == '0':
                    continue
                path.append(self.string[startIndex : i + 1])
                self.backtracking(result, path, i + 1)
                path.pop()

            else:
                continue 



    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        self.string = s 

        self.backtracking(result, path, 0)
        return result 

# Time Complexity: O(n * 3 ^ 4)
# Space Complexity: O(constant)