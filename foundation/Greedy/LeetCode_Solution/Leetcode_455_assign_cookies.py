
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
        # 由小到大排序
        g = sorted(g)
        s = sorted(s)

        # set the pointer in s array 
        start = len(s) - 1
        count = 0


        # loop through array g 
        for i in range(len(g) - 1, -1, -1):
            # 保证不越界。做比较。
            if start >= 0 and g[i] <= s[start]:
                start -= 1
                count += 1
        return count 

# m: length of g; n: length of s
# Time complexity: O(m*log(m) + n*log(n))
# Space complexity: O(1)