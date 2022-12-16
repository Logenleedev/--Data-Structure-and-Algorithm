# Method 1: KMP

class Solution:
    def getnext(self, a, s):
   
        next = [0]*a
        j = 0
        
        next[0] = 0

        
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = next[j - 1]
            
            if s[j] == s[i]:
                j += 1
            next[i] = j
        return next 

    def repeatedSubstringPattern(self, s: str) -> bool:
        next = self.getnext(len(s), s)
        ref = next[len(next) - 1]
        if ref == 0:
            return False
        else:
            if len(s) % (len(s) - ref)  == 0:
                return True
            return False




