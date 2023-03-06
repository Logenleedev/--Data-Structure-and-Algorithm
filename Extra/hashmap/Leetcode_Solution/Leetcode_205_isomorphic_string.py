from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        default_1 = defaultdict(str)
        default_2 = defaultdict(str)


        for i in range(len(s)):
            # create s -> t
            if not default_1[s[i]]:
                default_1[s[i]] = t[i]

            # create t -> s
            if not default_2[t[i]]:
                default_2[t[i]] = s[i]

            # check if the reference is correct
            if default_1[s[i]] != t[i] or default_2[t[i]] != s[i]:
                return False 

        return True 

# Time Complexity: O(n)
# Space Complexity: O(26)