class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = [0] * 26

        for char in s:
            hash[ord(char) - ord("a")] += 1

        for i in range(len(s)):
            if hash[ord(s[i]) - ord("a")] == 1:
                return i

        return -1 