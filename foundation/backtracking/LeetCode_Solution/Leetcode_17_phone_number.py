class Solution:
    
    def __init__(self):
        self.map = {

            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

    def backtracking(self, result, path, index, digits):

        if index == len(digits):
            result.append(''.join(path))
            return 

        digit = int(digits[index])
        
        # traverse set element
        for i in range(len(self.map[digit])):
            # append to temp
            path.append(self.map[digit][i])
            self.backtracking(result, path, index + 1, digits)
            # backtracking
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = []
        path = []


        self.backtracking(result, path, 0, digits)

        return result 


# m -> 3 字母的数量
# n -> 4 字母的数量

# Time Complexity: O(3^m * 4^n)
# Space Complexity: O(m + n) 基本上就是 O(length of the digit string)
