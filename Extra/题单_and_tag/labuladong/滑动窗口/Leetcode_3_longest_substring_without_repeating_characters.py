# Labuladong-style method 

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1
        pointer = 0

        count = defaultdict(int)
        for i in range(len(s)):
            element = s[i]

            count[element] += 1

            while len(count.keys()) != i - pointer + 1:

                discard = s[pointer]
                count[discard] -= 1
                if count[discard] == 0:
                    del count[discard]
                pointer += 1


            result = max(result, i - pointer + 1)
        return result 

# my brute force method 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 

        pointer = 0
        result = 1
        for i in range(len(s)):
            temp = s[pointer : i + 1]
            while len(''.join(set(temp))) != i - pointer + 1:
                pointer += 1
            result = max(result, i - pointer + 1)

        return result 