
# 先满足小胃口
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        count = 0

        for i in range(len(s)):
            if count < len(g) and s[i] >= g[count]:
                count += 1
        return count 
# 先满足大胃口
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        start = len(s) - 1
        count = 0

        for i in range(len(g) - 1, -1, -1):
            if start >= 0 and g[i] <= s[start]:
                start -= 1
                count += 1
        return count 

