#  Method 1: hash array
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapps = [0] * 26
        for i in range(len(magazine)):
            mapps[ord(magazine[i]) - ord("a")] = mapps[ord(magazine[i]) - ord("a")] + 1
        
        for j in range(len(ransomNote)):
            address = ord(ransomNote[j]) - ord("a")

            mapps[address] = mapps[address] - 1
        
        for num in mapps:
            if num < 0:
                return False
        
        return True 

# Method 2: Python dictionary
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = dict()

        for s in ransomNote:
            if s in hash:
                hash[s] += 1
            else:
                hash[s] = 1
            
        for s in magazine:
            if s in hash.keys():
                hash[s] -= 1
        
        
        for count in hash.values():
            if count > 0:
                return False
        
        return True 

# m -> the length of the first string
# n -> the length of the second string  

# Time Complexity: O(m + n)
# Space Complexity: O(|s|) |s| = 26