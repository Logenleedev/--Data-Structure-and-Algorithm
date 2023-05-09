class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        frequency = [0] * 26

        for char in s:
            frequency[ord(char) - ord("a")] += 1

        
        for char in t:
            frequency[ord(char) - ord("a")] -= 1

        for i in range(len(frequency)):
            if frequency[i] == -1:
                return chr(i + 97)

# Time Complexity: O(len(s) + len(t))
# Space Complexity: O(26)