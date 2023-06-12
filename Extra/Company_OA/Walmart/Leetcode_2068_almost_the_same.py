class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        ref1 = [0] * 26
        ref2 = [0] * 26


        for word in word1:
            ref1[ord(word) - ord('a')] += 1
        
        for word in word2:
            ref2[ord(word) - ord('a')] += 1


        for i in range(26):
            if abs(ref1[i] - ref2[i]) >= 4:
                return False 

        return True
        

# Time Complexity: O(n + m)
# Space Complexity: O(1)