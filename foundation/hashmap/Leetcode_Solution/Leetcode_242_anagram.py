# Method 1: My solution of using python map 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapps = {}
        for i in range(len(s)):
            if s[i] not in mapps.keys():
                mapps[s[i]] = 1
            else:
                mapps[s[i]] = mapps[s[i]] + 1
        
        for i in range(len(t)):
            if t[i] not in mapps.keys():
                return False
            else:
               mapps[t[i]] = mapps[t[i]] - 1

        for values in mapps.values(): 
            if values != 0:
                return False
        return True 

# Method 2: Implement an array map 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0] * 26

        for i in s:
            a[ord(i) - ord('a')] = a[ord(i) - ord('a')] + 1
        
        for i in t:
            a[ord(i) - ord('a')] = a[ord(i) - ord('a')] - 1
        
        for j in range(len(a)):
            if a[j] != 0:
                return False
        return True

# Method 3 - Method 1的简化版
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mapps = {}


        for char in s:
            mapps[char] = mapps.get(char, 0) + 1

        for char in t:
            if char not in mapps.keys():
                return False
            else:
                mapps[char] -= 1

        
        for value in mapps.values():
            if value != 0:
                return False 
            
        return True 

# Time Complexity: O(n)
# Space Complexity: O(1)


