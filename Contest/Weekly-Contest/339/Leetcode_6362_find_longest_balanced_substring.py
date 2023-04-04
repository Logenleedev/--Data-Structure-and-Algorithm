# 暴力
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
 
        
        res = float("-inf")
        # can also set res = 0

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                substring = s[i : j + 1]
                if substring.count("0") != substring.count("1") or (j - i + 1) % 2 != 0:
                    continue 
                else:
                    half = (j - i + 1) // 2
                    if substring != '0'*half + '1'*half:
                        continue
                    else:
                        res = max(res, half * 2)


        return res if res != float("-inf") else 0

# Time Complexity: O(n^2)
# Space Complexity: O(n)
