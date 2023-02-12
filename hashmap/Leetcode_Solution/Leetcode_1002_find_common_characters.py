# Method 1: hash array 

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        if len(words) == 0:
            return []
        
        hash = [0] * 26

        for i in range(len(words[0])):
            hash[ord(words[0][i]) - ord("a")] += 1
        

        for i in range(1, len(words)):
            hashOther = [0] * 26
            for j in range(len(words[i])):
                hashOther[ord(words[i][j]) - ord("a")] += 1
            
            for i in range(len(hash)):
                hash[i] = min(hash[i], hashOther[i])
            
        ans = []

        for i in range(len(hash)):
            while hash[i] > 0:
                ans.append(chr(ord("a") + i))
                hash[i] -= 1
        return ans


# m -> average length of the list element
# n -> length of words
# 26


# Time Complexity: O(n(m + 26))
# Space Complexity: O(26)