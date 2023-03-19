# Method 1: Brute force

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer = 0

        n = len(haystack)
        g = len(needle)

        while pointer < n:
            if(haystack[pointer : g + pointer] == needle):
                return pointer
            pointer += 1
        return -1 

# Method 2: KMP

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

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = self.getnext(len(needle), needle)

        j = 0


        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                ans = i - len(needle) + 1
                return ans
        return -1 

# m -> length of haystack
# n -> length of needle

# Time Complexity: O(m + n)
# Space Complexity: O(n)