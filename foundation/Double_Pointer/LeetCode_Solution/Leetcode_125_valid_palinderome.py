class Solution:
    def cleanspace(self, s):
        s = s.lower()

        result = []

        for char in s:
            if char.isalpha() == True and char != " ":
                result.append(char)
            elif char.isnumeric() == True:
                result.append(char)
        return "".join(result)


    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True 
        s = self.cleanspace(s)
        left = 0
        right = len(s) - 1
        
        result = True 

        while left <= right:
            if s[left] != s[right]:
                result = False
            left += 1
            right -= 1
        
        return result 
